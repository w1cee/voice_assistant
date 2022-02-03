import time
import speech_recognition as sr
import pyttsx3  # you need install PyAudio
import webbrowser
import os
import speedtest  # speedtest-cli
from googlesearch import search


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        say_message("Скажите вашу команду: ")
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: " + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"


def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("Привет друг!")

    elif "как дела" in message:
        say_message("Нормально, ты как?")
        time.sleep(3)

    elif "открой ссылку" in message:
        say_message("Открываю!")
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(url)
        time.sleep(5)

    elif "открой картинку" in message:
        os.startfile(r'H:\Gallery\кот.png')
        time.sleep(5)

    elif "открой мой профиль" in message:
        say_message("Открываю.")
        url = "https://github.com/w1cee/"
        webbrowser.open(url)

    elif "какая скорость интернета" in message:
        s = speedtest.Speedtest()
        download = s.download()
        download = download / 1000000
        print("Download speed: ", round(download), "Mb/s")

        upload = s.upload()
        upload = upload / 1000000
        print("Upload speed: ", round(upload), "Mb/s")

        server_names = []
        s.get_servers(server_names)
        print("Ping: ", s.results.ping, "ms")

        time.sleep(2)
    elif "кто такой" in message:
        say_message("Информация из поисковика: ")
        for result in search(message, num_results=2):
            print(result)

    elif "включи песню" in message:
        url = "https://www.youtube.com/watch?v=c9JNp6kdKqU"
        webbrowser.open(url)
        time.sleep(5)

    elif "открой заметки" in message:
        url = "https://keep.google.com/u/0/"
        webbrowser.open(url)
        time.sleep(5)

    elif "1000 - 7" in message:
        i = 1000
        say_message("Я.... Гуль")
        while i != 6:
            i = i - 7
            print(i)
        webbrowser.open("https://www.youtube.com/watch?v=eXvPgDmMLDk")
        time.sleep(5)

    elif "таблица умножения на 2" in message:
        for i in range(10):
            i += 1
            print(f"2 * {i} = ", 2 * i)

    elif "таблица умножения на три" in message:
        for i in range(10):
            i += 1
            print(f"3 * {i} = ", 3 * i)

    elif "таблица умножения на четыре" in message:
        for i in range(10):
            i += 1
            print(f"4 * {i} = ", 4 * i)

    elif "таблица умножения на пять" in message:
        for i in range(10):
            i += 1
            print(f"5 * {i} = ", 5 * i)

    elif "таблица умножения на шесть" in message:
        for i in range(10):
            i += 1
            print(f"6 * {i} = ", 6 * i)

    elif "таблица умножения на семь" in message:
        for i in range(10):
            i += 1
            print(f"7 * {i} = ", 7 * i)

    elif "таблица умножения на восемь" in message:
        for i in range(10):
            i += 1
            print(f"8 * {i} = ", 8 * i)

    elif "таблица умножения на девять" in message:
        for i in range(10):
            i += 1
            print(f"9 * {i} = ", 9 * i)

    elif "пока" in message:
        say_message("Пока!")
        exit()

    else:
        say_message("Команда не распознана!")


def say_message(message):
    voice = pyttsx3.init()
    voice.say(message)
    print("Голосовой ассистент: " + message)
    voice.runAndWait()


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
