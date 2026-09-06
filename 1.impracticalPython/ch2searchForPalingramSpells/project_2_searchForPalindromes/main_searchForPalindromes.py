#!! Project 2: Search for palindromes -- поиск палиндромов

## 1. загрузить цифровой словарь
## 2. проверить это слово палиндром
## 3. вывести список палиндромов


# lib

from PrintColors import *
from OpenText import *

fileDictionaryWords = r'file/2of4brif.txt'
listPalindromes = []

def main():
    """Основной процесс программы"""
    listWords = OpenText(fileDictionaryWords)
    listPalindromes.extend(w for w in listWords if len(w) > 1 and w[:] == w[::-1])
    print(f"{PrintColors.Green}Найдено {len(listPalindromes)} слов{PrintColors.Reset}")
    print(listPalindromes)

if __name__ == "__main__":
    main()
    print(f"\n{PrintColors.Red}До встречи!!{PrintColors.Reset}")

