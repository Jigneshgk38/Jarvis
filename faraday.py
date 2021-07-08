import os
import pyjokes
import pyautogui
import time
import requests
import cv2
import PyPDF2
from geopy.geocoders import Nominatim
import json
from bs4 import BeautifulSoup
import speedtest
import speech_recognition as sr
import pywhatkit as kit
import pyttsx3
import datetime
import webbrowser
import wikipedia




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query    



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Good Morning! it is {strTime}")
        print(f"Good Morning! it is {strTime}")

    elif hour>=12 and hour<18:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Good Afternoon! it is {strTime}")
        print(f"Good Afternoon! {strTime}")

    else:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Good Evening! it is {strTime}")
        print(f"Good Evening!  it is {strTime}")

    speak("I am Faraday Sir. Please tell me how may I help you")


def read_pdf():
    
    book = open('Python.pdf','rb')
    reader = PyPDF2.PdfFileReader(book)
    pages = reader.numPages
    speak(f"Total number of pages in this book {book}")
    speak("sir please enter the page number i have read ") 
    pg = int(input("sir please enter the page number : "))
    page = reader.getPage(pg)
    text = page.extractText()
    speak(text)


wishMe()
while True:
    query = takecommand().lower()
    if 'search' in query:
        speak('Searching in Wikipedia...')
        query = query.replace("search", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Opening youtube .......")
        webbrowser.open_new_tab('www.youtube.com')

    elif 'open google' in query:
            speak("Opening  google  .......")
            webbrowser.open_new_tab('www.google.com')

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

    elif 'play music' in query:
        webbrowser.open_new_tab('https://music.youtube.com/watch?v=3THNdrvc9bQ')
        

    elif 'open whatsapp'  in query:
        speak("Opening Whatsapp......")
        webbrowser.open_new_tab('https://web.whatsapp.com')


    elif 'i want to watch pokemon' in query:
        speak("Sir let's watch pokemon ")
        webbrowser.open_new_tab('www.youtube.com/channel/UCR1r4GPUBvdI0EJBpxKYPQQ')

    elif 'set alarm' in query:
        nn = int(datetime.datetime.now().hour)
        if nn == 6:
            music_dir = 'E:\\Musics'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))


    elif 'open cmd' in query:
        os.system("start cmd")

    elif 'open chrome' in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'open abode reader' in query:
        os.startfile("C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe")

    elif 'tell me a joke' in query:
        joke = pyjokes.get_joke(language="en", category="all")
        speak(joke)
        print(joke)

    elif 'take screenshot' in query:
        speak("name of screenshot file")
        op = takecommand().lower()
        time.sleep(5)
        img = pyautogui.screenshot()
        img.save(f"{op}.png")
        speak("sir screenshot file is saved in main folder")

    elif 'where we are' in query:
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode("Thanesar Kurukshetra")
        
        print(getLoc)
        speak(f"sir we are at{getLoc}")
        
        
        
    
    elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print(f"your IP address is {ip}")

    elif 'volume up' in query:
        pyautogui.press("volumeup")

    elif 'volume down' in query:
        pyautogui.press("volumedown")

    elif 'mute' in query:
        pyautogui.press("volumemute")

    elif 'shut down system' in query:
        os.system("shutdown /s /t 5")

    elif 'restart system' in query:
        os.system("shutdown /r /t 5")

    elif 'switch the windows' in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(4)
        pyautogui.keyUp("alt")

    elif 'read pdf' in query:
        read_pdf()

    elif 'temperature' in query:
        search = "temperature in kurukshetra"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"current {search} is {temp}")
        print(f"current {search} is {temp}")

    elif 'test network speed' in query:
        st = speedtest.Speedtest()
        dl = st.download()
        upl = st.upload()
        speak(f"sir we have {dl} bit per second downloding speed and {upl} bit per second uploding speed")
        print(f"sir we have {dl} bit per second downloding speed and {upl} bit per second uploding speed")

    elif 'good bye' in query:
        quit()
        

    elif 'set timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand().lower()
            timing =timing.replace('minutes', '')
            
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing*60
            speak(f'I will remind you in {timing} seconds')
            time.sleep(timing)
            speak('Your time has been finished sir'
    
    )

    elif 'goodbye' in query:
        speak("bye sir if you need any help call me ")
        quit()

    elif 'send message using whatsapp' in query:
        speak("what do i say")
        whatsapp = takecommand().lower()
        speak("in wich hour")
        hour = takecommand().lower()
        speak("in wich minute")
        time = takecommand().lower()
        kit.sendwhatmsg("+919355211323",whatsapp,9,19)

    elif 'open our main folder' in query:
        os.startfile("D:\\J.A.R.V.I.S")

    elif "song on youtube" in query:
        kit.playonyt("see you again")


    elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')    

    elif 'calculate' in query:
        speak("what do i calculte")
        l = input("JARVIS : ")
        poter = eval(l)
        print(poter)
        speak(poter)     


