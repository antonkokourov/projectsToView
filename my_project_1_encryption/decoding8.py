# тестовый код
# decoding

from PrintColors import *

cols = 4
rows = 5
key = '-1 2 -3 4'
text = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'

def main():

    text_list = text.split(' ') # в список каждое слово
    key_int = [int(k) for k in key.split(' ')]
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


