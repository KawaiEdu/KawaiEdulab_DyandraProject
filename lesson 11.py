daftar_belanja = []

while True:
    print("\nDaftar Belanja:", daftar_belanja)
    print("1. Tambah item ")
    print("2. Hapus item ")
    print("3. Keluar ")
    pilihan = input("Pilih opsi (1/2/3):")
    
    if pilihan == "1":
        item = input("Masukkan item yang ingin ditambahkan: ")
        daftar_belanja.append(item)
    elif pilihan == "2":
        item = input("Masukkan item yang ingin dihapus: ")
        if item in daftar_belanja: 
            daftar_belanja.remove(item)
        else:
            print("item tidak ditemukan dalam daftar! ")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program kepet ini! ")
        break
    else:
        print("Pilihan tidak valid, coba lagi. ")
