bmi = float(input("Masukkan BMI: "))
if bmi < 18.5:
    print("kekurangan berat badan. ")
elif bmi <= 24.9: 
    print("normal" )
elif bmi <= 29.9: 
    print("berat badan berlebih" )
else:
    print("obesitas")