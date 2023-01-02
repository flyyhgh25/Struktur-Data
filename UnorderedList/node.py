class NodeObject:
    def __init__(self,data):
        self.data = data
        self.next = None
  
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self,new_data):  
        self.data = new_data
    
    def setNext(self,new_nextData):
        self.next = new_nextData
temp = NodeObject(93)
# temp.getData()