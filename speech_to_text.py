import speech_recognition as sr

#listening to audio from mic
r = sr.Recognizer() #syntax
with sr.Microphone() as source:
    print("start")
    audio = r.listen(source) #"listens" from the mic audio aka captures the audio
                             #and stores the audio in the variable audio
                             
#expection handling a method to handle errors or exceptional situations at may occur during program execution, ensuring the program does not terminate abnomally. 
try: 
    text = r.recognize_google(audio, language = 'en-US')
    print(text)
except sr.UnknownValueError: #The first exception handling for cases where speech recognition fails. 
    print("Recognition failed")
except sr.RequestError as e: #network issue or internet issues or API issues 
    print(f"Request failed: {e}")
