class Node:
    def __init__(self):
        self.data = None
        self.next = None    
    def setData(self,data):
        self.data = data
        return self.data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
        return self.next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None

class NodeImplement():
    def __init__(self):
        self.head = None
        self.length = 0
    def listLength(self):
        cur = self.head
        count = 0
        while cur!=None:
            count = count+1
            cur = cur.getNext()
        return count
    def is_empty(self):
        self.head = None
        return self.head
    def add(self,data):
        newNode = Node()
        newNode.setData(data)
        self.head = newNode
        self.isiData = newNode.getData()
        print("Data : ", self.isiData)
    def search(self,item):
        cur = self.head
        found = False
        while cur !=None and not found:
            if cur.getData() == item:
                found = True
            else:
                cur = cur.getNext()
        return found
    def remove(self,item):
        cur = self.head
        prev = self.head
        while cur.next != None or cur.item != item:
            if cur.item == item:
                prev.next = cur.next
                
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length+=1
        self.isiData = newNode.getData()
        print("Data : ", self.isiData)
    def listprint(self, item):
        while (item is not None):
            print(item.data),
            # last = item
            item = item.next
        

x = NodeImplement()
x.add(4)
x.add(1)
x.insertAtBeginning(5)
x.add(2)
x.remove(1)
x.listLength()
x.listprint(x.head)