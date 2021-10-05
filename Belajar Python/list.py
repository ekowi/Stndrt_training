"""
Now i will learn tipe data list in tjis file
"""

daftar_buku = ['Jaringan Komputer', 'Berfikir Kritis', 'Belajar Python']

print("tampilkan daftar buku")
print(daftar_buku)

print('\nTampilkan daftar buku dengan for in')
for buku in daftar_buku:
    print(buku)
print('\nTampilkan daftar buku dari index tertentu')
print("3. ", daftar_buku[2])
print("1. ", daftar_buku[0])

print('\nTampilkan daftar buku for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])