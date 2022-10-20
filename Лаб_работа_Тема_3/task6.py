list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0
max_value = list_numbers[max_index]

for curr_ in range(len(list_numbers)):
    if list_numbers[curr_] > list_numbers[max_index]:
        max_index = curr_

list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]
print(list_numbers)

