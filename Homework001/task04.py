"""Пользователь вводит целое положительное число.
Программа выводит самую большую цифру в заданном числе."""

user_number = int(input('Введите целое положительное число '))

if user_number <= 0:
    print('Вы ввели неподходящее число')

else:
    max_digit = 0

    while user_number != 0:
        max_digit = max(max_digit, user_number % 10)
        user_number //= 10

    print(f'Самая большая цифра в заданном числе {max_digit}')
