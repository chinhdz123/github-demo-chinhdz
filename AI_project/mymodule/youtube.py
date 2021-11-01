from youtube_search import YoutubeSearch
import webbrowser
from mypackage.speak_hear import *
import time


def SearCh_YouTube(text):
    # Sử dụng vòng while tìm kiếm đến khi nào có kết quả trả về
    while True:
        # Biến resuilt lưu lại kết quả trả về dưới dạng dữ liệu Dictionary
        result = YoutubeSearch(text, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    time.sleep(1)
    speak("the content you looking for was open, what else do you want?")


def youtube():
    speak("What type of input do you want to choose?")
    while True:
        boss = hear()
        if boss is None:
            speak("i can't hear you, please say again, boss")
        elif "hand" in boss:
            search_w1 = input()
            SearCh_YouTube(search_w1)
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        elif "speak" in boss:
            speak("what video do you looking for?")
            search_w2 = hear()
            SearCh_YouTube(search_w2)
            speak("enter any press to continue")
            input()
        elif "previous" in boss:
            speak("Do you need any other help?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        else:
            speak("i can't hear you, please say again, boss")
