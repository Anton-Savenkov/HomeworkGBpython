"""Пользователь вводит время в секундах. Программа перевоодит время в часы,
минуты и секунды и выводит в формате чч:мм:сс """

user_input_time = int(input('Введите время в секундах '))

horus = user_input_time // 3600
minutes = int((user_input_time % 3600) / 60)
seconds = int((user_input_time % 3600) % 60)

print(f"[{horus}:{minutes}:{seconds}]")
