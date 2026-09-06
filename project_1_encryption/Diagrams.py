# Diagrams.py -- составление диграмм
"""
    анализ всего списка слов и определение процента встречаемых пар букв
    вывод словаря пар букв с результатом встречаемости в отдельный файл
"""
passPercentage = 0.09

import os
from OpenText import *
from collections import defaultdict
import json

fileDictionaryWords = r'file/2of4brif.txt'
listWords = OpenText(fileDictionaryWords)

def duAlphabet():
    """Выявление всех возможных пар букв в английском языке (теоретически)"""
    alphabet = ''.join([chr(97 + i) for i in range(26)])
    twoLetters = {}
    for i in alphabet:
        for j in alphabet:
            buffer = i + j
            twoLetters.update({buffer: 0})
    return twoLetters

def savFinish(data):
    """Сохранение диаграмы в файл json"""
    with open('finishLetter.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def savFirst(data):
    """Сохранение диаграмы в файл json"""
    with open('firstLetter.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def savFile(data):
    """Сохранение диаграмы в файл json"""
    with open('letter_combination.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        print("Файл готов к применению.")

def getPercent(duAlpha):
    """Получение совпадений букв в процентном соотношении"""
    size = sum(duAlpha.values())
    for da in duAlpha:
        duAlpha[da] = round(duAlpha[da] / size * 100, 2)

    duAlpha = dict(sorted(duAlpha.items(), key=lambda x: x[1], reverse=True))
    return duAlpha

def filtrationDuAlpha(words):
    """Фильтрация слов на основе созданного файла"""
    dataFirst = OpenJson('firstLetter.json')
    dataFinish = OpenJson('finishLetter.json')
    data = OpenJson('letter_combination.json')
    wordsDA = []

    for word in words:
        size = len(word)
        flag = True
        if size > 2:
            if word[:2] not in dataFirst or word[-3:] not in dataFinish:
                flag = False
        for i in range(1, size):
            buffer = word[i - 1] + word[i]
            if not flag or data[buffer] < passPercentage:
                flag = False
                break
        if flag:
            wordsDA.append(word)
    return list(set(wordsDA))

def Diagrams():
    """Основная программа, вывод встречаемых пар букв и их процент встречаемости"""

    duAlpha = duAlphabet()
    firstLett = []
    finishLett = []
    for word in listWords:
        size = len(word)
        if size > 2:
            firstLett.append(word[:2])
            finishLett.append(word[-3:])

        for i in range(1, size):
            buffer = word[i-1] + word[i]
            duAlpha[buffer] += 1

    duAlpha = getPercent(duAlpha)
    savFirst(list(set(firstLett)))
    savFinish(list(set(finishLett)))
    savFile(duAlpha)





if __name__ == '__main__':
    Diagrams()