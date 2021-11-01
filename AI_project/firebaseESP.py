from mypackage.speak_hear import *
import requests as re

url = "https://esp321-b1049-default-rtdb.firebaseio.com/.json"
json = {"first": 0, "second": 0}


def control_Led():
    while True:

        you = hear()
        if you is None:
            speak("i can't hear, please say again")
        elif "turn on" in you:
            if "first" in you:
                json["first"] = 1
                s = re.put(url=url, json=json)
                speak("the first led is on")
            if "second" in you:
                json["second"] = 1
                s = re.put(url=url, json=json)
                speak("the second led is on")

        elif "turn off" in you:
            if "first" in you:
                json["first"] = 0
                s = re.put(url=url, json=json)
                speak("the first led is off")
            if "second" in you:
                json["second"] = 0
                s = re.put(url=url, json=json)
                speak("the second led is off")
            if "both" in you:
                json["first"] = 0
                s = re.put(url=url, json=json)
                json["second"] = 0
                s = re.put(url=url, json=json)
        elif "goodbye" in you:
            speak("goodbye boss")
            exit()
        elif "previous" in you:
            speak("what else can i help you?")
            break
        elif "blink" in you:
            json["first"] = 2
            s = re.put(url=url, json=json)
            speak("leds are blink")
