usia = int(input("Masukkan usia: "))
if usia < 12:
    print("kategori: Anak-anak ")
elif usia <= 18:
    print("kategori: Remaja ")
elif usia >= 25: 
    print("kategori: Dewasa ")
else: print("kategori: Tua ")