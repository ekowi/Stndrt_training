# kali ini akan belajar try dan exception

# a = 10
# c = a / 'sa'
# print(c)
# output akan error karna integer tidak bisa mengoperasian string, maka dari itu kita gunakan try dan except

a = 10
b = "str"

print('penanggulangan jika terjadi kelasahan')
try:
    c = a / b
    print(c)
except TypeError:
    print('tidak bisa mengoperasikan int dan str')


print('=' * 20)
try:
    a = int(input("masukan nilai integer: "))   # input user akan menjadi int
    b = input("masukan nilai str: ")            # input user akan menjadi str
    c = a + b                                   # akan terjadi error jika tidak menggunakan try
    print(c)
except TypeError:
    print("nilai (a) anda adalah int maka tidak bisa dioperasikan dengan str")



print('=' * 20)
print('menggunakan else di try untuk penggulanngan jika tidak terjadi kesalahan')
try:
    a = int(input('masukan nilai int: '))
    b = int(input('masukan nilai int: '))
    c = a * b
except TypeError:
    print('masukan nilai integer/nomer')
else:
    print('nilai ', a, 'dikali', 'nilai ', b, '=')
    print(c)

print('=' * 20)
print('menggunakan finally pada try jika semua sudah terjadi')
try:
    a = int(input('masukan nilai int: '))
    b = input('masukan nilai b: ')
    c = a / b
except TypeError:
    print('tidak bisa membagi int dan str')
finally:
    print('terjadi kesalah input')
