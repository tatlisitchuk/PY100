from random import sample
import re


def get_random_password() -> str:
    password = sample(re.compile(r'[a-zA-Z0-9]'), 8)
    return password


print(get_random_password())
