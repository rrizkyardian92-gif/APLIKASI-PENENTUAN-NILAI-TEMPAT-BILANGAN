# Aplikasi Penentuan Nilai Tempat Bilangan RISKI ARDIAN

def proses_nilai_tempat(angka):
    daftar = [
        (10**6, "Jutaan"),
        (10**5, "Ratusan Ribu"),
        (10**4, "Puluhan Ribu"),
        (10**3, "Ribuan"),
        (10**2, "Ratusan"),
        (10**1, "Puluhan"),
        (10**0, "Satuan"),
    ]

    print("\n--- HASIL PEMECAHAN BILANGAN ---")
    sisa = angka

    for pembagi, nama in daftar:
        nilai = sisa // pembagi
        sisa = sisa % pembagi

        if angka >= pembagi:
            print(f"{nama:15} : {nilai}")

    print("---------------------------------")


try:
    data = input("Masukkan bilangan (maks 7 digit): ")

    if data.isnumeric():
        bilangan = int(data)

        if bilangan <= 9999999:
            proses_nilai_tempat(bilangan)
        else:
            print("Maksimal hanya sampai jutaan!")

    else:
        print("Input harus berupa angka!")

except:
    print("Terjadi kesalahan saat menjalankan program.")
