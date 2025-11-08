hari_libur = ("Minggu ")

hari = input("Masukkan hari: ")
if hari in hari_libur:
    print(f"{hari} adalah hari_libur! ")
else:
    print(f"{hari} adalah hari sekolah. ")