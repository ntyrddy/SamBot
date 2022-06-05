import pyttsx3
import speech_recognition as sr
from translate import Translator

LANGUAGES = {"french":'fr-FR',
                "spanish":'es-ES',
                 "korean": 'ko-KR',
                 "japanese": 'ja-JP',
                 "russian":'ru-RU',
                 "italian":'it-IT',
                 "hindi":'hi-IN'}

listener = sr.Recognizer()
engine = pyttsx3.init()
engine2 = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')


engine.say("Hello. I am Sam, your Python translator.")
engine.say("Which language would you like me to translate")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Please speak now...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice).lower()

except Exception as e: print(e)
print(command)

print(LANGUAGES[command])
translator = Translator(from_lang=LANGUAGES[command][0:2], to_lang = 'en')
go_on = True

while go_on:
    try:
        with sr.Microphone() as source:
            print("Please speak now...")
            voice = listener.listen(source)
            sentence = listener.recognize_google(voice, language=LANGUAGES[command])

    except Exception as e: print(e)
    translation = translator.translate(sentence)
    print(translation)
    engine.say(translation)
    engine.runAndWait()

    translation = ''
    sentence = ''

    print("If you would like to continue, say 'continue'. To end say 'end'")
    engine.say("If you would like to continue, say 'continue'.... To end say 'end'")
    engine.runAndWait()

    try:
        with sr.Microphone() as source:
            print("Please speak now...")
            voice = listener.listen(source)
            sentence = listener.recognize_google(voice)

            if sentence.lower() == 'end':
                go_on = False
            else:
                go_on = True

    except Exception as e:
        print(e)