"""This version doesn't calculate the factorial,
it just calculates the number of zeros"""

def zeros(n):
    """Calculates the number of zeros in a factorial n"""
    n = int(n)
    zeros = 0
    while True:
        zeros += n//5
        n //= 5
        if n == 0:
            break
    return zeros


n = input("Enter n factorial:\n> ")
print(zeros(n))
