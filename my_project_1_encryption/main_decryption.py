# -*- coding: utf-8 -*-
"""
    Project 8: routeCipher -- маршрутный шифр "decoding"

    1. Перевод текста и ключа в список слов
    2. Создание таблицы нужного размера
    3. Заполнение таблицы декодирования словами
    4. Чтение таблицы в нужном порядке, согласно ключа
    5. Вывод результата

"""

textLayout = 'file\\test.txt'

from OpenText import OpenText
from PrintColors import *

# key = '-1 2 -3 4'
# text = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'

def searchColumnsRows(textLen, keyLen):
    """Определение размера строки и колонки"""
    cols = keyLen
    rows = int(textLen / cols)
    return cols, rows

def readingFile():
    """Чтение файла шифра. Разделение на основной текс и ключ"""
    dirtyText = OpenText(textLayout)
    print(dirtyText)
    key = dirtyText[0]
    print(key)

    text = ''
    for row in range(1, len(dirtyText)):
        text += f'{dirtyText[row]} '
    print(text)
    return key, text

def main():
    key, text = readingFile()

    text_list = text.split(' ') # в список каждое слово

    key_int = [int(k) for k in key.split(' ')]

    cols, rows = searchColumnsRows(len(text_list), len(key_int))




    table_text = [None] * cols # создание таблицы слов
    print(text_list)
    print()
    w = 0 # индекс первого слова

    for i in range(cols):
        if key_int[i] < 0:
            table_text[i] = list(reversed(text_list[w:w + rows]))
        else:
            table_text[i] = text_list[w:w + rows]
        print(table_text[i])
        w += rows

    result = ''
    for r in range(rows):
        for c in range(cols):
            result += f'{table_text[c][r]} '

    print(PrintColors.Green)
    print(result)
    print(PrintColors.Reset)
    return

if __name__ == "__main__":
    main()
    print(f"\n{PrintColors.Blue}До встречи!!{PrintColors.Reset}")

