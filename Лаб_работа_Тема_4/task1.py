# TODO реализовать функцию
def remove_whitespace(str_: str):
    new_list = str_.split(' ')
    final_list = [i for i in new_list if bool(i) == True]
    new_str = ' '.join(final_list)
    return new_str


# почему не сработал split (он же несколько пробелов считает как один разделитель) и сразу join
def remove_whitespace2(str_: str):
    new_list = str_.split(' ')
    new_str = ' '.join(new_list)
    return new_str

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace2(str_with_space))
print(repr(str_with_space))
