from gtts import gTTS
from playsound import playsound
"""
#1. English
text = "How can I help you?"
file_name = 'sample.mp3' #Saved as an mp3 file aka Audio file.
tts_english = gTTS(text = text, lang = 'en') #Use gTTS to convert text to speech, english
tts_english.save(file_name)
playsound(file_name) #playsound allows the computer to automatically start the mp3 file.


#2. Korean
text2 = "안녕하세요. 저는 파이썬을 배우고 있습니다"
file_name2 = 'sample2.mp3'
tts_korean = gTTS(text = text2, lang = 'ko')
tts_korean.save(file_name2)
playsound(file_name2)
"""

file_name = 'sample3.mp3'
with open('sample_text3.txt','r') as f:
    text = f.read()
    
tts_english = gTTS(text = text, lang = 'en')
tts_english.save(file_name)
playsound(file_name)