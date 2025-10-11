suhu = int(input("masukkan suhu udara saat ini (C): "))

if suhu < 10:
    print("Cuaca: dingin ")
    print("Saran: pakai jaket tebal dan makan ramen yang hangat! ")
elif suhu <= 25:
    print("Cuaca: sejuk ")
    print("Saran: waktunya berjalan-jalan ke mall atau bermain bersama saudara ")
elif suhu <= 35:
    print("Cuaca: hangat ")
    print("saran: bermain di pantai bersama keluarga atau berkumpul bersama keluarga kalian ")
else:
    print("Cuaca: panas")
    print("saran: tetap di dalam rumah dan rebahan untuk mengumpulkan semua nyawa untuk mu! ")