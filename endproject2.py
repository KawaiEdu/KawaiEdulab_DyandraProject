# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nSelamat datang di program daftar tugas!")
    print("1. tambah tugas")
    print("2. tampilkan daftar tugas")
    print("3. hapus tugas")
    print("4. simpan daftar ke file")
    print("5. muat daftar dari file")
    print("6. keluar")
    

# Fungsi untuk menambahkan tugas
def tambah_tugas(daftar):
    tugas = input("masukkan nama tugas: ")
    daftar.append(tugas)
    print("{} berhasil ditambahkan ke daftar tugas.".format(tugas))

# Fungsi untuk menampilkan daftar tugas
def tampilkan_daftar(daftar):
    if daftar:
        print("n\daftar tugas:")
        for i, tugas in enumerate(daftar, start=1):
            print("{}.{}".format(i, tugas))
        else: 
            print("daftar tugas kosong.")
            
# Fungsi untuk menghapus tugas 
def hapus_tugas(daftar):
    tampilkan_daftar(daftar)
    try:
        nomor = int(input("masukkan nomor tugas yang ingin dihapus"))
        if 1 <= nomor <= len(daftar):
            tugas = daftar.pop(nomor - 1)
            print("{} berhasil dihapus dari daftar tugas.".format(tugas))
        else:
            print("nomor tugas tidak valid.")
    except ValueError:
        print("input harus angka!")
        
# Fungsi untuk menyimpan daftar ke file
def simpan_daftar(daftar):
    try:
       with open("daftar_tugas.txt","w") as file:
           for tugas in daftar:
               file.write(tugas + "\n") 
               print("daftar tugas berhasil disimpan ke file.")
    except Exception as e:
        print("terjadi kesalahan saat menyimpan: {}".format(e))

# Fungsi untuk memuat daftar dari file
def muat_daftar():
    try:
        with open("daftar_tugas.txt","r") as file:
            daftar = [line.strip()for line in file]
        print("daftar tugas berhasil dimuat dari file.")
        return daftar
    except IOError: # Gunakan IOError agar kompatibel dengan Python 3.4
        print("file daftar tugas berhasil dimuat dari file.")
        return[]
    except Exception as e:
        print("terjadi kesalahan saat memuat: {}".format(e))
        
# Program utama
def main():
    daftar = muat_daftar() # Memuat daftar dari file saat program dimulai
    
    while True:
        tampilkan_menu()
        pilihan = input("masukkan pilihan (1-6): ")
        
        if pilihan =="1":
            tambah_tugas(daftar)
        elif pilihan =="2":
            tampilkan_daftar(daftar)
        elif pilihan =="3":
            hapus_tugas(daftar)
        elif pilihan =="4":
            simpan_daftar(daftar)
        elif pilihan =="5":
            daftar = muat_daftar()
        elif pilihan == "6":
            print("terima kasih! sampai jumpa!")
            break
        else:
            print("pilihan tidak valid. silakan coba lagi.")
            
if __name__=="__main__":
    main()