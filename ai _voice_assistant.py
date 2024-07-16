import datetime
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
from bardapi import Bard
import random
from bardapi import BardCookies
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import keyboard
import pyaudio



def CookieScrapper():
    webbrowser.open("https://bard.google.com/chat")
    sleep(7)
    pyautogui.click(x=1246, y=58)
    sleep(5)
    pyautogui.click(x=1071, y=212)
    sleep(5)
    pyautogui.click(x=1019, y=99)
    sleep(1)
    keyboard.press_and_release('ctrl + w')

    data = pyperclip.paste()
    try:
        json_data = json.loads(data)
        pass

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = next((item for item in json_data if item["name"] == SID), None)
    TSValue = next((item for item in json_data if item["name"] == TS), None)
    CCValue = next((item for item in json_data if item["name"] == CC), None)

    if SIDValue is not None:
        SIDValue = SIDValue["value"]
    else:
        print(f"{SIDValue} not found in the JSON data.")

    if TSValue is not None:
        TSValue = TSValue["value"]
    else:
        print(f"{TSValue} not found in the JSON data.")

    if CCValue is not None:
        CCValue = CCValue["value"]
    else:
        print(f"{CCValue} not found in the JSON data.")

    cookie_dict = {
        "__Secure-1PSID": SIDValue,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }

    return cookie_dict
cookie_dict =CookieScrapper()
bard = BardCookies(cookie_dict=cookie_dict)
def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def username():
    speak("what should i call you ?")
    uname=takeCommand()
    speak("Welcome   " + uname)
    speak("How can i help you?")
    return uname
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning ")
    elif hour>=12 and hour<18:
        speak("Good afternoon ")
    else:
        speak("Good evening ")
    speak("I am your virtual assistant Jarvis.")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        audio=r.listen(source,phrase_time_limit=10)
        try:
            print("Recognizing......")
            query=r.recognize_google(audio, language='en-in')

            print(f"User said:{query}\n")
        except Exception as e:
            speak("Unable to recognize your voice......")
            return ""
        return query

if __name__=='__main__':
    wishMe()
    name=username()

    while True:
        order=takeCommand().lower()

        if 'how are you' in order or 'how r u' in order:
            speak("I am fine, Thank you.")
            speak("how are you, mam?")

        elif 'fine' in order or 'good' in order:
            speak("It's good to know you are fine.")

        elif 'who am i' in order or 'who i am' in order:
            speak('if you can talk then surely you are an human.')

        elif 'who are you' in order or 'hu r u' in order:
            speak("I am your virtual assistant jarvis.")

        elif 'bye-bye' in order:
            speak(f"Thank you {name}, i am glad to talk with you")
            break

        elif 'open notepad' in order:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)


        elif 'open google' in order:
            speak("opening google...")
            webbrowser.open("google.com")

        elif 'open youtube' in order:
            speak("Opening youtube....")
            webbrowser.open("youtube.com")

        elif 'open amazon' in order:
            speak("Opening amazon....")
            webbrowser.open("amazon.com")

        elif 'play song' in order or 'play music' in order:
            mpath="https://open.spotify.com/"
            songs=os.listdir(mpath)
            rd=random.choice(songs)
            os.startfile(os.mpath.join(mpath,rd))

        elif 'who built you' in order:
            speak("I am thankful to my developer")
            speak(" Miss sonalin jena ")

        elif 'what is the time' in order or 'current time' in order:
            time=datetime.datetime.now().strftime("%H:%M")
            speak(time)

        elif 'what is the date' in order or 'current date' in order:
            date=datetime.date.today()
            speak(date)

        elif 'where is' in order:
            order=order.replace("where is","")
            location=order
            speak("Locating....")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "")

        elif 'tic-tac-toe' in order:
            speak('enjoy')
            webbrowser.open("https://playtictactoe.org/")
            sleep(15)
        # elif 'write a note' in order:
        #     speak("what should i write?")
        #     note=takeCommand()
        #     file=open('jarvis.txt','w')
        #     speak("should I include date and time as well?")
        #     sn=takeCommand()
        #     if 'yes' in sn or 'sure' in sn or 'yeah' in sn:
        #         strTime=datetime.datetime.now().strftime("%H:%M:%S")
        #         file.write(strTime)
        #         file.write(note)
        #     else:
        #         file.write(note)

        # elif 'display note' in order:
        #     speak("showing note")
        #     file=open('jarvis.txt','r')
        #     print(file.read())
        #     nt=file.read()
        #     speak(nt)


        elif 'jarvis search' in order:
            while True:
                speak("ask me anything")
                Question = takeCommand().lower()
                if 'stop' in Question:
                    speak("Ending Search engine session")
                    break

                RealQuestion = str(Question)
                results = bard.get_answer(RealQuestion)['content']
                current_datetime = datetime.datetime.now()
                formatted_time = current_datetime.strftime("%H%M%S")
                filenamedate = str(formatted_time) + str(".txt")
                filenamedate = "C:\\Users\\ASUS\\Desktop\\friday.py\\DataBase\\" + filenamedate
                speak(split_and_save_paragraphs(results, filename=filenamedate))

        elif 'search image' in order:
            while True:
                speak("Enter image absolute url ")
                imagename = str(input("Enter The Image Name : "))
                if 'stop' in imagename:
                    speak("Ending Search image session")
                    break
                image = open(imagename, 'rb').read()
                bard = BardCookies(cookie_dict=cookie_dict)
                results = bard.ask_about_image('what is in the image?', image=image)['content']
                current_datetime = datetime.datetime.now()
                formatted_time = current_datetime.strftime("%H%M%S")
                filenamedate = str(formatted_time) + str(".txt")
                filenamedate = "C:\\Users\\ASUS\\Desktop\\friday.py\\DataBase\\" + filenamedate
                speak(split_and_save_paragraphs(results, filename=filenamedate))