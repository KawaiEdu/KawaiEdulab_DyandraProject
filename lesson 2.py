nama = input("Siapa nama kamu? ")
umur = int(input("Berapa umur kamu? "))
tinggi = float(input("Berapa tinggi badan kamu(dalam meter)? "))

suka_Udon = input("Apakah kamu suka makan Udon?(ya/tidak) ").lower() == "ya"

print("\nInformasi yang kamu masukkan:")
print("Nama: ", nama)
print("Umur: ", umur)
print("Tinggi badan: ", tinggi," meter")

print("Suka makan Udon: ", suka_Udon)