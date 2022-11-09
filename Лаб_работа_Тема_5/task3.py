from random import sample
min_ = -10
max_ = 10
qty = 15

def get_unique_list_numbers() -> list[int]:
    return sample(range(min_, max_+1), 15)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
