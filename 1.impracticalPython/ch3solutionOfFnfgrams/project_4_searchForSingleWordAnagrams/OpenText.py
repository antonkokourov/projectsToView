# -*- coding: utf-8 -*-

import sys

def OpenText(file):
    try:
        with open(file, encoding='utf-8') as Fi:
            listWords = Fi.read().split('\n')
            #listWords = [i.strip() for i in listWords if len(i) > 1]
            listWords = [i.lower() for i in listWords if len(i) > 0]
            return listWords
    except IOError as Er:
        print("Ошибка чтения файла",Er, file)
        sys.exit(1)

def HashTable(listWords):
    hashT = [{0}, ]
    maxSize = 0
    for h in range(1, 16):
        buffer = []
        for w in listWords:
            if len(w) > maxSize:
                maxSize = len(w)
            if len(w) == h and h < 15:
                buffer.append(w)

            elif len(w) >= 15 and h == 15:
                buffer.append(w)
        hashT.append(set(buffer))
    return hashT

