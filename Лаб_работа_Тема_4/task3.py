def delete(list_: list, index=None):
    index = len(list_) - 1 if index is None else index
    list1 = list_[:index]
    list2 = list_[index + 1:]
    list_new = list1 + list2
    return list_new


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

