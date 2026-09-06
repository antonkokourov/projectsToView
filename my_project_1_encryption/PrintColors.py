# Определяем цвета
class PrintColors:
    # Текст
    Red = '\033[91m' # Красный
    Green = '\033[92m' #
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    # Стили
    Bold = '\033[1m'
    Underline = '\033[4m'
    # Сброс
    Reset = '\033[0m'

"""
---=== Использование===---

print(f"{PrintColors.Green}Привет{PrintColors.Reset}")
print(f"{PrintColors.Bold}{PrintColors.Blue}Жирный синий текст{PrintColors.Reset}")
print(f"{PrintColors.Red}Ошибка{PrintColors.Reset} {PrintColors.Yellow}Внимание{PrintColors.Reset}")

"""