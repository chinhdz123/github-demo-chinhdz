import pyttsx3
import speech_recognition as sr


def hear():
    print("Michael:Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Boss: ", end='')
        audio = r.listen(source, phrase_time_limit=10)  # nghe
        try:
            text = r.recognize_google(audio)  # dịch ra
            print(text)
            return str(text).lower()
        except:
            return None


def speak(text):
    print("Michael: " + text)
    engine = pyttsx3.init()
    voice = engine.getProperty("voices")
    engine.setProperty("voice", voice[1].id)
    engine.say(text)
    engine.runAndWait()
