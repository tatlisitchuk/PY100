a = 73
b = 10
c = 55

x = 45  # переменная, меньше которой должно быть только одно число

condition_1 = (a < x) and (b > x) and (c > x)   # TODO записать условие, что только первое число меньше 45
condition_2 = (b < x) and (a > x) and (c > x)
condition_3 = (c < x) and (b > x) and (a > x)   # TODO записать условие, что только третье число меньше 45

if condition_3 or condition_2 or condition_1:
    print("Одно из чисел меньше 45")
