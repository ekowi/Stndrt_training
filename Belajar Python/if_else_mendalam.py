# Saya akan belajar if else mendalam

total_belanja = int(input("Masukan jumlah belanjaan RP"))

if total_belanja > 150000:
    print("Kamu mendapatkan diskon 10%")

diskon = total_belanja * 10/100
bayar = total_belanja - diskon


print("Kamu harus membayar RP ", int(bayar))
