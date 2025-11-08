def konversisuhu(celcius):
    print("celcius ke reamur")
    hasil = 4/5 * celcius
    return hasil

def Fahrenheit(celcius):
    print("celcius ke fahrenheit")
    hasil = (9/5 * celcius) + 32
    return hasil

def kelvin(celcius):
    print("celcius ke kelvin")
    hasil = 273.15 + celcius
    return hasil

while True:
    print("\nprogram konversi suhu")
    print("1. suhu celcius")
    print("2. suhu reamur")
    print("3. suhu fahrenheit")
    print("4. suhu kelvin")
    print("5. keluar")
    choice = input("pilih menu anda: ")
    celcius = float(input("masukkan suhu celcius: "))
    
    if choice == "1":
        print(f"suhu celcius adalah {celcius}")
    elif choice == "2":
        hasil = konversisuhu(celcius)
        print(f"hasil celcius ke reamur adalah {hasil}")
    elif choice == "3":
        Fahrenheit(celcius)
        print(f"hasil celcius ke fahrenheit adalah {hasil}")
    elif choice == "4":
        kelvin(celcius)
        print(f"hasil celcius kelvin adalah {hasil}")
    elif choice == "5":
        print("keluar dari program")
        break
    else:
        print("input anda salah silahkan coba lagi")