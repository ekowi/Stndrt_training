from numpy import random

algebra = random.randn(8,5)
for lis in range (8):
    algebra[lis] = lis

print(algebra)