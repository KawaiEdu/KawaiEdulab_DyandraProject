kalkulator = set()

while True:
    print("program perhitungan")
    print("1. penjumlahan \n2. pengurangan \n3. perkalian \n4. pembagian \n5. keluar")
    choiche = int(input("masukkan pilihan :"))
    if choiche == 1 :
        angka1 = int(input("masukkan angka 1: "))
        angka2 = int(input("masukkan angka 2: "))
        hasil_perkalian = angka1 * angka2
        kalkulator.add(hasil_perkalian)
    elif choiche == 4 :
        angka1 = int(input("masukkan angka 1: "))
        angka2 = int(input("masukkan angka 2: "))
        hasil_pembagian = angka1 / angka2
        kalkulator.add(hasil_pembagian)
    elif choiche == 5:
        print("terimakasihtelah menggunakan program aneh ini")
        break
    else:
        print("program anda salah")
        
for i in kalkulator :
    print(f" - {i} ")