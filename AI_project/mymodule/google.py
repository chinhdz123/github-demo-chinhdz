import webbrowser
from mypackage.speak_hear import *
import time


def Search_google(text):
    url = "https://www.google.com/search?q=" + text
    webbrowser.open(url)
    time.sleep(1)
    speak("Your result has been found,what else do you want?")


def google():
    speak("What type of input do you want to choose? ")
    while True:
        boss = hear()
        if boss is None:
            speak("i can't hear you, please say again, boss")
        elif "hand" in boss:
            search_g1 = input("enter your search: ")
            Search_google(search_g1)
            speak("enter any press to continue")
            input()
        elif "speak" in boss:
            search_g2 = hear()
            Search_google(search_g2)
            speak("enter any press to continue")
            input()
        elif "previous" in boss:
            speak("Do you need any other help?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
