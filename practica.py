import speech_recognition
import os
import webbrowser

recognition = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

def get_audio():
    recognition = speech_recognition.Recognizer()
    mic = speech_recognition.Microphone()
    with mic as audio_file:
        audio = recognition.listen(audio_file)
        text = recognition.recognize_google(audio, language='ru-RU')
        return text.lower()

while True:
    print("Здравствуйте, повелитель")
    print("Что желаете сделать?")
    text = get_audio()
    print("Вы сказали: " + text)
    if (text.count("открой диспетчер задач") > 0) or (text.count("включи диспетчер задач") > 0) or (text.count("запусти диспетчер задач") > 0) or (text.count("открыть диспетчер задач") > 0) or (text.count("включить диспетчер задач") > 0) or (text.count("запустить диспетчер задач") > 0):
        print("Открываю диспетчер задач")
        os.system("taskmgr")
        break
    elif (text.count("открой панель управления") > 0) or (text.count("включи панель управления") > 0) or (text.count("запусти панель управления") > 0) or (text.count("открыть панель управления") > 0) or (text.count("включить панель управления") > 0) or (text.count("запустить панель управления") > 0):
        print("Открываю панель управления")
        os.system("control")
        break
    elif (text.count("открой клавиатуру") > 0) or (text.count("открыть клавиатуру") > 0) or (text.count("открой экранную клавиатуру") > 0) or (text.count("открыть экранную клавиатуру") > 0) or (text.count("включи клавиатуру") > 0) or (text.count("включить клавиатуру") > 0) or (text.count("включи экранную клавиатуру") > 0) or (text.count("включить экранную клавиатуру") > 0) or (text.count("запусти экранную клавиатуру") > 0) or (text.count("запустить экранную клавиатуру") > 0) or (text.count("запусти клавиатуру") > 0) or (text.count("запустить клавиатуру") > 0):
        print("Открываю экранную клавиатуру")
        os.system("osk")
        break
    elif text.count("искать в интернете") or text.count("ищи в интернете") or text.count("осуществи поиск в интернете") or text.count("осуществить поиск в интернете") or text.count("найти в интернете") or text.count("найди в интернете") or text.count("выполни поиск в интернете") or text.count("выполнить поиск в интернете") > 0:
        s = text.split()
        while s[0] != "интернете":
            del s[0]
        del s[0]
        s = " ".join(s)
        print("Ищу в интернете: " + s)
        url = 'https://www.google.co.in/search?q='
        search_url = url + s
        webbrowser.open(search_url)
        break
    elif text.count("-") > 0:
        s = text.split()
        if s[0].isdigit() == True:
            if s[2].isdigit() == True:
                k = int(s[0]) - int(s[2])
                print(str(s[0]) + " - " + str(s[2]) + " = " + str(k))
            else:
                print('Второе число не распознано, не удалось посчитать')
        else:
            print('Первое число не распознано, не удалось посчитать')
        break
    elif (text.count("выключи компьютер") > 0) or (text.count("выключить компьютер") > 0) or (text.count("выключай компьютер") > 0) or (text.count("заверши работу компьютера") > 0) or (text.count("завершить работу компьютера") > 0) or (text.count("завершай работу компьютера") > 0):
        os.system("shutdown -p")
        break
    elif (text.count("выключись") > 0) or (text.count("выключайся") > 0) or (text.count("выключить") > 0) or (text.count("выключить голосового ассистента") > 0) or (text.count("выключи голосового ассистента") > 0) or (text.count("выключай голосового ассистента") > 0) or (text.count("завершай работу голосового ассистента") > 0) or (text.count("заверши работу голосового ассистента") > 0) or (text.count("завершить работу голосового ассистента") > 0):
        os.system("taskkill /F /T /IM cmd.exe")
        break
    else:
        print("Команда не распознана")
        break