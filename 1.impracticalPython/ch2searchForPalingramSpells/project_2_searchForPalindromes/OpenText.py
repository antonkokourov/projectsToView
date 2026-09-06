import sys

def OpenText(file):
    try:
        with open(file, encoding='utf-8') as Fi:
            listWords = Fi.read().split('\n')
            #listWords = [i.strip() for i in listWords if len(i) > 1]
            listWords = [i for i in listWords if len(i) > 0]
            return listWords
    except IOError as Er:
        print("Ошибка чтения файла",Er, file)
        sys.exit(1)

