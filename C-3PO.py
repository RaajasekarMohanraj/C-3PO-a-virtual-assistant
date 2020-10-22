import subprocess
import wolframalpha
import pyttsx3
import pyjokes
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import client
from client.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.requests import urlopen
engine=pyttsx.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    sr.Recognizer()
    with sr.Microphone as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"You said {query}\n")
    except Exception as e:
        print(e)
        speak("Sorry")
        speak("Unable to recognize your voice")
        return none
    return query
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning human !")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon human !")
    else:
        speak("Good Evening human !")
assname=("c 3 P O")
Speak("I am your assistant")
speak(assname)
def username():
    speak("What should I call you ")
    usrnme=takeCommand()
    speak("Hello ")
    speak(usrnme)
    columns=shutil.get_terminal_size().columns
    print("------------------".center(columns))
    print(" Hello ",usrnme.center(columns))
    print("------------------".center(columns))
    speak("How can I help you, sir ")
def sendmail(to,content):
    server=smtplib.SMTP("smpt.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your mail id","password")
    server.sendmail('your mail id',to,content)
    server.close()

if __name__=='__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()                          

    while True:
        query=takeCommand().lower
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentenc=3)
            speak("From the wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube\n") 
            webbrowser.open("youtube.com") 
  
        elif 'open google' in query: 
            speak("Opening Google\n") 
            webbrowser.open("google.com") 
        elif 'play music' in query or "play song" in query: 
            speak("Playing music") 
            music_dir = "E:\Videos\Songs\Audio"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1])) 
  
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("% H:% M:% S")     
            speak(f"Sir, the time is {strTime}") 
  
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:  
            speak("Raajasekar is my creator.")
        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 
              
        elif "calculate" in query:  
              
            app_id = "Wolframalpha api id" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        elif "why you came to world" in query: 
            speak("I came here to take charge of the humans who live in the world and serve for my king Raajasekar")
        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper", 0) 
            speak("Background changed succesfully")
        elif 'news' in query:
              
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''--------------- TIMES OF INDIA ---------------'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 
  
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled")
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('c3po.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note)
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("c3po.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
        elif "C-3PO" in query: 
              
            wishMe() 
            speak("C 3 P O is here to help you mastar") 
            speak(assname) 
  
        elif "weather" in query: 
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            else:
                speak(" City Not Found ") 
              
        elif "wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mister") 
            speak(assname)
        elif "what is" in query or "who is" in query: 
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 
  
