

import math


def persegi():
    sisi = float(input("Masukkan sisi persegi : "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi     =", luas)
    print("Keliling Persegi=", keliling)

def persegi_panjang():
    panjang = float(input("Masukkan panjang : "))
    lebar = float(input("Masukkan lebar   : "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang     =", luas)
    print("Keliling Persegi Panjang=", keliling)

def segitiga():
    alas = float(input("Masukkan alas   : "))
    tinggi = float(input("Masukkan tinggi : "))
    sisi1 = float(input("Masukkan sisi 1 : "))
    sisi2 = float(input("Masukkan sisi 2 : "))
    sisi3 = float(input("Masukkan sisi 3 : "))
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    print("Luas Segitiga     =", luas)
    print("Keliling Segitiga=", keliling)

def lingkaran():
    r = float(input("Masukkan jari-jari : "))
    luas = math.pi * r * r
    keliling = 2 * math.pi * r
    print("Luas Lingkaran     =", luas)
    print("Keliling Lingkaran=", keliling)


nama = input("Masukkan Nama Anda : ")
print("\nSelamat datang,", nama)


menu = [
    "Persegi",
    "Persegi Panjang",
    "Segitiga",
    "Lingkaran"
]

ulang = "iya"

while ulang == "iya":
    print("\n=== APLIKASI BANGUN DATAR ===")
    for i in range(len(menu)):
        print(i + 1, ".", menu[i])
    print("5. Keluar")

    pilihan = int(input("Pilih menu (1-5): "))

    if pilihan == 1:
        persegi()
    elif pilihan == 2:
        persegi_panjang()
    elif pilihan == 3:
        segitiga()
    elif pilihan == 4:
        lingkaran()
    elif pilihan == 5:
        print("Terima kasih", nama, ", program selesai.")
        break
    else:
        print("Pilihan tidak valid!")

    ulang = input("\nUlangi program? (iya/tidak): ")
