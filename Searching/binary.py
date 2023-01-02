# algoritma
# 1. Membaca data yang ada di array, jika data belum terurut, maka lakukan pengurutan data.
# 2. Menentukan data yang akan dicari di dalam array.
# 3. Menentukan nilai elemen tengah array, jika nilai elemen tengah array sama dengan data yang dicari, maka pencarian akan    dihentikan, jika elemen tengah tidak sama dengan data yang dicari, maka:
#    -> Jika nilai tengah lebih besar dari nilai yang dicari, maka pencarian hanya dilakukan pada setengah array pertama.
#    -> Jika nilai tengah lebih kecil dari nilai yang dicari, maka pencarian hanya dilakukan pada setengah array sisa.
#    -> Nilai tengah dindapatkan dari penjymlahan index ke-0 sampai index akhir dibagi 2
#    -> untuk mendapatkan index akhir dari len(data) - 1
def binarySearch(list,cari):
    first = 0
    last = len(list)-1
    found = False
    while first<=last and not found:
        nilaiTengah = (first+last)//2
        print("Niali tengah : ",nilaiTengah)
        if list[nilaiTengah] == cari:
            found = True
        else:
            if cari < list[nilaiTengah]:
                last = nilaiTengah-1
            else:
                first = nilaiTengah+1
    return found
# Algoritma binary search merupakan contoh bagus dari strategi pencarian data yang disebut divide and 
# conquer, yaitu dengan cara memecah kasus menjadi lebih kecil.
myList = [5,1,3,7,9]
myList.sort()
print(myList)
print(binarySearch(myList,4))

print("===========Binary Search Recursive================")
# Teknik recursive
def binarySearchRecursive(list,cari):
    if len(list)==0:
        return False
    else:
        nilaiTengah = len(list)//2
        if list[nilaiTengah] == cari:
            return True
        else:
            if cari<list[nilaiTengah]:
                return binarySearchRecursive(list[:nilaiTengah],cari)
            else:
                return binarySearchRecursive(list[nilaiTengah+1:],cari)

print(binarySearchRecursive(myList,4))

# Dalam pencarian data dilakukan perbanding data tengah
# Melakukan operasi perbandingan ke 1,2,3...x dengan jumlah data yang dicari n/2,n/4,n/8,...n/(2^x)dst
# Berapa jumlah operasi perbandingan 
# paling banyak? Jika data dalam list ada n items, maka setelah operasi perbandingan pertama data yang 
# dicari tinggal n/2, setelah operasi perbandingan kedua pencarian berikutnya tinggal n/4, dan seterusnya