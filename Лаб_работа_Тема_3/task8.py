money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить, он же счётчик

# TODO Оформить решение

def rest_(money_capital: float,
          month: int,
          salary: int,
          spend: int,
          increase: float = 0):
    money_capital = money_capital + salary * month - spend * month * (1 + increase) ** month
    return money_capital


while True:
    money_capital = rest_(money_capital, month, salary, spend, increase)
    if money_capital > 0:
        month += 1
    else:
        break


print(month)


