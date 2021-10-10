# kali ini kita akan belajar casting string
# yaitu mengubah huruf besar/kecil menambahakan atau lain nya pada variable string


print("Upper dan Lower case")
nama_besar = input("masukan nama anda:")
nama_besar = nama_besar.upper()    #variable(str).upper() untuk mengubah string menjadi capital
print(nama_besar)

nama_kecil = input("masukan nama anda dengan huruf kapital:")
nama_kecil = nama_kecil.lower()     #variable(str).lower() untuk mengubah string capital menjadi kecil
print(nama_kecil)

print("-" * 10)

print("Sekarang kita akan menghapus whitespace pada string di variable menggunakan rstrip,lstrip,strip")

print("\nRSTRIP")
spasi_belakang = "Apakah ini ada whitespace                   "
print(spasi_belakang)
print("kita eksekusi")
print(spasi_belakang.rstrip())      #rstri() untuk menghapus whitespace disebelah kanan(right)

print("\nLSTRIP")
spasi_depan = "         Apakah ini ada whitespace"
print(spasi_depan)
print("kita eksekusi")
print(spasi_depan.lstrip())         #lstrip() untuk menghapus whitespace disebelah kiri(left)

print("\nStrip")
spasi_semua = "        Apakah ini ada whitespace              "
print(spasi_semua)
print("kita eksekusi")
print(spasi_semua.strip())          #strip juga bisa menghapus kata

print("\nMenghapus kata menggunakan strip")
spasi = "NamaNamaEKO WIDODONamaNama"
print(spasi)
print(spasi.strip("Nama"))
