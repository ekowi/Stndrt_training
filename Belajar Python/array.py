import numpy as np

hp = ['iphone', 'samsung', 'xiaomi', 'nokia']

n = hp[2]
print(n)
print(type(hp))
print('-' * 20)

# try to add value in array using .append()
n =hp.append('motorola')
print(hp)
print('-' * 20)

# clear value array try using .clear()
hp = ['iphone', 'samsung', 'xiaomi', 'nokia']
hp.clear()
print(hp)
print('-' * 20)
# copy array try using .copy()
hp = ['iphone', 'samsung', 'xiaomi', 'nokia']
android = hp.copy()
print(android)
print('-' * 20)

# ada array to other array try using .extend()
fruit = ['apple', 'banana', 'pinapple']
android.extend(fruit)
print(android)

print('-' * 20)
# delete value in specified location try using .pop()
android.pop(4)
print(android)
print('-' * 20)

# remove value use name element try using .remove()
android.remove('banana')
android.remove('pinapple')
android.remove('iphone')
print(android)