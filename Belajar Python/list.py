"""
Now i will learn tipe data list in tjis file
"""

pemilik_loker = ['ridwan','surya','shinta']

print("\nTampilkan isi List")
print(pemilik_loker)

print("\nTampilkan daftar list")
for loker in pemilik_loker:
    print(loker)

print("\nTampilkan daftar loker dengan for in range")
for i in range(0, len(pemilik_loker)):
    print(pemilik_loker[i])

print("\nTampilkan index tertentu")
print(pemilik_loker[2])

print("\nMenambahkan isi List")
pemilik_loker.append('ratu')
print("Ratu sudah ditambahkan", pemilik_loker)

#print("\nClear list")
#pemilik_loker.clear()
#for i in range(0, len(pemilik_loker)):
#   print(pemilik_loker[i])

print("\nMengambil list dan store list dengan (pop)")
vip = pemilik_loker.pop(2)
for i in range(0, len(pemilik_loker)):
    print(pemilik_loker[i])

print("\nMelihat store list")
print(vip)

pemilik_loker = ['ridwan','surya','shinta','ratu']
print("\n", pemilik_loker)
print("Menstore pop dari belakang dan dengan operasi minus(-)")
wanita = pemilik_loker.pop()
for i in range(0, len(pemilik_loker)):
    print(pemilik_loker[i])

print("\nOperasi minus (-2)")
pria = pemilik_loker.pop(-2)
for i in range(0, len(pemilik_loker)):
    print(pemilik_loker[i])

print("\nMelihat store list")
print(pria, wanita)