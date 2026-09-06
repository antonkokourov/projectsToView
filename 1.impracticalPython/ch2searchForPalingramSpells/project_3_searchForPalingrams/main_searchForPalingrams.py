#!! Project 3: search for palingrams -- поиск палинграмм

## 1.
## 2.
## 3.


import time
from PrintColors import *
from OpenText import *

timeStart = time.time()

fileDictionaryWords = r'file/2of4brif.txt'
listPalindromes = []

def main():
    """Основной процесс программы"""
    listWords = OpenText(fileDictionaryWords)
    listWords = [word for word in listWords if len(word) > 1]

    #listWords = ['tot', 'ant', 'tna', 'vera', 'nika', 'aki', 'narev', 'anna', 'a', 'nna', 'oshibka', 'lev', 'osovel', 'nurses', 'run', 'stir', 'grits']
                # [tot, tot], [ant, tna],   [vera, nika]
    setWords = set(listWords)
    #hashList = HashTable(listWords)

    result = []
    #sizeList = len(listWords)

    for word in listWords:
        # if len(word) < 2:
        #     continue
        re_word = word[::-1]
        size = len(word)
        for i in range(size):

            if re_word[:i] in setWords and re_word[i:] == re_word[i:][::-1]:
                    # w = sorted([word, re_word[:i]])
                    # if w not in result:
                    result.append([word, re_word[:i]])

            if re_word[i:] in setWords and re_word[:i] == re_word[:i][::-1]:
                    w = sorted([word, re_word[i:]])
                    if w not in result:
                        result.append([word, re_word[i:]])

    #print(sorted(result))
    print(len(result))


if __name__ == "__main__":
    timeStart = time.time()
    main()
    timeEnd = time.time()
    print(f"{timeEnd - timeStart:.4f} sek")
    print(f"\n{PrintColors.Red}До встречи!!{PrintColors.Reset}")


