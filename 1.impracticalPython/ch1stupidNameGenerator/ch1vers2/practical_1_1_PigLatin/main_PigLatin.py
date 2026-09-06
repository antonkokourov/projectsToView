#!! practical 1 ch1: "Pig Latin"

## 1. загрузить список гласных букв (а, е, ё, и, о, у, ы, э, ю, я)
## 2. читается весь текст, разбивается на слова.
## 3. проверка первой буквы согласная или гласная
##  3.1. если согласная, то первая буква перемещается назад и в конец добавляется "ау"
##  3.2. если гласная, в конец слова добавляется "вау"
## 4. выводится исправленный текст


# lib

from PrintColors import *

"""Списки имен"""
vowel_letter = set('аеёиоуыэюя') # гласные буквы
text = "Какой то текст. И, еще текст? Вот ещё. Ёмаё."
marks = set('.?,:;!')
ay = 'ау'
vay = 'вау'


def main():
    """Основной процесс программы"""
    result = []
    words = text.split() # разделили по словам
    print(text)
    print("_____________________")

    words = [w.strip() for w in words if w.strip()]
    for w in words:
        buffer = ''

        if w[-1] in marks:
            buffer = w[-1]
            w = w[:-1]
        isCapital = w[0].isupper()

        w = w.lower()
        newWord = pigWord(w)
        if buffer:
            newWord += buffer
        if isCapital:
            newWord = newWord[0].upper() + newWord[1:]
        result.append(newWord)

    print(f"\n{PrintColors.Blue}{' '.join(result)}{PrintColors.Reset}")

def pigWord(word):
    """Преобразование слова в хрюкающее"""
    if word[0] not in vowel_letter:
        word = word[1:] + word[0] + ay
    else:
        word = word + vay
    return  word

# end

if __name__ == "__main__":
    main()
    print(f"\n{PrintColors.Red}До встречи!!{PrintColors.Reset}")