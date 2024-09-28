import pyttsx3
from datetime import datetime
import wikipedia
import webbrowser
import os
import re
from random import randint
import smtplib
import speech_recognition as sr
from urllib.request import urlopen

ass = pyttsx3.init()

def is_net():
    try:
        urlopen("https://google.com", timeout=1)
        return True
    except:
        return False

def speak(audio):
    vs = ass.getProperty('voices')
    ass.setProperty("voice", vs[1].id)
    ass.setProperty("rate", 150)
    ass.say(audio)
    ass.runAndWait()

def greet():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        wish = "Good morning sasmita! My self Alexa. I am your assistant, how can I help you?"
    elif 12 <= hour < 17:
        wish = "Good Afternoon sasmita! My self Alexa. I am your assistant, how can I help you?"
    else:
        wish = "Good Evening dear sasmita! My self Alexa. I am your assistant, how can I help you?"
    print(wish)
    speak(wish)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speak("listening")
        r.energy_threshold = 4500
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..")
            cmd = r.recognize_google(audio)
            print(cmd)
        except Exception as e:
            print("Sorry I could not understand. Please repeat again.")
            speak("Sorry I could not understand. Please repeat again.")
            cmd = "-1"
    return cmd

greet()
if not is_net():
    print("sasmita As You are not connected to the internet, so I cant recognize your voice")
    speak("sasmita As You are not connected to the internet, so I cant recognize your voice")

