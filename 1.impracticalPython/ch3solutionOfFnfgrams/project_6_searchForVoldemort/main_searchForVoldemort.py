# -*- coding: utf-8 -*-
"""
    Project 5: search for phrase anagrams -- поиск фразовых анаграмм

    1. Загрузка электронного словаря слов
    2. Запрос у пользователя текста для поиска анаграммных фраз
    3. Проход по всему загруженному списку
        - сортировка введенного текста и слова из списка
        - сравнение по схожести в количествах букв
        - при совпадении добавляем слова со словаря в список для выбора пользователю
        - удаление букв из введенного текста входящие в состав выбранного слова
        - повтор цикла с оставшимися буквами из введенной фразы
    4. Выводим на экран результат (список анаграмм)

"""

import sys
import time
from collections import Counter
from PrintColors import *
from OpenText import *

fileDictionaryWords = r'file/2of4brif.txt'

def doInputText():
    """Ввод слова, выводит фраза которая введена(inpWord) и список введенных букв (dictionaryOfLetters)"""
    while True:
        iinputText = input("Введите слово для поиска его анаграмм: ").lower()
        if iinputText == '#':
            sys.exit()
        iiText = sorted([i for i in iinputText if i.isalpha()])

        if iinputText == "":
            print("!Вы ничего не ввели")
        else:
            return iiText, iinputText



listWords = OpenText(fileDictionaryWords)

# обработка введенного текста, остаются только буквы
iText, inputText = doInputText()  # iText - обработанный веденный текст; inputText - введенный текст
lettersInText = Counter(iText)  # lettersInText - словарь с количеством букв от веденного текста
sizeText = len(iText)


def isComparisonOfLetters(text, iWord):
    """Сравнение количества букв подходит ли слово как анаграмма"""
    word = Counter(iWord)
    for letter in word:
        if word[letter] <= text[letter]:
            pass
        else:
            return False

    return True

def deletingLetters(text, iWord):
    """Удаление букв"""
    word = Counter(iWord)

    for letter in word:
        text[letter] -= word[letter]
        if text[letter] == 0:
            text.pop(letter)

    return text


def choice(words):
    """Сообщение пользователю о выборе слова, и возврат выбранного слова"""
    if not words:
        return None
    while True:
        print("Слова которые подходят:", end=" ")
        print(', '.join(words))

        print(PrintColors.Yellow)
        print(f"Выберите одно слово - напечатав его или начните сначала нажав enter (# - exit): {PrintColors.Reset}", end="")


        choiceInput = input().lower().strip()
        if choiceInput == '#':
            print("Выход!")
            sys.exit()
        elif choiceInput == '':
            main()
        else:
            for word in words:
                if word == choiceInput:
                    print("вы выбрали слово:", word)
                    return word



def main():
    """Основной процесс программы"""

    result = []
    sizeResult = 0

    while True:
        words = []
        for word in listWords:

            if len(word) <= sizeText and isComparisonOfLetters(lettersInText, word):
                words.append(word)

        choiceWord = choice(words)
        if choiceWord is None:
            print("!Неудачный текст, давай сначала!")
            main()
            sys.exit()
        result.append(choiceWord)
        sizeResult += len(choiceWord)

        ilettersInText = deletingLetters(lettersInText, choiceWord)

        if sizeResult >= sizeText:
            break
        print("Сейчас фраза: ", *result)
        print("Остались буквы: ", *list(ilettersInText.elements()), sep=', ')


    print("Получилась фраза:", end='')
    print(PrintColors.Blue, end=' ')
    print(*result)
    print(f"{PrintColors.Reset}")






# запуск программы
if __name__ == "__main__":
    # timeStart = time.time()
    main()
    # timeEnd = time.time()
    # print(f"{timeEnd - timeStart:.4f} sek")
    print(f"\n{PrintColors.Red}До встречи!!{PrintColors.Reset}")

