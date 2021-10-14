# kali ini kaan belajar fungsi dan definisi
# def utuk mendefinisikan lalu diikuti parameter dan perintah lalu diakhiri return

def bagi(angka1, angka2):           # kita mendefisinian lalu memberi parameter
    hasil = angka1 / angka2         # code yang berjalan jika kita memanggil def
    return hasil                    # return hasil untuk mengeluarkan dri def dan mengembalikan hasil(expresion)


result = bagi(10, 2)
print('dicetak dari result', result)

print('\n\n\n', "=" * 20)
print('kali ini def denganrerun none')
def cetak(paragraf):
    print(paragraf)
    return                  # return none untuk mengeluarkan dari def dan tidak mengembalikan hasil

paragraf = cetak('Hasil pemanggilan definisi')
print(paragraf)
