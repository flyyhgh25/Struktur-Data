list = [3,2,1,3]
print(list)
print("mancari nomor")
cari = int(input("Masukkan angka yang akan dicari : "))
jml_pencarian = 0
while jml_pencarian != len(list):
    if(list[jml_pencarian]) == cari:
        where = list.index(cari)
        print(f"Angka {cari} ditemukan! pada index ke  {where}")
    jml_pencarian+=1

if cari not in list:
    print(f"Angka {cari} tidak ditemukan! ")
    