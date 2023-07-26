# declaration dictionaries
from copy import copy, deepcopy
from collections import defaultdict

MyDict = {'nama' : 'Ahmad', 'umur' : '22', 'asal' : 'Malang'}

# Get Method
print("======Get======")
print(MyDict)
a = MyDict.get('nama') 
print("Data Get nama :",a)

# Pop Method
print("======Pop======")
MyDict['Job'] = "Progamer"
print(MyDict)
print("Item yang dihapus : ",MyDict.pop('Job'))
print(MyDict)

# PopItem Method
print("======PopItem======")
MyDict['Job'] = "Progamer"
print(MyDict)
print("Item yang dihapus : ",MyDict.popitem())
print(MyDict)

# Keys 
print("======Keys======")
print(MyDict.keys())

# Values 
print("======Values======")
print(MyDict.values())

# Items
print("======Items======")
print(MyDict.items())

# # Clear Item 
# print("======Clear======")
# print(MyDict)
# MyDict.clear()
# print(MyDict)

# Update 
print("======Update======")
print(MyDict)
MyDict.update(nama = "Bambang")
print(MyDict)

MyDict.update(alamat= "Lowokwaru")
print(MyDict)

# Copy 
print("======Copy======")
x = MyDict.copy

print(x is MyDict)
print(x == MyDict)
#Dari contoh di atas kita sudah berhasil meng-copy dictionary x ke variabel y. Sekarang membandingkan x dan y dengan operator is akan mengembalikan nilai False.
# Dengan kata lain, kedua dictionary tersebut adalah objek yang berbeda. Namun, key-value pair yang kita copy adalah sama, jadi jika kita membandingkannya dengan operator == akan mengembalikan nilai True.
# Apabila kita ingin membuat replika dari sebuah double dictionary, kita tidak bisa menggunakan metode copy().

# DeepCopy
print("======Deepcopy======")
# digunakan untuk melakukan duplikat pada directori
x = deepcopy(MyDict)
print("MyDict",MyDict)
print("x",x)

# Default dict
print("======Default Dict======")
keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
y = defaultdict(int) # set default value sebagai integer

print(y['z']) # mengakses key z dari dictionary y

# double Dictonary
print("======Double Dict======")
a = {"orang": 
        {
        "nama": "Budi",
        "umur": "20",
        "alamat": "Jalan"
        }
}
print(a["orang"]["nama"])

# From keys
keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys,100)
print(y)