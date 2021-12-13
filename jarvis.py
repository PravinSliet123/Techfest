from typing import NoReturn, Sequence
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
from pyttsx3 import engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour >=12 and hour<18:
        speak("good afternoon")
    else:
        speak("sat shri akaal")
    speak("this is chhitti two point o fifteen terabite. please tell me how may i help you")
def takeCommand():
    #it takes microphone input from the user and return  string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try: 
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
                # print(e)
                print("Say Again please....")
                return "none"
        return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube jarvis' in query:
            speak("wait opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google jarvis' in query:
            speak("ok sir opening google")
            webbrowser.open("google.com")
        elif 'codechef' in query:
            speak("its a good platform for learn coding")
            webbrowser.open("codeChef.com")
        elif 'open my gmail jarvis' in query:
            speak("openning gmail ")
            webbrowser.open("gmail.com")
        elif 'play music ' in query:
            music_dr = 'D:\\my music'
            my_music = os.listdir(music_dr)
            print(my_music)
            os.startfile(os.path.join(music_dr, my_music[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'open browser' in query:
            browPath = "C:\\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(browPath)
        elif 'tauba' in query:
            os.abort()
        # elif 'stop music' in query:
        #     music_dr = 'D:\\my music'
        #     my_music = os.listdir(music_dr)
          
           
         
           


