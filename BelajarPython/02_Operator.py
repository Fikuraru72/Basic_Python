
# Arimatic opperators
print("=====Arimatic Operators======")
x = 50
print("===+===")
print(x + 20)

print("===/===")
print(x/5)

print("===-===")
print(x-10)

print("===*===")
print(x*5)

print("===%===")
print(x%3)

print("===**===")
y = 4
print(x ** y)

print("===//===")
y = 3
print(x // y)

# Assigment Operators
print("=====Assigment Operators======")
x += 20
print("=== += ===")
print(x)
print("=== -= ===")
x -= 40
print(x)
print("=== *= ===")
x *= 5
print(x)
print("=== %= ===")
x %= 2
print(x)
print("=== = ===")
x = 50
print(x)
print("=== //=  ===")
x //= 4
print(x)
print("=== **= ===")
x **= 5
print(x)

# Comparison operators
print("=====Assigment Operators======")
print("=== == ===")
x = 50 
print(x == 30)

print("=== < ===")
x = 50 
print(x < 30)

print("=== > ===")
x = 50 
print(x > 20)

print("=== <= ===")
x = 50 
print(x <= 20)

print("=== >= ===")
x = 50 
print(x >= 50)

print("=== != ===")
x = 50 
print(x != 30)

# is operator
print("=====is operator======")
a = 10
b = 10
c = 20
print('nilai a =', a, ', id =', hex(id(a)))
print('nilai b =', b, ', id =', hex(id(b)))
print('nilai c =', c, ', id =', hex(id(c)))
print('======================')
hasil = a is b
print('a is b =', hasil)
hasil = a is c
print('a is c =', hasil)

# in operator 
print("=====in operator======")
data1 = "123-321-111"
data2 = "3131-1232-2122"

print(data1)
print(data2)
print('======================')
hasil = '111' in data1
print('111 in data1 =', hasil )
hasil = '111' in data2
print('111 in data2 =', hasil )

# logical Operation
print("=====logical Operationr======")
x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)
