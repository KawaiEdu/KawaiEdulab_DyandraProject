while True:
    print("\nmMENU: [1] sapa [2] hitung [0] keluar")
    pilih = input("pilih: ").strip()
    if not pilih:
        continue
    if pilih =="0":
        print("sampai jumpa!")
        break
    elif pilih == "1":
        nama = input("namamu: ").strip()
        if not nama:
            continue
        print("halo,", nama + "!")
    elif pilih == "2":
        n = int(input("masukkan n: "))
        total = 0
        for i in range(1, n+1):
            total = 0
            for i in range(1, n+1):
                total += i
            print("jumlah 1..", n, "=", total)
        else:
            print("pilihan tidak valid")