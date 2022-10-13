list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
new_set2 = set(list_)
sum_s = sum(new_set2)
len_s = len(new_set2)
aver_s = round(sum_s/len_s, 5)
print(sum_s)
print(len_s)
print(aver_s)
