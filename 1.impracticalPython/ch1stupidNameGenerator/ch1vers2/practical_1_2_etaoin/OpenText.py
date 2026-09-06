import sys

def OpenText(file):
    try:
        with open(file, encoding='utf-8') as fi:
            return fi.read()
    except IOError as e:
        print("Ошибка чтения файла", e, file)
        sys.exit(1)

