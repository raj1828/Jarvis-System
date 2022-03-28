from datetime import date, datetime
from logging import exception
import os
from unittest import result
import speech_recognition as sr
from pip import main
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import time
# from selenium import webdriver

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)

webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

contact = {
    "sir" : "letsmail.m.raj@gmail.com",
    "adarsh" : "adarshmhatre06@gmail.com",
    "aqsa" : "sarnaikaqsa7769@gmail.com",
    "sherya" : "shreyamhatre736@gmail.com"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    # print(hour)
    if hour>=0 and hour<12:
       speak("Good Morning Sir") 
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")

    elif hour>=16 and hour<24:
        speak("Good Evening Sir")
    speak("I am Jervis Sir. Please tell me how may I help you")

def takeCommand():
    # it takes the voic inputs through microphones
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print("Say that again Please...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('myjarvisai47@gmail.com','googleraj1828')
    server.sendmail('myjarvisai47@gmail.com', to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic to execute
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            url = 'https://youtube.com'
            webbrowser.get('chrome').open(url)

        elif 'open google' in query:
            url = 'https://google.com'
            webbrowser.get('chrome').open(url)

        elif 'open stackoverflow' in query:
            url = 'https://google.com'
            webbrowser.get('chrome').open(url)

        elif 'open browser and search' in query:
            query = query.replace('open browser and search',"")
            print(query)
            # com = '.com'
            google = 'google.com/search?q='
            new = google+query
            url = new
            webbrowser.get('chrome').open(url)

        elif 'play music' in query:
            music_dir = "E:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")


        elif 'open VS code' in query:
            code_path = "C:\\Users\\mhatr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'create new folder' in query:
            try:
                query = query.replace('create new folder',"")
                print(query)
                speak("sir please check the name")
                value = takeCommand()
                if(value=="yes"):
                    directory = query
                    parent_dir = "D:/AI-Jarvis-Folder/"
                    path = os.path.join(parent_dir,directory)
                    os.mkdir(path)
                    speak("sir folder created")
                else: 
                    speak("please say the command again")
                
            except Exception as e:
                print(e)
                speak("sorry Sir can u Say this again")


        # elif 'email to sir' in query:
        #     try:
        #         speak("What should i say?")
        #         content = takeCommand()
        #         to = "letsmail.m.raj@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email Has been sent.")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry sir I am not able to send Email")


        elif 'email to ' in query:
            try:
                query = query.replace("email to ","")
                emailContact = contact[query]
                to = emailContact
                speak("What is subject?")
                subject = takeCommand()
                speak("What should i say?")
                content = takeCommand()
                # to = "letsmail.m.raj@gmail.com"
                sendEmail(to, content)
                speak("Email Has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry sir I am not able to send Email")

        elif 'jarvis you can rest now' in query:
                speak("I will be right back.")
                time.sleep(30)
                speak("I am back")

        elif 'jarvis i will call you later' in query:
            speak("Bye Sir!! Have a nice day")
            exit()
