import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import webbrowser

opts = {
    "alias": ('практика'),
    "tbr": ('прошу', 'пожалуйста', 'умоляю'),
    "cmds": {
        "dispetcher": ('открой диспетчер задач', 'включи диспетчер задач', 'запусти диспетчер задач'),
        "panel": ('открой панель управления', 'включи панель управления', 'запусти панель управления'),
        "poisk": ('поиск в интернете', 'найди в интернете', 'ищи в интернете', 'выполни поиск в интернете', 'осуществи поиск в интрнете', 'сделай поиск в интернете'),
        "vikl": ('выключись', 'прекрати работу', 'выключайся', 'завершай работу', 'заверши работу'),
        "klav": ('открой клавиатуру', 'открой электронную клавиатуру', 'включи клавиатуру', 'включи электронную клавиатуру', 'запусти клавиатуру', 'запусти электронную клавиатуру'),
        "sch": ('считай', 'считать'),
        "comp": ('выключи компьютер', 'выключай компьютер')
    }
}


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'dispetcher':
        os.system("taskmgr")

    elif cmd == 'panel':
        os.system("control")

    elif cmd == 'poisk':
        with sr.Microphone() as source:
            print("Что искать?")
            audio = r.listen(source)
            try:
                voice = r.recognize_google(audio, language="ru-RU").lower()
                print("Ищу в интернете: " + voice)
                url = 'https://www.google.co.in/search?q='
                search_url = url + voice
                webbrowser.open(search_url)
            except:
                print("Не могу найти")

    elif cmd == 'klav':
        os.system("osk")

    elif cmd == 'sch':
        with sr.Microphone() as source:
            print("Что считать?")
            audio = r.listen(source)
            try:
                voice = r.recognize_google(audio, language="ru-RU").lower()
                print("Считаю: " + voice)
                s = voice.split()
                if s[0].isdigit() == True:
                    if s[1] == '-':
                        if s[2].isdigit() == True:
                            print(int(s[0]) - int(s[2]))
                        else: print('второе число не распознано, не удалось посчитать')
                else: print('первое число не распознано, не удалось посчитать')
            except:
                print("Не могу посчитать")
    elif cmd == 'vikl':
        os.system("taskkill /F /T /IM cmd.exe")
    elif cmd == 'comp':
        os.system("shutdown -p")



r = sr.Recognizer()
m = sr.Microphone(device_index=1)

print("Здравствуйте, повелитель")
print("Практика слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)
