#!! practical 2 ch1: "ETAOIN"

## 1. читает текст по каждому символу.
## 2. определяет букву, добавляем ее в словарь, если ее там нет
## 3. считаем количество каждой буквы
## 4. выводим результат



# lib
from collections import defaultdict
from collections import Counter
import pprint
from PrintColors import *
from OpenText import *

file = 'files\\text.txt'
text = OpenText(file)
text = text.lower()

def main():
    """Основной процесс программы"""

    # отображение каждого символа в словаре
    resultStr = defaultdict(list)
    resultInt = defaultdict(int)

    for i in text:
        if i.isalnum():
            resultStr[i].append(i)
            resultInt[i] += 1
    resultStr = dict(sorted(resultStr.items()))
    resultInt = dict(sorted(resultInt.items()))

    print(PrintColors.Blue)
    pprint.pprint(resultStr, compact=True, width=1000)
    print(PrintColors.Cyan)
    pprint.pprint(resultInt)
    print(PrintColors.Reset)

    # result = Counter(text) # автоматический счет символов
    # print(result)

# end

if __name__ == "__main__":
    main()
    print(f"\n{PrintColors.Red}До встречи!!{PrintColors.Reset}")