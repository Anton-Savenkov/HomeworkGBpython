"""Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма (прибыль — выручка
больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника."""

fin_result = 0

revenue = float(input('Введите значение выручки компании '))
costs = float(input('Введите значение издержек компании '))

if revenue > costs:
    fin_result = float(revenue) - float(costs)
    print(f'Выручка компании составила {fin_result}')
elif revenue < costs:
    fin_result = float(revenue) - float(costs)
    print(f'Убытки компании составили {- fin_result}')
else:
    print(f'Баланс компании равен {fin_result}')

headcount = input('Введите колличество сотрудников компании ')

if fin_result > 0:
    profit_per_person = fin_result / float(headcount)
    print(f'Прибыль фирмы в расчете на одного сотрудника '
          f'составляет {profit_per_person}')
elif fin_result < 0:
    lost_per_person = fin_result / float(headcount)
    print(f'Убыток фирмы в расчете на одного сотрудника '
          f'составляет {- lost_per_person}')
