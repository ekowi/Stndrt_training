# kali ini akan beljar for lebih dalam

# for adalah perulangan yang terhitung sedangkan while adalah perulangan yang tidak terihitung atau memiliki syarat

kurcaci = ["doc", "dopey", "sleepy", "grumpy", "sneezy", "happy", "bashful"]
print(kurcaci)

print("\nmenghitung kurcaci")
for i in range(0, len(kurcaci)):
    print(kurcaci[i])
print("=" * 10)

print("\nDoc memberikan 20 apel ke putri salju, bantulah doc menghitung apel")
apel = 20

for i in range(1, apel+1):
    print(f"Doc memberikan apel ke-{i} ke putri salju")

print("\nsebutkan nama 7 kurcaci : ")
for nama in kurcaci:
    print(nama)
print("=" * 10)

# while adalah perulangan yang akan berhenti jika syarat terpenuhi

tanki_air = 20
isi_ulang = 0

while isi_ulang < tanki_air:
    isi_ulang += 1
    print(f"Doc sudah mengisi tanki air yang ke{isi_ulang}")
