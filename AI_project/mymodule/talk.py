from mypackage.speak_hear import *
import numpy as np


q1 = open("database\\question_ques.txt", mode='r', encoding="utf8")
ques1 = q1.read().split("\n")
a1 = open("database\\answer_ques.txt", mode='r', encoding="utf8")
answ1 = a1.read().split("\n")
q2 = open("database\\question_answ.txt", mode='r', encoding="utf8")
ques2 = q2.read().split("\n")
a2 = open("database\\answer_answ.txt", mode='r', encoding="utf8")
answ2 = a2.read().split("\n")
q3 = open("database\\practice_ques.txt", mode='r', encoding="utf8")
ques3 = q3.read().split("\n")
a3 = open("database\\practice_ans.txt", mode='r', encoding="utf8")
answ3 = a3.read().split("\n")
def talk():
    speak("yes, i would love to talk to you ")
    speak("Do you want to ask or answer?")
    while True:
        boss = hear()
        if boss is None:
            speak("i can't hear you, please say again")
        elif "ask" in boss:
            ask()
        elif "answer" in boss:
            ans()
        elif "practice" in boss:
            practice()
        elif "previous" in boss:
            speak("Do you need any other help?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        else:
            speak("i can't hear you, please say again")


def choose_ans():
    speak("choose one question")
    while True:
        i = int(input())
        if i >= 0 or i <= len(answ2):
            i = i - 1
            break
        else:
            speak(f"I just learn {len(answ2)}, please choose again")
    return i


def ask():
    speak("please talk to me")
    while True:
        boss = hear()
        if boss is None:
            speak("I can't hear you, please say again")
        elif "previous" in boss:
            speak("Do you want to talk to me more?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        else:
            Api = handle_data_ques(boss)
            if Api is None:
                speak("I can't hear you, please say again")
            else:
                speak(Api)


def ans():
    speak("please talk to me")
    while True:
        boss = hear()
        if boss is None:
            speak("I can't hear you, please say again")
        elif "previous" in boss:
            speak("Do you want to talk to me more?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        else:
            Api = handle_data_ans(boss)
            if Api is None:
                speak("I can't hear you, please say again")
            else:
                speak(Api)


def practice():
    i = choose_ans()
    while True:
        question(i)
        while True:
            boss = hear()
            if boss is None:
                speak("I can't hear you, please say again")
            else:
                Apii = handle_data_practice(boss, i)
                if Apii == 1:
                    break
                else:
                    option = input("quit or again")
                    if "quit" in option:
                        break
        speak("Do you want to answer continue or again?")
        a = input()
        if "back" in a or "no" in a:
            speak("Do you want to ask or answer?")
            break
        elif "goodbye" in a:
            speak("goodbye, boss")
            exit()
        elif "again" in a:
            i = i - 1
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        else:
            i = choose_ans()

def handle_data_ques(text):
    # chia câu hỏi người dùng thành các từ riêng biệt
    if text is None:
        return None
    else:
        text1 = text.split(" ")
        # khởi tạo list rỗng để lưu tỉ lệ % giống nhau giữa câu hỏi người dùng với data question đã tạo
        que = []
        # tính toán tỷ lệ phần trăm
        for s in ques1:
            text2 = s.lower().split(" ")
            count = 0
            a = len(text2)
            for i in text1:
                if i in text2:
                    count += 1
            ratio = count * 100 / a
            que.append(ratio)
        return answ1[np.argmax(que)]  # trả về vị trí có tỷ lệ % cao nhất


def handle_data_ans(text):
    # chia câu hỏi người dùng thành các từ riêng biệt
    if text is None:
        return None
    else:
        text1 = text.split(" ")
        # khởi tạo list rỗng để lưu tỉ lệ % giống nhau giữa câu hỏi người dùng với data question đã tạo
        que = []
        # tính toán tỷ lệ phần trăm
        for s in answ2:
            text2 = s.lower().split(" ")
            count = 0
            a = len(text2)
            for i in text1:
                if i in text2:
                    count += 1
            ratio = count * 100 / a
            que.append(ratio)
        return ques2[np.argmax(que)]  # trả về vị trí có tỷ lệ % cao nhất


def handle_data_practice(text, i):
    text1 = text.split(" ")
    text2 = answ3[i].lower().split(" ")
    count = 0
    num = 0
    for s in text2:
        count += 1
        for z in text1:
            if z in s:
                num += num
    ratio = int(num * 100 / count)
    if ratio > 40:
        speak(f"qualified, exactly {ratio} %")
        return 1
    if ratio < 40:
        speak(f"unsatisfactory,exactly {ratio} %, please reply again")
        return 0


def question(i):
    speak(ques3[i])