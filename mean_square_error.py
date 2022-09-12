import numpy as np

def solution(array_a, array_b):
    arr1 = np.array(array_a)
    arr2 = np.array(array_b)
    return np.mean((abs(arr1 - arr2)) ** 2)
