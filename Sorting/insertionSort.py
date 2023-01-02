def insertionSort(list):
    for index in range(1,len(list)):
        curVal = list[index]
        posisi = index
        while posisi>0 and list[posisi-1]>curVal:
            list[posisi] = list[posisi-1]
            posisi = posisi-1
        
        list[posisi] = curVal

myList = [32,13,53,21,1,3,56,0]
insertionSort(myList)
print(myList)