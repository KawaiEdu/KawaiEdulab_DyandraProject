kelas = {
    "kelas A": ["deku", "bakugo"],
    "kelas B": ["monoma", "kendo"]
    
}

for nama_kelas, siswa in kelas.items():
    print(nama_kelas + ":")
    for s in siswa:
        print("- " + s)
    print()