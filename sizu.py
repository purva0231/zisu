import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=19 and hour== 0:
        speak("good night!")

    elif hour>=0 and hour<=4:
        speak("good night!")

    elif hour>=4 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<=16:
        speak("good afternoon!")

    else:
        speak("good evening")

    speak("i am sizu. i am programed by purva. please tell me how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-IN")
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)

        speak("say that again please...")
        return "none"
    return query



if  __name__ == "__main__":
    wishMe()

    if 1:
        query = takeCommand().lower()
    #logic for executing tasks based on query
     

        if 'wikipedia' in query:
            speak('searching wikipedia... please wait...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open blogspot' in query:
            webbrowser.open("blogspot.com")

        elif 'open youtube studio.com' in query:
            webbrowser.open("youtubestudio.com")

        elif 'play music' in query:
             webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")
        

        elif 'open visual studio code' in query:
            vsPath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(vsPath)

        elif 'open desktop' in query:
            fePath = "C:\\Users\\purva\\OneDrive\\Desktop"
            os.startfile(fePath)

        
           

