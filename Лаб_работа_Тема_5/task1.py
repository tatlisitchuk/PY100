# TODO решить с помощью list comprehension и распечатать его

from pprint import pprint

qty = 15

super_dict = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(qty+1)]
# print(super_dict)
pprint(super_dict)