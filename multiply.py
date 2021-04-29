# Author: Samuel Bennett
# Date: 4/28/2021
# Description: Determines multiplication value of two positive integers using addition

def multiply(x, y):
    if x == 1:
        return y
    return y + multiply(x-1, y)


print(multiply(23, 3))
