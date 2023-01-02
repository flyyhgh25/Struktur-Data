# batas recurrsion yaitu 1000 untuk merubahnya pakai library sys
from sys import getrecursionlimit
from sys import setrecursionlimit
# cetak 10-1
def cetak(n):
    print(n)
    if(n>1):
        cetak(n-1)
# cetak(1000)
setrecursionlimit(3000)
# print(getrecursionlimit())
# cetak 1-10
def cetak(n):
    if(n<=10):
        print(n)
        n+=1
        cetak(n)
# cetak(1)

# (2)
# faktorial
def hitungFaktorial(n):
    if n==1:
        return 1
    else:
        return (n*hitungFaktorial(n-1)) #7*6*5*4*3*2*1
# print(hitungFaktorial(7))

# (3)
# fibbonanci
def hitungFibonacci(n):
    if n<=1:
        return n
    else:
        return(hitungFibonacci(n-1)+hitungFibonacci(n-2))

# for i in range(8):
#     print(hitungFibonacci(i))

# (4) binary number basis(0,1)
def binary(num):
    if num>0:
        # y = num//2
        # print(y)
        binary(num//2)  #melakukan pembulan bilangan dibagi 2
        print(num%2,end='')
# binary(50)

# (5) oktal number basis 8 (0..7)
def oktal(num):
    if(num>0):
        oktal(num//8)
        print(oktal%8,end='')

# (6) Hexa number basis 16 (0...F)
hexta_tabel = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def hexa(num):
    if num>0:
        hexa(num//16)+hexta_tabel[num%16]
        return hexa(num//16)+hexta_tabel[num%16]
    else:
        return ""
# print(hexa(26))

# (7) Menara hanoi
def MenaraHanoi(n,asal,perantara,tujuan):
    if(n==1):
        print("Memindahkan disk 1 dari asal",asal,'ke perantara',perantara)
        return
    MenaraHanoi(n-1,asal,tujuan,perantara)
    print("Memindahkan disk",n,'Dari asal',asal,'ke perantara',perantara)
    MenaraHanoi(n-1,tujuan,perantara,asal)

n = 4
MenaraHanoi(n,'A','B','C')
