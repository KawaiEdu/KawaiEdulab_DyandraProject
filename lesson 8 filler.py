while True: 
    print("program konversi BMI")
    berat = float(input("berat dalam kilogram "))
    tinggi = float(input("Masukkan tinggi dalam meter "))
    bmi = berat / (tinggi**2)
    print(f"BMI ANDA ADALAH {bmi} ")