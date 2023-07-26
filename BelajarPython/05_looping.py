# for loop range
from ast import For

for i in range(5):
    print("Welcome")
    
for o in range(0,5,2):
    print("nice")
    
# for loop list
number = [22, 33, 44, 55]
for i in number:
    print('i =',i)

# for loop continue
nama = ["ahmad", "nurul", "Kurniawan", "Bambang"]
for i in nama :
    if i == "nurul" :
        continue
    print("nama : ",i)
    
print(10*"=")

# for loop break
for x in nama :
    if x == "Kurniawan" :
        break
    print("nama : ",x)

# for loop else
for a in range(0,10,1):
    print(a)
else :
    print("Berhitung Selesai")

# Nested for loop
namaDepan = ["Bambang", "Adam", "Galang", "Ucup"]
namaBelakang = ["Wibowo", "Widodo", "Pratama", "Muncup"]

for x in namaDepan :
    for y in namaBelakang:
        print(x,y)
else :
    print(15*"=")

# for loop list by index
for x in range(len(namaDepan)):
    print(namaDepan[x],namaBelakang[x])
    
# while Loop
print(20*"=")
i = 0
while i < 10 :
    print(i)
    i += 1

print(20*"=")

# while loop break
x = 0
while x < 10 : 
    print(x)
    if x == 7 :
        break
    x += 1
    
print(20*"=")

# while loop continue
z = 0
while z < 10 : 
    z += 1
    if z == 3 :
        continue
    print(z)
    
    
print(20*"=")


# while loop else
s = 0
while s < 10 : 
    print(s)
    s += 1
else : 
    print("Hitung Selesai")
