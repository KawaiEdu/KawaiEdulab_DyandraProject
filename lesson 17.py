def tulis_catatan():
    catatan = input("masukkan catatan anda: ")
    with open("catatan.txt", "a") as file: 
        file.write(catatan + "\n")
    print("catatan berhasil disimpan!")
    
def baca_catatan():
    try:
        with open("catatan.txt", "r") as file:
            print("\ncatatan harian anda: ")
            print(file.read())
            file.close()
    except FileNotFoundError:
        print("belum ada catatan yang tersimpan.")
        
while True:
    print("\npilih menu: ")
    print("1. tulis catatan")
    print("2. baca catatan")
    print("3. keluar")
    pilihan = input("masukkan pilihan (1/2/3): ")
    
    if pilihan == "1":
        tulis_catatan()
    elif pilihan == "2":
        baca_catatan()
    elif pilihan == "3":
        print("terimakasih! sampai jumpa.")
        break
    else:
        print("pilihan tidak valid. silakan coba lagi.")