import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import datetime
import os


r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("[User_speaking]: " + command)
            return command
        except sr.UnknownValueError:
            return None

def respond(text):
    tts = gTTS(text = text, lang = 'en')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")
    
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y")

while True:
    print("Is there anything I can help you with?")
    """intro = "Is there anything I can help you with?"
    file_name2 = 'intro.mp3'
    tts_intro = gTTS(text = intro, lang = 'en')
    tts_intro.save(file_name2)
    playsound(file_name2)
    print("[Ai_speaking]: " + intro)"""
    command = listen()
    if command:
        if "hello" in command:
            respond("[Ai_speaking]: Hello User")
        elif "time" in command:
            respond("[Ai_speaking]: " + get_time())
            print(get_time())
        elif "date" in command:
            respond("[Ai_speaking]: " + get_date())
            print(get_date())
        elif "goodbye" in command:
            respond("[Ai_speaking]: Goodbye")
            break
        elif "weather" in command:
            respond("The weather is sunny today")
    else:
        respond("[Ai_speaking]: I didn't get that. Please try again.")