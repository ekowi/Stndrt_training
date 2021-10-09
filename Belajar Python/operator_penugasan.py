# Kali ini akan belajar operator penugasan

a = int(input("masukan variable a:"))
print(a)

# penjumlahan menggukana simbol +=
a += 10

# Operasi penjumlahan ini sama saja seperti
# a = a + 10 jadi kita me replace a sebelumnya dengan a + 10
print("variable (a) akan dijumlah 10 menjadi ", a)

# Pengurangan menggunakan simbol -=
a = int(input("masukan variable a:"))
a -= 2
print("variable (a) akan dikurang 2 menjadi ", a)

# Perkalian menggunakan simbol *=
a = int(input("masukan variable a:"))
a *= 10
print("variable (a) akan dikali 10 menjadi ", a)

# Pembagian menggunakan simbol /=
a = int(input("masukan variable a:"))
a /= 2
print("variable (a) akan dibagi 2 menjadi ", a)

# Sisa bagi atau modulus menggunakan simbol %=
a = int(input("masukan variable a:"))
a %= 2
print("variable (a) akan menghitung sisa bagi dari 2 menjadi ", a)

# Pemangkatan menggunakan simbol **=
a = int(input("masukan variable a:"))
a **= 3
print("variable (a) akan dipangkat menjadi ", a)

# Flooor division menggunakan simbol //=
a = int(input("masukan variable a:"))
a //= 2
print("variable (a) akan menghitung bagi 2 menjadi ", a)