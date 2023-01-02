def tampil_menu():
    print("Toko Untung Utami")
    print("1. Tampil Data")
    print("2. Tambah Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Tampil Data Urut Nama")
    print("6. Keluar")
    pilih = int(input("Masukkan pilihan Anda : "))
    return pilih
def tampil_data(data):
    print ('Daftar Barang')
    print ('---------------------------------------------------------------------------------------')
    print ('|Kode Barang           |Nama Barang           | QTY |   Harga Beli   |   Harga Jual   |')
    print ('---------------------------------------------------------------------------------------')
    if (len(data) == 0):
        print ('|                            Data Barang Masih Kosong                                 |')
    else:
        for barang in data:
            print ("|",barang["kode"].ljust (20," ") ,"|",barang["nama"].ljust(20," "),"|",barang["qty"].center(3," "),"|",barang["harga_beli"].rjust(14," "),"|",barang["harga_jual"].rjust(14," "),"|")
    
    print ('---------------------------------------------------------------------------------------')
    input ('Tekan Enter untuk melanjutkan')

def tambah_data():
    kode_barang = input("Kode Barang  : ")
    nama_barang = input("Nama Barang  : ")
    qty = input("QTY          :")
    harga_beli = input("Harga Beli   :")
    harga_jual = input("Harga jual   :")
    barang = {"kode":kode_barang,"nama":nama_barang,"qty":qty,"harga_beli":harga_beli,"harga_jual":harga_jual}
    return barang

def edit_data(data):
    tampil_data(data)
    kode=input("Masukkan kode dari data barang yang akan anda edit :")
    ketemu = False
    posisi = -1
    for barang in data:
        print(barang)
        posisi += 1
        if(kode==barang['kode']):
            ketemu=True
            data[posisi]['harga_beli'] = input("Harga beli baru :")
            data[posisi]['harga_jual'] = input("Harga jual baru :")
            break
    if not ketemu:
        print("Kode tidak dimasukkan")

def hapus_data(data):
    tampil_data(data)
    # print(data)
    kode = input("Masukkan kode dari barang yang akan dihapus : ")
    ketemu = False
    posisi = -1
    print(posisi)
    for barang in data:
        print(barang)
        posisi += 1
        if(kode==barang['kode']):
            ketemu=True
            del(data[posisi])
            break
    if not ketemu:
        print("Kode tidak dimasukkan")
   
def urutData(data):
    for x in range(len(data)-1,0,-1):
        for i in range(x):
            print('datanya',i)
            if data[i]['nama']>data[i+1]['nama']: 
                temp = data[i]['nama'] 
                print(temp)
                data[i]['nama'] = data[i+1]['nama'] 
                data[i+1]['nama'] = temp 
    
# const bubbleSortRecursive = (array) => {
#   // Dummy check for single element in the array
#   if (array.length <= 1) return array;
#   // Boolean represents whether elements in the array have 
#   // been swapped
#   let check = false;
#   // Run through array and swap elements if second element 
#   // is greater than the first
#   for(let i = 0; i < array.length; i++) {
#     if (array[i + 1] < array[i]) {
#       swap(array, i, i + 1);
#       check = true
#     }
#   };
#   // If the elements haven't been swap the array is 
#   // sorted, return array
#   // else recursively call bubbleSortRecursive()
#   if (!check) {
#     return array
#   } else {
#     return bubbleSortRecursive(array);
#   }
# };