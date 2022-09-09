import enum
from ipaddress import summarize_address_range
from signal import set_wakeup_fd
from typing import OrderedDict

# This version doesn't work correctly
def order_weight(string_of_weights):
    """This function orders the weights in order of the sums of their digits"""
    list_of_strings = string_of_weights.strip().split()
    lists_of_chars = list(map(list, list_of_strings))
    lists_of_ints = [list(map(int, l)) for l in lists_of_chars]
    lists_of_ints.sort(key=sum)
    sums = [sum(l) for l in lists_of_ints]
    d = {}
    for el in sums:
        d[el] = []
    for index, el in enumerate(sums):
        d[el].append(int("".join(list(map(str, lists_of_ints[index])))))
    for el in d:
        d[el].sort()

    for key, value in d.items():
        d[key] = list(map(str, value))

    for key in d:
        d[key].sort(key=lambda x: x[0])

    
    strings = []
    for el in d:
        for val in d[el]:
            strings.append(val)
  
    return " ".join(strings)
    
      
var = input("Enter weights:\n> ")
print(order_weight(var))
