error = 0;
#pip install termcolor
from termcolor import colored, cprint

def letters_to_numbers(text):
    result = []
    global error;
    for char in text.upper():
        if 'A' <= char <= 'Z':
            num = ord(char) - ord('A') + 1
            result.append(str(num))
        else:
            result.append(colored(char, "red"))  # не буквы оставляем как есть
            error += 1
    return ' '.join(result)


def numbers_to_letters(numbers_str):
    parts = numbers_str.split()
    result = []
    global error;
    for part in parts:
        if part.isdigit():
            num = int(part)
            if 1 <= num <= 26:
                char = chr(num + ord('A') - 1)
                result.append(char)
            else:
                result.append(colored(part, "red"))  # если число не в диапазоне 1-26
                error += 1
        else:
            result.append(colored(part, "red"))  # если не число
            error += 1
    return ''.join(result)





def russian_letters_to_numbers(text):
    result = []
    global error;
    for char in text.upper():
        if 'А' <= char <= 'Я':
            num = ord(char) - ord('А') + 1  
            result.append(str(num))
        elif char == 'Ё':
            result.append('7')  # Ё обычно идёт после Е (Е=6, Ё=7)
        else:
            result.append(colored(char, "red"))  # не буквы оставляем как есть
            error += 1
    return ' '.join(result)


def numbers_to_russian_letters(numbers_str):
    parts = numbers_str.split()
    result = []
    global error;
    for part in parts:
        if part.isdigit():
            num = int(part)
            if 1 <= num <= 6:  # А-Е
                char = chr(num + ord('А') - 1)
            elif num == 7:  # Ё
                char = 'Ё'
            elif 8 <= num <= 33:  # Ж-Я (с учётом сдвига из-за Ё)
                char = chr(num + ord('А') - 2)  # потому что Ё занимает место
            else:
                char = colored(part, "red")  # если число вне диапазона
                error += 1
            result.append(char)
        else:
            result.append(colored(part, "red"))  # если не число
            error += 1
    return ''.join(result)






language = str(input("Введите язык (русский/английский): "))

if language == "русский":
    incoded_decoded = str(input("Что вы хотите сделать (кодировать/декодировать): "))
    if incoded_decoded == "кодировать":
        encoded_russian = russian_letters_to_numbers(str(input("Введите текст для кодировки: ")))
        print(encoded_russian)
        if error > 0:
            print("В текущем тексте имеется не разпознаный символ: " + str(error))
    elif incoded_decoded == "декодировать":
        decoded_russian = numbers_to_russian_letters(str(input("Введите цыфры для декодировки через пробел: ")))
        print(decoded_russian)
        if error > 0:
            print("В текущем тексте имеется не разпознаный символ: " + str(error))

elif language == "английский":
    incoded_decoded = str(input("Что вы хотите сделать (кодировать/декодировать): "))
    if incoded_decoded == "кодировать":
        encoded = letters_to_numbers(str(input("Введите текст для кодировки: ")))
        print(encoded)
        if error > 0:
            print("В текущем тексте имеется не разпознаный символ: " + str(error))
    elif incoded_decoded == "декодировать":
        decoded = numbers_to_letters(str(input("Введите цыфры для декодировки через пробел: ")))
        print(decoded)
        if error > 0:
            print("В текущем тексте имеется не разпознаный символ: " + str(error))
