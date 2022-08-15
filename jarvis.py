import random
import datetime
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import pyjokes
import os
import time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour< 12:
        speak("Good morning harshit sir")
    elif hour>= 12 and hour< 18:   
        speak("Good Afternoon harshit sir")
    else:
        speak("Good Evening harshit sir")
wishMe()
speak("Online and ready sir") 



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("LISTENING...")
         r.pause_threshold = 1
         r.energy_threshold = 4000
         audio = r.listen(source)

    try:
        print("RECOGNIZING....")
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        print(e)
        speak("Try to say again")
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query  = takeCommand().lower()
        print(query)
        
        if 'wikipedia' in query:
            speak("Searching on wiki")
            try:
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                
                speak("so, wikipedia says")
                speak(results)
                
            except:
                speak("Not available on wikipedia")
         
        if 'quit' in query:
            speak("Waiting for Activation sir")
            
            break
        elif 'search on google' in query:
            speak("what would you like to search sir?")
            h = takeCommand().lower()
            webbrowser.open(f"https://www.bing.com/search?q={h}")
            

        elif 'open youtube' in query:
            speak("what would you like to search on youtube")
            x = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            
         
        elif 'open web browser' in query or 'open a new tab of browser' in query or 'open a web browser' in query:
            
            webbrowser.open("www.goolge.com")
            
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.bing.com/search?q={query}")
            speak("As your wish sir")


        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
            

        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takeCommand()
            if "yes" in ch:
                
                os.system("shutdown /s /t 1")
            else:
                speak("ok sir")
        elif "play music" in query:
            speak("tell me the song name!")
            p = takeCommand()
            webbrowser.open(f"https://soundcloud.com/search?q={p}")
            
            
        elif "play" in query:
            query = query.replace("play", "")
            speak("Ok sir opening your desired song!")
            webbrowser.open(f"https://soundcloud.com/search?q={query}")    
            
            
        elif "give me your introduction" in query:
            speak("Wait, i am introducing myself. My name is Jarvis, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, opening youtube, searching on web and many more")
        
        
        elif "who am i" in query:
            speak("You are pro coder (harshit)")
            
            
        elif 'hello' in query:
            speak("O hello sir")