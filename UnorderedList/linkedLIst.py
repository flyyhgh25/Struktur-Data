from node import NodeObject
class LinkedList:
    def __init__(self):
        self.head = None
       
    def is_empty(self):
        return self.head ==None
    def append(self,item):
        temp = NodeObject(item)
        # current = temp
        if self.head is None:
            self.head = temp
        else:
            current = self.tail
            current.setNext(temp)
        self.tail = temp
    # def add(self,item):
    #     temp = NodeObject(item)
    #     temp.setNext(self.head)
    #     self.head = temp
    #     self.data = temp.setData(item)
    #     self.isiData = temp.getData()
    #     print(f" Datat: {self.isiData}")
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if previous == None:
                self.head  = current.getNext()
            else:
                previous.setNext(current.getNext())
    def pop(self):
        current = self.head
        if(current is None):
            return -1
        else:
            prev = current
            while current.getNext() != None:
                prev = current
                current = current.getNext()
            prev.setNext(None)
            return current.getData()

myList = LinkedList()
print("\t=== MENAMBAHKAN DATA ====")
# myList.add(40)
# myList.add(66)
# myList.add(7)
myList.append(9)
myList.append(66)
myList.pop()