"""
This file for if else basic coding and i use example "mom told me to buy a bottle of milk and 6 eggs"
"""

# Sekuansi: eksekusi berutrutan
print('Ibu berkata ke budi "Pergi ketoko"')
print('budi menjawab "baiklah buk"')
print('budi telah sampai ditoko')
print('Apakah ada Susu?')

# Peercabangan: eksekusi terpilih (if else)
adaSusu = True
if adaSusu:
    print("Ada silahkan dibeli")
    uang = 10000
    if uang > 6000:
        print("Uang cukup, beli susu satu botol")
    else:
        print("Uang tidak cukup")
else:
    print("Sudah habis")
print("Apakah ada telur?")

adaTelur = False
if adaTelur:
    print("Sudah habis")
else:
    print("Ada, ingin berapa butir?")

print("ingin 6 butir")

# Perulangan: eksekusi berulang
jumlah_telur = 6

for jumlah_telur in range(1, jumlah_telur+1):
    print(f'Telur ke{jumlah_telur}')
