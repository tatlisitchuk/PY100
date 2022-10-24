def get_count_char(str_: str) -> dict:
    new_str = str_.lower()
    dict_char = {}
    for i in new_str:
        if i in dict_char:
            dict_char[i] += 1
        elif i.isalpha():
            dict_char[i] = 1
    return dict_char


def get_share_char(dict_: dict) -> dict:
    all_char = sum(dict_.values())
    dict_share = {}
    if not dict_:
        print('В словаре нет значений!')
    else:
        for key, values in dict_.items():
            dict_share[key] = round(values / all_char * 100, 2)
        return dict_share




main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
b = get_count_char(main_str)
print(get_share_char(b))
