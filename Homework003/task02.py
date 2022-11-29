"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

user_name = input('Введите имя: ')
user_surname = input('Ведите фамилию: ')
user_birth = input('Введите дату рождения: ')
user_citi = input('Введите город проживания: ')
user_email = input('Введите адрес электронной почты: ')
user_tel = input('Введите нонмер телефона: ')


def user_full_name(name_a, name_b):
    """Функция обьеденения введенных пользователем имени и фамилии"""
    return user_name + ' ' + user_surname


full_name = user_full_name(user_name, user_surname)


def user_data_output(name=full_name, year_birth=user_birth, city=user_citi,
                     email=user_email, tel=user_tel):
    """Функция принимает данные введенные пользователем
    и выводит их одной строкой"""

    print(f"Данные пользователя: {name} {year_birth} "
          f"{city} {email} {tel}")


user_data_output()
