# selection sort mencari posisi dari angka terbesar untuk diletakkan di akhir siklus
def selectionSort(list):
    for x in range(len(list)-1,0,-1): #3,2,1
        maxPos = 0
        for loc in range(1,x+1): #(1,4) => 1,2,3
            if list[loc]>list[maxPos]: #list[1]>list[0]
                maxPos = loc #maxPos = 1
        temp = list[x] #temp = list[3]
        list[x] = list[maxPos] #list[3] = list[1]
        list[maxPos] = temp #list[1] = list[3]
    
list = [32,12,31,22]
selectionSort(list)
print(list)

# selection sort memiliki jumlah operasi perbandingan yang 
# sama dengan bubble-sort, yaitu O(n2).
#  Namun demikian selection sort memiliki keunggulan pada jumlah 
# operasi pertukaran data yang lebih kecil, sehingga memerlukan waktu yang lebih singkat jika 
# dibandingkan dengan bubble-sort.