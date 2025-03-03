import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kit
import openai
from config import apikey



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"vishal: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speak(response["choices"][0]["text"])
    print(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


strTime=datetime.datetime.now().strftime("%H:%M:%S")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning..Sir..!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening..Sir..!")
    speak(f"it's {strTime}")
    # print(strTime)
    speak("tell me how can i help you..!")
def takecommand():
    # It takes microphone input from the user and returns strings output.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"You said:{query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query.lower()


if __name__=="__main__":
    wishMe()
    for i in range(0,10):
        query=takecommand().lower()
        # todo: Add more websites and applications hare in list.
        apps=[["notepad","V:\\Desktop\\Python\\music\\notepad.txt"],["command prompt","C:\\Users\\Vishal KumarGautam\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"],["vs code","C:\\Users\\Vishal KumarGautam\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"],["files","C:\\Users\\Vishal KumarGautam"],["browser","C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"]]
        sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"],["instagram","https://www.instagram.com"],["geeksforgeeks",""]]
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                opath=app[1]
                speak(f"opening {app[0]} sir..")
                if "open browser"in query.lower():
                    speak("sir! what should i search on browser")
                    search=takecommand()
                    webbrowser.open(search)
                    exit()
                os.startfile(app[1])
                exit()
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak(f"opening {site[0]} sir..")
                webbrowser.open(site[1])
                exit()
        if "play song" in query.lower():
            music_dir="V:\\Music"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            exit()
        elif "the time" in query.lower():
            speak(f"Sir.. the time is {strTime}")
        # Logic for executing task based on query
        elif "according to wikipedia"in query.lower():
            speak('searching wikipedia..') 
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=3)
            speak("according to wikipedia..")
            print(results)
            speak(results)  
        elif "ok Jarvis exit "in query.lower():
            speak("ok sir..")
            exit()
        elif "Using webbrowser" in query.lower():
            speak("searching on webbrowser sir..")
            webbrowser.open(query)
        elif "listen Jarvis" in query.lower():
            print("Listening")
            chat(query)
        elif "Jarvis"in query.lower():
            ai(prompt=query)
        else:
            print("Listening2")
            chat(query)
            


                 
