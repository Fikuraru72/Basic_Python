# List string
from tracemalloc import start


print("=====Str=====" )
StrList = ["ahmad", "budi", "Kurniawan"]
print(StrList)

# List Int
print("=====Int=====" )
IntList = [30,50,90]
print(IntList)

# Random List 
print("=====Rdm=====" )
RdmList = ["banana", 50, "Watermellon", 50]
print(RdmList)

# List Legnht
print("=====List Leght=====" )
LghtList = ["Left", 40, "Right", 50, "Center"]
print(LghtList)
print("Lenght = ",len(LghtList))

# List Type
print("=====List Type=====" )
List1 = ["ahmad", "budi", "Kurniawan"]
print(List1, "Type =", type(List1))
List2 = [30,50,90]
print(List2, "Type =", type(List2))

print('Halo nama saya ' + str(20) * 3)
print( 30 * 2 + 10 - (21  // 5) )

# List Adition
print("=====List Adition=====" )
person1 = ['David Doe', 20,1,180.0,100.0]
person2 = ['John Smith', 25,1,170.0,70.0]

person_list = person1 + person2
print(person_list)

# List Append 
print("=====List Append=====" )
a_list = ['a', 'b', 'c', 'd', 'e']
a_list.append('f')
print(a_list)   

# List Extend
print("=====List Extend=====" )
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1,2,3,4,5]
list1.extend(list2)

print(list1)
list1.extend('f')
print(list1)

# List deletion
# del (Mwnghapus list harus dengan index)
print("=====List Del=====" )
n_list = [11,22,33,44,55,66]
print(n_list) 

del n_list[3] 
print(n_list)

# pop (menghapus list dengan index, apabila tidak diberi akan menghapu list terkhir)
print("=====List Pop=====" )
n_list = [10,20,30]
print(n_list) # print seluruh items

n = n_list.pop()
print('n = ',n)
print('n_list =',n_list)

# remove (menghapus list tanpa diketahui index nya)
print("=====List Remove=====" )
n_list = [11,22,33,44,55,66]
print(n_list)

n_list.remove(44)
print(n_list)

# List Slicing
print("=====List Slicing=====" )
the_list = ['a', 'b', 'c', 'd', 'e']
print(the_list[1:3]) 
print(the_list[-2:])
print(the_list[:-2])
print(the_list[:-2])
print(the_list[1::-1])

# List in Operator
print("=====List in Operator=====" )
num_list = [10, 20, 30, 40, 50, 60]
print("70 in num_list =",70 in num_list)
print("20 in num_list =",20 in num_list)
print("40 not in num_list =",40 not in num_list)

# Tuple 
colour = ("Red", "Blue", "Green", "Yellow")
print(colour)

''' 
    - Tupple tidak dapat diubah
    - Tuple memiliki kelebihan yaitu lebih cepat untuk diproses dibandingkan dengan list
'''