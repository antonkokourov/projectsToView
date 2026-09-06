# -*- coding: utf-8 -*-
"""
    Project 7: searchForVoldemortAndBritish -- поиск Волдеморта, или британская грубая сила

    1. Загрузка электронного словаря слов
    2. Запрос у пользователя текста для поиска
    3. Запрос у пользователя на какую букву будет показаны слова
    4. Фильтрация слов:
        - подготовка списка возможных сочетаний букв
        - формирования шаблона фильтрации для гласных и согласных
        - фильтрация с помощью шаблона сочетания гласных и согласных букв
        - формирование файла диаграмм возможных сочетаний двух букв
        - фильтрация списка возможных слов через файл диаграмм
        - показ списка возможных слов на указанную букву
        - при отсутствии нужных вариантов запрос другой буквы или ввод другого слова для поиска
        - при выборе другой буквы и того же слова (показывает тот же список, но на другую букву)
        - при выборе ввода другого слова, процесс повторяется, но без формирования шаблонов и файлов

"""

import os
import sys
import subprocess
from itertools import permutations

from VowelConsonants import *
from Diagrams import *
from OpenText import *
from PrintColors import *

def wordQuery():
    """Запрос слова для преобразования"""
    return input("Введите слова для преобразования в возможные имена: ")

def letterRequest(words):
    """Запрос начальной буквы"""
    letters = []
    for word in words:
        letters.append(word[0])
    lett = ', '.join(sorted(list(set(letters))))
    while True:
        inp = input(f"Введите начальную букву имен из {lett}: ")
        if inp in letters:
            return inp

def fileCheck():
    """Проверка существует ли файл по сочетанию пар букв. Если нет, то создает файл"""
    if os.path.exists('letter_combination.json'):
        print(f"{PrintColors.Yellow}", end='')
        print("✅ Файл фильтрации диграмм существует", end='')
        print(f"{PrintColors.Reset}")
    else:
        print(f"{PrintColors.Yellow}", end='')
        print("❌ Файл фильтрации диграмм не найден")
        Diagrams()
        print(f"{PrintColors.Reset}", end='')

def finishWords(words, letter):
    """Показывает список получившихся слов"""
    if len(words) == 0:
        print("Результат отсутствует")
        return 0

    else:
        fWords = [word for word in words if word[0] == letter]
        i = 1
        for word in fWords:
            print(f"{i}. {word}")
            i += 1
        return i-1, sorted(fWords)

def finishProg(word):
    """Вывод результата"""
    print("Вы выбрали: ")
    print(f"{PrintColors.Red}{word}{PrintColors.Reset}")
    print(f"\n{PrintColors.Blue}До встречи!!{PrintColors.Reset}")
    sys.exit()


def menu(size, word, wordsDA, letter, fWord):
    """Вывод меню запросов"""
    while True:
        nameReturn = 0
        print("Если нашли подходящее имя введите 'yes'")
        print("Если не нашли подходящее имя и хотите поменять начальную букву имени введите 'no'")
        print("Если нужно изменить слово для преобразования введите 'new'")
        print("Для выхода введите 'exit'")
        choice = input("Ваш выбор: ")

        if choice == 'yes':
            name = input("Отлично, введите номер подходящего имени: ")

            if name.isdigit() and 0 < int(name) <= size :
                name = int(name) - 1
                finishProg(fWord[name])
            else:
                print("Такого номера не найдено!")
                print("Просьба выбрать число: ")
                size, fWord = finishWords(wordsDA, letter)
                menu(size, word, wordsDA, letter, fWord)
        elif choice == 'no':
            letter = letterRequest(wordsDA)
            size, fWord = finishWords(wordsDA, letter)
            menu(size, word, wordsDA, letter, fWord)
        elif choice == 'new':
            main()
        elif choice == 'exit':
            print(f"\n{PrintColors.Blue}До встречи!!{PrintColors.Reset}")
            sys.exit()
        else:
            print("Нет такого выбора!")


def main():
    """Основной процесс программы"""
    word = wordQuery() # запрос ввода слова

    perms = [''.join(i) for i in permutations(word)] # показать сколько слов было изначально
    print(f"{PrintColors.Green}Первый этап (без фильтрации): {len(perms)} слов!{PrintColors.Reset}")

    wordsCV, listCV = cv_map(word, perms) # список слов после фильтрации гласные-согласные, конструкции возможных сочетаний гласные-согласные
    print(f"{PrintColors.Green}Второй этап (после CV): {len(wordsCV)} слов!{PrintColors.Reset}")
    fileCheck() # проверка существование файла, создание

    wordsDA = filtrationDuAlpha(wordsCV)
    print(f"{PrintColors.Green}Третий этап (после DA): {len(wordsDA)} слов!{PrintColors.Reset}")
    wordsDA = sorted(wordsDA)
    letter = letterRequest(wordsDA)
    size, fWord = finishWords(wordsDA, letter)
    menu(size, word, wordsDA, letter, fWord)





# запуск программы
if __name__ == "__main__":
    main()
    print(f"\n{PrintColors.Blue}До встречи!!{PrintColors.Reset}")

