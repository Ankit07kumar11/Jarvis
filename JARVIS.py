import time
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import email.mime.image
from playsound import playsound


engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to conert voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold=1
        audio=r.listen(source,timeout=2,phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please.....")
        return "none"
    return query

# to get daily news
def news():
        main_url ='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=559bdf7e85f742738a0d4a6d1f580919'
        main_page= requests.get(main_url).json()

        # print (main_page)
        articles = main_page["articles"]
        #print(article)
        head = []

        day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range (len(day)):
            #print(f"today's {day[i]} news is :",head[i])
            speak(f"today's {day[i]} news is : {head[i]}")


# to wish
def wish():

    tt=time.strftime("%I:%M ")
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak(f"good morning sir,its {tt}")

    elif hour>12 and hour<18:
        speak(f"good afternoon sir,its {tt}")

    else :
        speak(f"good evening sir,its {tt}")

    speak("i am jarvis, sir please tell me how i can help you")

#to send email
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aky56074@gmail.com','auikpupohkxoqtlq')
    server.sendmail('aky56074@gmail.com',to,content)
    server.close()


if __name__=="__main__":
    wish()
    # takecommand()

    while True:
    # if 1:

        query=takecommand().lower()

        #logic building for task

        if "open notepad" in query:
            npath="C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(npath)

        elif"open command propmt" in query:
            os.system("start cmd")

        elif"open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;

            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir="C:\\music"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            for songs in songs:
                if songs.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,songs))

        elif"ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif"wikepedia" in query:
            speak("searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=5)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif"open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif"open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif"open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif"open google" in query:
            speak("sir,  what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")

        elif"send message" in query:
            kit.sendwhatmsg("+917428107443","hello this is a testing message by Jarvis",10,17)

        elif" song on youtube" in query:
            speak("which song you want to listen sir")
            name=takecommand()
            kit.playonyt(name)

        elif"mail to ankit" in query:
            try:
                to = "ankitkumar56074@gmail.com"
                speak("what should i say ,sir?")
                content=takecommand().lower()
                sendEmail(to,content)
                speak("email has been sent to ankit")

            except Exception as e:
                print(e)
                speak("sorry sir,i am not  able to send this email")

        elif "you can sleep" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()


        # speak("sir do you have any other work?")
    #to close any application
        elif"close notepad" in query:
            speak("okay sir,closing notepad")
            os.system("taskkill/f /im notepad++.exe")

    #to set an alarm
        elif"set alarm" in query:
            nn =int(datetime.datetime.now().hour)
            if nn==(15):
                music_dir="C:\\music"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[1]))

    # to find a joke
        elif"tell me a joke "in query:
            joke=pyjokes.get_joke()
            speak(joke)

        elif"shutdown the system "in query:
            os.system("shutdown /s /t 1")

        elif "restart the system" in query:
            os.system("shutdown /r/t 5")

        elif"sleep the system" in query:
            os.system("rund1132.exe powrprof.dll,setsuspendstate 0,1,0")

        elif"switch window"in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.keyUp("alt")

        elif"news"in query:
            speak("please wait sir,fetching the latest news")
            news()


        elif"email to ankit"in query:
            speak("sir what would i say?")
            query=takecommand().lower()
            if"send a file" in query:
                email='aky56074@hmail.com'#your mail id
                password='auikpupohkxoqtlq' #password
                send_to_email='ankitkumar56074@gmail.com' # to whom you are sending mail

                speak("okay sir,what is the subject for this email")
                query=takecommand().lower()
                subject=query  #subject of this email

                speak("and sir what is the message for this email")
                query2=takecommand().lower()
                message=query2  # the message in mail

                speak("sir please enter the correct path of the file into the shell")
                file_location =input("please the path of file: ")    #the file attatchment in the emial

                speak("please wait, i am sending the email now")


                msg= MIMEMultipart()
                msg['From']=email
                msg['To']=send_to_email
                msg['subject']=subject

                msg.attach(MIMEText(message,'plain'))

            # setup the attachment

                filename=os.path.basename(file_location)
                attachment = open(file_location,'rb')
                part=MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content_Disposition',"attachment; filename=%s" % filename)

                #attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.ehlo()
                server.login(email,password)
                # server.login('aky56074@gmail.com','#9PassworD?incorrent#@#@#@')
                text= msg.as_string()
                server.sendmail('aky56074@gmail.com','ankitkuamr56074@gmail.com',text)
                server.quit()
                speak("email has been sent to ankit")

            else:
                email = 'aky56074@hmail.com'  # your mail id
                password = 'auikpupohkxoqtlq'  # password
                send_to_email = 'ankitkumar56074@gmail.com'  # to whom you are sending mail
                message = query # the message in email

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()  #use TLS
                server.login(email,password) #login  to email server
                # server.login('aky56074@gmail.com', 'auikpupohkxoqtlq')
                server.sendmail(email, send_to_email, message)#send the mail
                server.quit()       #logout of email server
                speak("email has been sent to ankit")

