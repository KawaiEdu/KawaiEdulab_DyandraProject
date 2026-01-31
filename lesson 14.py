kamus_husbu = {
    "dabi": "rambut berwarna hitam",
    "hawks": "rambut berwarna kuning",
    "shoto": "rambut berwarna merah putih",
}

husbu = input("Masukkan nama husbu: ")
if husbu in kamus_husbu:
    print(f"{husbu}: {kamus_husbu[husbu]}")
else:
    print("husbu tidak ditemukan dalam kamus.")