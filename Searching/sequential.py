# pencarian data
#dimulai mulai dari index pertama
# jika sudah ditemukan berhenti, jika blm maka terus lanjut
def sequentialSearch(list,cari):
    found = False
    index = 0
    print(not found)
    while index<len(list) and not found:
        print(index)
        if list[index] == cari:
            found = True
        else :
            index+=1
    return found

myList = [2,6,8,5,3,0]
print(sequentialSearch(myList,6))

# KASUS TERBAIK (best case) jika item berada pada posisi yang pertama list (index = 0), maka sequential search hanya perlu melakukan operasi  perbandingan sekali saja. 
# KASUS TERBURUK (worst case) dimana item yang dicari tidak ada dalam list, maka sequential search harus melakukan operasi perbandingan sebanyak n.


# Cara menangani Worst Case
def sequentialSearch1(list,cari):
    found = False
    index = 0
    stop = False
    while index<len(list) and not found and not stop:
        print(index)
        if list[index] == cari:
            found = True
        else :
            if(list[index]>cari):
                stop = True
            else:
                index = index+1
    return found

myList = [2,6,8,5,3,0]
myList.sort()
print(myList)
print(sequentialSearch1(myList,4))
