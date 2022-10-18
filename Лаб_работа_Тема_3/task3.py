x = 1
y = -1
'''
# TODO переписать через if-elif-else
if x > 0:
    if y > 0:               # x > 0, y > 0
        print("Первая четверть")
    else:                   # x > 0, y < 0
        print("Четвертая четверть")
else:
    if y > 0:               # x < 0, y > 0
        print("Вторая четверть")
    else:                   # x < 0, y < 0
        print("Третья четверть")
'''
if x > 0:
    if y > 0:               # x > 0, y > 0
        print("Первая четверть")
    else:                   # x > 0, y < 0
        print("Четвертая четверть")
elif y > 0:              # x < 0, y > 0
        print("Вторая четверть")
else:                   # x < 0, y < 0
        print("Третья четверть")