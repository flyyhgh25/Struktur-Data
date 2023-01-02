class Node:
    def __init__(self,item):
        self.next = None
        self.prev = None
        self.nodeValue =item

class DNode:
    def __init__(self):
        self.front = None
        self.tail = None
      
    # menyisipkan node di belakang s
    def append(self,newItem):
        newNode = Node(newItem)
        newNode.next = self.front
        if self.front is not None:
            self.front.prev = newNode
        self.front = newNode

     #menyisipkan node di depan 
    def prepend(self, newElement):
        newNode = Node(newElement)
        if(self.front == None):
            self.front = newNode.next
            return
        else:
            temp = self.front
            while(temp.next != None):
                temp = temp.next
            temp.next= newNode
            newNode.prev = temp
       

    # Menyisipkan node di list tertentu
    def insert(self, prev, item):
        if prev is None:
            return
        NewNode = Node(item)
        NewNode.next = prev.next
        prev.next = NewNode
        NewNode.prev = prev
        if NewNode.next is not None:
            NewNode.next.prev = NewNode
    
    # Mengeprint list   
    def listprint(self, item):
        while (item is not None):
            print(item.nodeValue),
            last = item
            item = item.next
        
    
    # delete first
    def pop_first(self):
        if(self.front == None):    
            return;    
        else:       
            if(self.front != self.tail):    
                self.front = self.front.next;    
                self.front.prev = None;    
            else:    
                self.front = self.tail = None;    
    
    # DELETE LAST
    def pop(self, item):
            if(self.front != None):
                if(self.front.next == None):
                    self.front = None
                else:
                    temp = self.front
                    while(temp.next != None):
                        # temp = temp.next
                        # lastNode = temp.next
                        temp.next = None
                        lastNode = None
    def remove(self, x):
        if self.front is None:
            print("Tidak ada element yang mau dihapus")
            return 
        if self.front.next is None:
            if self.front.nodeValue == x:
                self.front = None
            else:
                print("Item tidak ditemukan")
            return 
        if self.front.nodeValue == x:
            self.front = self.front.next
            self.front.prev = None
            return
        n = self.front
        while n.next is not None:
            if n.nodeValue == x:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.nodeValue== x:
                n.prev.next = None
            else:
                print("Element tidak ditemukan")
    def reversList(self):
        temp = None
        current = self.front
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.front = temp.prev
   
dNode= DNode()
print("Manambahkan List (APPEND)")
dNode.append("Merah")
dNode.append("Kuning")
dNode.append("Biru")
dNode.listprint(dNode.front)
print("Manambahkan List (PREPEND)")
dNode.prepend('Ungu')
dNode.listprint(dNode.front)
print("Manambahkan List (INSERT)")
dNode.insert(dNode.front.next,"Hijau")
dNode.listprint(dNode.front)
# Menghapus Node
print()
dNode.pop_first()
dNode.listprint(dNode.front)
print()
# dNode.pop_tail(dNode.front)
dNode.remove("Hijau")
dNode.listprint(dNode.front)
print()
dNode.reversList()
dNode.listprint(dNode.front)