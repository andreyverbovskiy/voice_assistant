import random
import playsound
from gtts import gTTS
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak: ")
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio)
        print("I said: ", speech)
        return speech
    except sr.UnknownValueError:
        return 'ERROR'
    except sr.RequestError:
        return 'ERROR'

def say(text):
    voice = gTTS(text, lang = "ru")
    unique_filename = "audio_" + str(random.randint(0,100000)) + ".mp3"
    voice.save(unique_filename)

    playsound.playsound(unique_filename)
    print("Assistant:", text)

def handle_message(message):
    if "Hi" in message:
        say("Hello baby")
    elif "How is life" in message:
        say("I am fine")
    elif "Who is my mother" in message:
        say("Tatiana Verbovskaya")
    elif "I love you" in message:
        say("I love you even more")
    elif "bye" in message:
        finish()
    else:
        say("I do not understand, repeat again")

def finish():
    say("bye baby")
    exit()

print("It works")
while True:
    command = listen()
    handle_message(command)
