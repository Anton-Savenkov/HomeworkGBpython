"""Программа расчета суммы чисел n + nn + nnn, число n задается пользователем"""



user_number = int(input('Введите натуральное число '))

sum_number = user_number + user_number * 11 + user_number * 111


print(f'Сумма чисел {user_number} + {user_number}{user_number} + '
      f'{user_number}{user_number}{user_number} равна {sum_number}')
