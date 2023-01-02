def bubbleSort(list):
    # print(len(list))
    for x in range(len(list)-1,0,-1): #2 1
        for i in range(x): # in => 3 => 0, 1, 2
            if list[i]>list[i+1]: #list[0]>list[1]
                temp = list[i] # temp = list[0]
                list[i] = list[i+1] #list[0] = list[1]
                list[i+1] = temp #list[1] = list[0]
                print(list)

data =[4,5,1,6]
# print(data)
bubbleSort(data)
print(data)