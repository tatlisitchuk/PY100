ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы
str_ALLOW= ''.join(ALLOW_SYMBOLS)
import re


def check_string(str_):
    res = bool(str_) and not re.sub('[01]', '', str_) # как вместо 01 сослаться на символы из ALLOW_SYMBOLS ?
    return res



    ...  # TODO проверить что в строку входят только символы 1 и 0


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
