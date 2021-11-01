"""
this file will be learn lambda the anonymous fuction
"""

def myfucn(n):
    return lambda a : a * n

double = myfucn(2)

print(double(5))
print('-' * 30)