while True:
    if is_net():
        query = takecommand().lower()
    else:
        query = input("sasmita Please Enter your text please: ").lower()

    if "wikipedia" in query:
        if is_net():
            result = wikipedia.summary(query, sentences=2)
            print("Searching Please Wait ...")
            speak("Searching Please Wait ...")
            query = query.replace("wikipedia", "")
            speak("According to wikipedia ")
            print(result)
            speak(result)
        else:
            print("sasmita Can't connect to the internet at that moment")
            speak("sasmita Can't connect to the internet at that moment")
            print("Please check your connection then try again")
            speak("Please check your connection then try again")
    elif "open youtube" in query:
        if is_net():
            print("Opening Youtube Please Wait ...")
            speak("Opening Youtube Please Wait ...")
            webbrowser.open("youtube.com")
        else:
            print("sasmita Can't connect to the internet at that moment")
            speak("sasmita Can't connect to the internet at that moment")
            print("Please check your connection then try again")
            speak("Please check your connection then try again")
    elif "open google" in query:
        if is_net():
            print("Opening Google Please Wait ...")
            speak("Opening Google Please Wait ...")
            webbrowser.open("google.com")
        else:
            print("sasmita Can't connect to the internet at that moment")
            speak("sasmita Can't connect to the internet at that moment")
            print("Please check your connection then try again")
            speak("Please check your connection then try again")
    elif "open facebook" in query:
        if is_net():
            print("Opening Facebook Please Wait ...")
            speak("Opening Facebook Please Wait ...")
            webbrowser.open("facebook.com")
        else:
            print("sasmita Can't connect to the internet at that moment")
            speak("sasmita Can't connect to the internet at that moment")
            print("Please check your connection then try again")
            speak("Please check your connection then try again")
    elif "open gmail" in query:
        if is_net():
            print("Opening Gmail Please Wait ...")
            speak("Opening Gmail Please Wait ...")
            webbrowser.open("gmail.com")
        else:
            print("sasmita Can't connect to the internet at that moment")
            speak("sasmita Can't connect to the internet at that moment")
            print("Please check your connection then try again")
            speak("Please check your connection then try again")
    elif "play music" in query or "play song" in query or "play me a music" in query or "play a song" in query:
        print("playing music for you")
        music = "E://music"
        pl = os.listdir(music)
        r = randint(0, 10)
        k = pl[r]
        def countdown(num):
            print("count down started........")
            speak("count down started........")
            while num > 0:
                yield num
                num = num - 1
        v = countdown(3)
        for i in v:
            print(i)
            speak(i)
        speak("let the music begin")
        print("playing {} for you".format(k))
        speak("playing {} for you".format(k))
        os.startfile(os.path.join(music, pl[r]))
    elif "play video" in query or "play video song" in query or "play me a video" in query or "play a video" in query:
        print("playing video for you")
        music = "E://music"
        pl = os.listdir(music)
        r = randint(0, 10)
        k = pl[r]
        print("playing {} for you".format(k))
        speak("playing {} for you".format(k))
        os.startfile(os.path.join(music, pl[r]))
    elif "date and time" in query or "the date and time" in query or "the time and date" in query or "is time and date" in query:
        curr = datetime.now()
        strDate = curr.strftime("%x")
        strTime = curr.strftime("%X")
        print("sasmita, The Date is \n", strDate)
        speak("sasmita, The Date is "+strDate)
        print("sasmita, The time is, \n", strTime)
        speak("sasmita, The time is, "+strTime)
    elif "is time" in query or "the time" in query:
        curr = datetime.now()
        strTime = curr.strftime("%X")
        print("sasmita, The time is, \n", strTime)
        speak("sasmita, The time is, "+strTime)
    elif "is date" in query or "the date" in query:
        curr = datetime.now()
        strDate = curr.strftime("%x")
        print("sasmita, The Date is \n", strDate)
        speak("sasmita, The Date is "+strDate)
    elif "is day" in query or "the day" in query:
        curr = datetime.now()
        strday = curr.strftime("%A")
        print("sasmita, The Day is \n", strday)
        speak("sasmita, The Day is "+strday)
    elif "open notepad" in query:
        print("Opening notepad ...")
        speak("Opening notepad ...")
        os.system("notepad")
    elif "open microsoft word" in query or "m s word" in query or "ms word" in query:
        print("Opening Microsoft word...")
        speak("Opening microsoft word...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word")
    elif "open microsoft excel" in query or "m s excel" in query or "ms excel" in query:
        print("Opening Microsoft excel...")
        speak("Opening microsoft excel...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel")
    elif "open microsoft powerpoint" in query or "m s powerpoint" in query or "ms powerpoint" in query:
        print("Opening Microsoft powerpoint...")
        speak("Opening microsoft powerpoint...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint")
    elif "open bigdata ppt" in query or "bigdata ppt" in query:
        print("Opening bigdata ppt...")
        speak("Opening bigdata ppt...")
        computernetwork = "E:\\computernetwork"
        p1 = os.listdir(computernetwork)
        os.startfile(os.path.join(computernetwork, p1[1]))
    elif "introduce yourself" in query or "who are you" in query or "your introduction" in query or "about you" in query:
        print("sasmita My self Alexa")
        speak("sasmita My self Alexa")
        print("I am your assistant and I am here to help you")
        speak("I am your assistant and I am here to help you")
        print("what you have to do is just ask")
        speak("what you have to do is just ask")
    elif "i love you" in query or "love u" in query or "love" in query:
        a = "it is 7th sense that destroy all the sense"
        speak(a)
        print(a)
    elif 'joke' in query:
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif "don't listen" in query or "stop listening" in query:
        speak("For how much time do you want to stop Aisha from listening to commands?")
        a = int(takecommand())
        time.sleep(a)

        print(a)
    elif "write a note" in query:
        speak("What should i write, mam")
        note = takecommand()
        file = open('aisha.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = takecommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.now().strftime("%H:%M:%S")
            strDate = datetime.now().strftime("%x")
            file.write(strTime)
            file.write(" ")
            file.write(strDate)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
    elif "show note" in query:
        speak("Showing Notes")
        file = open("aisha.txt", "r")
        print(file.read())
        speak(file.read(6))
    elif "open" in query:
        reg_ex = re.search('open (.+)', query)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak('the website you requested has been opened for you sir')
        else:
            pass
    elif "who made you" in query:
        speak("i have been created by Sasmita and she is my master or creator")
    elif "calculate" in query:
        speak("enter first number")
        a = input("enter first number: ")
        speak("enter second number")
        b = input("enter second no: ")
        min_val = a if a < b else b
        print("the minimum value is: {}".format(min_val))
        speak("the minimum value is: ")
        speak(min_val)
    elif "expression" in query:
        speak("enter any expression")
        a = input("enter any expression: ")
        result = eval(a)
        print("the result is", result)
        speak("The result is")
        speak(result)
    elif 'search' in query or 'play' in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)
    elif "how are you" in query:
        print("I am doing well, thanks for Asking. How are you?")
        speak("I am doing well, thanks for Asking. How are you?")
    elif "fine" in query or "good" in query:
        print("It's good to know you are fine.")
        speak("It's good to know you are fine.")
    elif query == "-1":
        print("Sorry I could not understand Please repeat again")
        speak("Sorry I could not understand Please repeat again")
    elif "What is your name" in query:
        print("My name is Alexa.")
        speak("My name is Alexa.")
        print("And I am your assistant.")
        speak("And I am your assistant.")
    elif "send mail" in query or "send a mail" in query or "send gmail" in query:
        if is_net():
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(my_gmail, "sasmitaparida@gmail.com")
            print("To whom?")
            speak("To whom?")
            receiver = takecommand()
            mail.sendmail(my_gmail, "babubai39894@gmail.com", "hey how are you")
        else:
            print("sasmita Can't connect to the internet at that moment")
            speak("sasmita Can't connect to the internet at that moment")
            print("Please check your connection then try again")
            speak("Please check your connection then try again")
    elif "thanks" in query or "thank you" in query:
        print("Your Welcome sasmita, I am just doing my job")
    elif "repeat" in query or "revise" in query:
        if is_net():
            text = takecommand().lower()
        else:
            text = input("Please Enter your text please: ").lower()
        print(text)
        speak(text)
    elif "exit" in query or "go" in query or "leave" in query or "shut up" in query or "get lost" in query:
        print("ok sasmita")
        speak("ok sasmita")
        print("bye ! bye !")
        speak("bye ! bye !")
        print("i will happy to help u again Call me Again")
        speak("i will happy to help u again Call me Again")
        exit()
    else:
        try:
            if is_net():
                results = wikipedia.summary(query, sentences=3)
                print("Here are something matching with your text")
                speak("According to wikipedia ")
                print(results)
                speak(results)
            else:
                print("satyajit Can't connect to the internet at that moment")
                speak("satyajit Can't connect to the internet at that moment")
                print("Please check your connection then try again")
                speak("Please check your connection then try again")
        except Exception as e:
            print("Sorry! I have a lot to learn")
            speak("Sorry! I have a lot to learn")
    print("What else can I do for you.")
    speak("What else can I do for you")
