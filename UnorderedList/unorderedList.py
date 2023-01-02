#lokasi item pertama dari daftar harus ditentukan secara eksplisit. 
# Setelah kita tahu di mana item pertama berada, item pertama dapat memberi tahu kita di mana item
# kedua, dan seterusnya. 
# Ingatlah bahwa struktur daftar tertaut hanya memberi kita satu titik masuk, kepala daftar.
# Semua node lain hanya dapat dicapai dengan mengakses node pertama dan kemudian
# mengikuti link berikutnya. Ini berarti bahwa tempat termudah untuk menambahkan simpul
# baru adalah tepat di kepala, atau awal, dari daftar.
from node import NodeObject
class UnorderedList:
    def __init__(self):
        self.head = None #Referensi ke None akan menunjukkan fakta bahwa tidak ada node berikutnya.
    def is_empty(self):
        return self.head ==None
    def add(self,item):
        temp = NodeObject(item)
        # temp = self.data
        temp.setNext(self.head)  #None
        self.head = temp #self.head = self.data
        self.data = temp.setData(item)
        self.isiData = temp.getData()
        print(f" Data: {self.isiData}")
        # print(self.head)
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
myList = UnorderedList()
print("\t=== MENAMBAHKAN DATA ====")
myList.add(40)
myList.add(66)
myList.add(7)
myList.add(9)
myList.add(34)
print()
print("\t=== PENCARIAN DATA ====")
print(f"Apakah ada data yang isinya 40? : {myList.search(40)}")
print(f"Apakah ada data yang isinya 2?  : {myList.search(2)}")
print("\t=== CEK UKURAN PANJANG DATA ====")
print(f"Ukuran data : {myList.size()}")
print()
print("\t=== CEK DATA (KOSONG/TIDAK)====")
print(f"Apakah datanya kosong ? : {myList.is_empty()}")
print()
print("\t=== PENGHAPUSAN DATA ====")
print("Menghapus  9....")
myList.remove(9)
print()
print("\t=== PENCARIAN DATA ====")
print(f"Apakah ada data yang isinya 9? : {myList.search(9)}")
