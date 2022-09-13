from copy import copy
import math
from pickletools import int4
import numpy as np

def zeros(n):
    """returns the number of trailing zeros of an n factorial
    provided by the user"""

    factoriall = str(math.factorial(int(n)))
    factoriall = np.array(list(factoriall))
    print(factoriall)
    counter = -1
    zero_count = 0
    while True:
        if factoriall[counter] == "0":
            zero_count += 1
            counter -= 1
        else: 
            print(f"Factorial of {n}: {''.join(factoriall)}")
            print(f"Trailing zeros: {zero_count}")
            return zero_count
    
n = input("Enter n factorial:\n> ")
zeros(n)