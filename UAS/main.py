from my_lib import *
data_barang = []
pilih = tampil_menu()
# untuk kondisi pilih = 1,2,3,4,5
list_number = [i for i in range(1,6)]
while pilih in list_number:
    match pilih:
        case 1: 
            tampil_data(data_barang)
        case 2:
            barang = tambah_data()
            data_barang.append(barang)
        case 3:
            edit_data(data_barang)
        case 4:
            hapus_data(data_barang)
        case 5:
            urutData(data_barang)
            tampil_data(data_barang)
    pilih = tampil_menu()
