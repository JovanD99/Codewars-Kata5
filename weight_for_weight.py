from ipaddress import summarize_address_range
from signal import set_wakeup_fd
from typing import OrderedDict

# This version doesn't work correctly

def order_weight(string_of_weights):
    """This function orders the weights in order of the sums of their digits"""
    weights_str = string_of_weights.strip().split()
    sums_index_tupple = [] 
    for index, val in enumerate(weights_str):
         sums_index_tupple.append((sum(map(int, val)), index, val))
    sums_index_tupple.sort()
    for index, val in enumerate(sums_index_tupple):
        if index < len(sums_index_tupple) - 1:
            if val[0] == sums_index_tupple[index + 1][0]:
                if val[2] > sums_index_tupple[index + 1][2]:
                    temp = val
                    sums_index_tupple[index] = sums_index_tupple[index + 1]
                    sums_index_tupple[index + 1] = temp
            
    result = []
    for val in sums_index_tupple:
        result.append(weights_str[val[1]])
    
    return " ".join(result)




    



var = input("Enter weights:\n> ")
print(order_weight(var))
