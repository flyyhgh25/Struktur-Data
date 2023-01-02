# Buat Program untuk menginputkan beberapa data nilai mahasiswa
# NIM, Nama, Nilai. 
# Kemudian data diurutkan berdasarkan nilai menggunakan method:
    # a. Bubble Sort
    # b. Selection Sort 
    # c. Insertion Sort  

nim = [213456,34567,55667]
mahasiswa=['Rara','Ahmad','Zahra','Sinta']

# Bubble Sort
def bubbleSort(list):
    # print(len(list))
    for x in range(len(list)-1,0,-1): #2 1
        for i in range(x): # in => 3 => 0, 1, 2
            if list[i]>list[i+1]: #list[0]>list[1]
                temp = list[i] # temp = list[0]
                list[i] = list[i+1] #list[0] = list[1]
                list[i+1] = temp #list[1] = list[0]
                print(list)
# print(data)
# bubbleSort(mahasiswa)
# print(mahasiswa)

# Selection Sort
def selectionSort(list):
    for x in range(len(list)-1,0,-1): #3,2,1
        maxPos = 0
        for loc in range(1,x+1): #(1,4) => 1,2,3
            if list[loc]>list[maxPos]: #list[1]>list[0]
                maxPos = loc #maxPos = 1
        temp = list[x] #temp = list[3]
        list[x] = list[maxPos] #list[3] = list[1]
        list[maxPos] = temp #list[1] = list[3]
    
# list = [32,12,31,22]
# selectionSort(mahasiswa)
# print(mahasiswa)

    
def insertionSort(list):
    for index in range(1,len(list)):
        curVal = list[index]
        posisi = index
        while posisi>0 and list[posisi-1]>curVal:
            list[posisi] = list[posisi-1]
            posisi = posisi-1
        list[posisi] = curVal

myList = [32,13,53,21]
insertionSort(mahasiswa)
print(mahasiswa)
