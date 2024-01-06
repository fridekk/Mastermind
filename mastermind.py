import time
import random

text = 'Быки и коровы'
width = 160
print(text.center(width))

instr = input('Тебе нужна инструкция?  ')
if instr.lower() == 'да':
    rules = [
        "Игра 'Быки и коровы' - это логическая игра, в которой ваша задача - угадать загаданное компьютером число.",
        "Компьютер загадывает четырехзначное число, все цифры которого различны (первая цифра числа не равна 0).",
        "Ваша задача - угадать это число, делая предположения и получая подсказки.",
        "После каждого вашего предположения компьютер дает подсказку в формате 'X быков, Y коров'.",
        "'Бык' - это угаданная цифра, стоящая на своем месте, 'корова' - это угаданная цифра, "
        "стоящая не на своем месте.",
        "Игра продолжается до тех пор, пока вы не угадаете число (получите 4 быка).",
        "Удачи!"
    ]

    for line in rules:
        print(line)
        time.sleep(3)
else:
    print('Хорошо')


def get_bulls_and_cows(secret_number, user_number):
    bulls = cows = 0
    for i in range(4):
        if secret_number[i] == user_number[i]:
            bulls += 1
        elif secret_number[i] in user_number:
            cows += 1
    return bulls, cows


tries = 0
secret_number = str(random.randint(1000, 9999))

while tries <= 10:
    user_number = input('Введи четырехзначное число:  ')
    if len(user_number) != 4 or not user_number.isdigit():
        print("Пожалуйста, введите четырехзначное число.")
        continue
    bulls, cows = get_bulls_and_cows(secret_number, user_number)
    print(f"Быки: {bulls}, Коровы: {cows}")
    if bulls == 4:
        print("Поздравляем, вы выиграли!")
        break
    tries += 1
else:
    print(f"Вы проиграли. Загаданное число было {secret_number}.")
