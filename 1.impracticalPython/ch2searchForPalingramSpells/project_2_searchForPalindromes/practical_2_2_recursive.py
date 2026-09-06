#!! searchForPalindromes recursive

from OpenText import *
import sys

file = r'file/2of4brif.txt'
words_list = OpenText(file)


def recursive(word):
    """реверс для определения палиндромы"""
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return recursive(word[1:-1])

def main():
    """основной цикл программы"""
    while True:

        word = input("Введите слово или введите 'q' для выхода: ")
        if word == 'q':
            sys.exit()
        if len(word) < 1:
            print("Вы ничего не ввели!")
        elif len(word) == 1:
            print("Вы ввели одну букву, а это палиндром!")
        elif word.lower() not in words_list:
            print("это странное слово, давай еще раз")
        elif recursive(word.lower()):
            print("Именно это слово я и ждал, это палиндром")
        else:
            print("Это не палиндром")




if __name__ == '__main__':
    main()
