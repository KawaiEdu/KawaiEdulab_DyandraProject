jadwal = []

while True:
    print("\njadwal kegiatan harian:", jadwal)
    print("1. tambah kegiatan ")
    print("2. hapus kegiatan ")
    print("3. keluar")
    pilihan = input("pilih opsi (1/2/3): ")
    
    if pilihan == "1":
        kegiatan = input("masukkan kegiatan baru: ")
        jadwal.append(kegiatan)
    elif pilihan == "2":
        kegiatan = input("masukkan kegiatan yang ingin dihapus: ")
        if kegiatan in jadwal:
            jadwal.remove(kegiatan)
            print(f"kegiatan '{kegiatan}'telah dihapus.")
        else:
            print("kegiatan tidak ditemukan!")
    elif pilihan == "3":
        print("semoga hari mu menyenangkan!")
        break
    else:
        print("pilihan tidak valid, coba lagi. ")