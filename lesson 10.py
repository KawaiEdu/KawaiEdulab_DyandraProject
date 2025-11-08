tambah = lambda x, y: x + y
kurang = lambda x, y: x - y
kali = lambda x, y: x * y
bagi = lambda x, y: x / y

print("program kalkulator lambda")
x = float(input("masukkan angka pertama: "))
y = float(input("masukkan angka kedua: "))
choice = input("pilih operasi(pilih 0 untuk keluar) ")

if x != 0 and y != 0 :
    if choice == "+":
        print("hasil operasi tambah adalah ", tambah(x, y))
    elif choice == "-":
        print("hasil operasi pengurangan adalah ", kurang(x, y))
    elif choice == "*":
        print("hasil operasi perkalian adalah ", kali(x, y))
    elif choice == "/":
        print("hasil operasi pembagian adalah ", bagi(x, y))
else:
    print("keluar dari program")