"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове. """

user_lisl = input('Ведитее строку из нескольких слов, '
                  'разделенных пробеелом: ').split(' ')

number_str = 1

for i in user_lisl:
    temp_str = str([i])
    print(f"Строка №{number_str} {temp_str[0:12]}']")
    number_str += 1