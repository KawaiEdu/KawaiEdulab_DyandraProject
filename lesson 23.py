def diskon(harga, persen):
    potongan = harga * persen / 100
    return harga - potongan

# contoh penggunaan:
print(diskon(100000, 20)) # output: 80000.0

def halo(nama='siswa'):
    if nama == 'siswa':
        print("halo, peserta fans wibuu!")
    else:
        print(f"halo,{nama}!")
        
# contoh penggunaan:
halo("aizawa")  # output: halo, aizawa!
halo()   # output: halo,peserta fans wibuu!

def perkalian(a, b=2):
    return a * b

# contoh penggunaan:
print(perkalian(4))  # output: 8(karena b=2)
print(perkalian(4,5))  # output: 20