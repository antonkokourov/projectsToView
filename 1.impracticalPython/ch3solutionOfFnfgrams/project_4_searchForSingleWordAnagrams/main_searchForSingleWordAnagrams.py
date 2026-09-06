# -*- coding: utf-8 -*-
"""
    Project 4: search for one-word anagrams -- поиск однословных анаграмм

    1. Загрузка электронного словаря слов
    2. Запрос у пользователя слова для поиска анаграмм
    3. Проход по всему загруженному списку
        - сортировка введенного слова и слова из списка
        - сравнение по схожести в количествах букв
        - при совпадении добавляем слова со словаря в список анаграмм
    4. Выводим на экран результат (список анаграмм)

"""
import time
from PrintColors import *
from OpenText import *

fileDictionaryWords = r'file/2of4brif.txt'


def inputWord():
    """Ввод слова, выводит фраза которая введена(inpWord) и список введенных букв (word)"""
    while True:
        inpWord = input("Введите слово для поиска его анаграмм: ").lower()
        word = sorted([i for i in inpWord if i.isalpha()])
        if inpWord == "":
            print("!Вы ничего не ввели")
        else:
            return word, inpWord


def main(listWords):
    """Основной процесс программы"""

    # обработка введенного слова, остаются только буквы
    word, inpWord = inputWord()
    timeStart = time.time()
    sizeWord = len(word)

    anagrams = []

    for wordDictionary in listWords:
        if inpWord == wordDictionary:
            continue
        if len(wordDictionary) == sizeWord and sorted(list(wordDictionary.lower())) == word:
            anagrams.append(wordDictionary)



    if anagrams:
        print("Используемое имя: ", inpWord)
        print("Анаграммы: ", ' ,'.join(anagrams))
    else:
        print("Нужен больше словарь или введите другое имя")



    timeEnd = time.time()
    print(f"{timeEnd - timeStart:.4f} sek")

if __name__ == "__main__":
    # timeStart = time.time()
    dictionaryWords = OpenText(fileDictionaryWords)
    main(dictionaryWords)
    # timeEnd = time.time()
    # print(f"{timeEnd - timeStart:.4f} sek")
    print(f"\n{PrintColors.Red}До встречи!!{PrintColors.Reset}")

