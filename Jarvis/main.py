import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import webbrowser
import sys
from playsound import playsound
from requests import get
import pygame
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
pygame.mixer.init()

listener=sr.Recognizer()
engine=pyttsx3.init()
# voices=engine.getProperty('voices')       ----->To change the voice
# engine.setProperty('voice',voices[1].id) 
engine.say('jarvis at your service sir')   
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            
            
            voice=listener.listen(source, timeout=100)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                command=command.replace('jarvis','')
                print(command)
    except:
        pass
    return command
def run_jarvis():
    # pygame.mixer.music.load(r'C:\Users\\admin\\Desktop\\Jarvis\\Iron-Man-2-BGM .mp3')
    # pygame.mixer.music.play(-10)
    command = take_command()
    print(command)
    if 'play' in command:
        if 'in youtube' in command:
            song = command.replace('play','')
            talk('playing '+ song)
            pywhatkit.playonyt(song)
        elif 'jack' in command:
            playsound(r"C:\\Users\\admin\\Desktop\\Jarvis\\jack.wav")
            
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('sir current time is '+time)
    elif 'record' in command:
        # name = command.replace('record','')
        freq = 44100
        talk('what is the name of the audio sir')   
        name=take_command()        
        # talk('what is the time duration sir')   --->This is to try to enter the number  by speech recognition but it failed because time comes in the form of string
        # if 'minutes' in time:
        #     time1=time.replace('minutes','')
        #     duration=time1*60
        # else :
        #     duration=time.replace('seconds','')
        duration=5
        recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
        sd.wait()
        write(name+".wav", freq, recording)
    elif 'who is' in command:
        person=command.replace('who is','')
        info = wikipedia.summary(person, sentences = 2)
        print(info)
        talk(info)
    elif 'shut yourself' in command:
        print('shutting down with your permission sir')
        talk('shutting down with your permission sir')
        sys.exit()
    elif 'open notepad' in command:
        talk('as per your orders, there you go sir')
        os.startfile('C:\\Windows\\system32\\notepad.exe')
    elif 'open command prompt' in command:
        talk('as per your orders, there you go sir')
        os.system("start cmd")
    elif 'what is my ip address' in command:
        ip = get("https://api.ipify.org").text
        print(ip)
        talk(f"your ip address is {ip}")
    elif 'open youtube' in command:
        webbrowser.open("www.youtube.com")
    elif 'open whatsapp' in command:
        webbrowser.open("https://web.whatsapp.com/")
    elif 'google' in command:
        object=command.replace("google","")
        pywhatkit.search(object)
    else :
        apology='sorry sir i am unable to understad you, could you please tell again'
        print(apology)
        talk(apology)
while True:
       run_jarvis()
     
