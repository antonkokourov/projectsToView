# -*- coding: utf-8 -*-

import sys
import json

def OpenText(file):
    try:
        with open(file, encoding='utf-8') as Fi:
            listWords = Fi.read().split('\n')
            listWords = [i.lower() for i in listWords if len(i) > 0]
            return listWords
    except IOError as Er:
        print("Ошибка чтения файла",Er, file)
        sys.exit(1)

def OpenJson(fileJson):
    """открытие файла json"""
    try:
        with open(fileJson, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except IOError as Er:
        print("Ошибка чтения файла",Er, fileJson)
        sys.exit(1)