import pyttsx3
from pyttsx3 import engine 


def text_to_speech_init():
    global engine 
    engine = pyttsx3.init()
    VIETNAMESE_VOICE_ID = 'aav/vi'
    engine.setProperty('voice',VIETNAMESE_VOICE_ID, )


def AI_say(text):
    engine.say(text)
    engine.runAndWait()

