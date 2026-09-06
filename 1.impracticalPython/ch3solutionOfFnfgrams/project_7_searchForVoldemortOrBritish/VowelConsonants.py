# VowelConsonants.py -- фильтрация с помощью проекции гласные-согласные
"""
    определение часто встречаемых последовательностей букв гласные-согласные
    и фильтрация слов
"""

from OpenText import *
from collections import defaultdict
from PrintColors import *

fileDictionaryWords = r'file/2of4brif.txt'
listWords = OpenText(fileDictionaryWords)

def wordListSize(size):
    """Вывод списка слов с указанным количеством букв"""
    wordsSize = []
    setWords = set(listWords)
    for word in setWords:
        if len(word) == size:
            wordsSize.append(word)
    return wordsSize

def VowelConsonant(wordsSize):
    """вывод конструкций гласные-согласные"""
    vowelsLett = 'aeyuioy'
    vowelCons = []
    for word in wordsSize:
        temporary = ''
        for lett in word:
            if lett in vowelsLett:
                temporary += 'v'
            else:
                temporary += 'c'
        vowelCons.append(temporary)
    listCV = list(set(vowelCons))

    return listCV

def filtrationCV(words, listCV):
    """Фильтрация на основе совпадений конструкций гласные-согласные"""
    vowelsLett = 'aeyuioy'
    wordsCV = []
    for word in words:
        temporary = ''
        for lett in word:
            if lett in vowelsLett:
                temporary += 'v'
            else:
                temporary += 'c'
        if temporary in listCV:
            wordsCV.append(word)
    return wordsCV


def cv_map(word, perms):
    """Основной процесс программы, выводит процент по последовательности букв гласные-согласные"""
    sizeLett = len(word)
    wordsSize = wordListSize(sizeLett)
    listCV = VowelConsonant(wordsSize)
    wordsCV = filtrationCV(perms, listCV)

    return wordsCV, listCV

