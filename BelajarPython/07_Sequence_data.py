# Iterator===================
# List
print("=====List Iterator=====")
list1 = [11,22,33,44] * 2
print(list1)

# Tuple
print("=====Tupel Iterator=====")
tup1 = (1,2,3)
print(tup1 * 2)

# String
print("=====String Iterator=====")
str2 = 'hello'
print(str2 * 3)

# Range 
print("=====Range Iterator=====")
ran = list(range(5)) * 3
print(ran)

# Count Method=====================
# List
print("=====List Count Method=====")
list1 = [11,11,11,22,33,44] 
print(list1.count(11))

# Tuple
print("=====Tupel Count Method=====")
tup1 = (11,11,11,22,33,44) 
print(tup1.count(11))

# String
print("=====String Count Method=====")
str1 = 'hello world'
print(str1.count('l'))

# Range 
print("=====Range Count Method=====")
ran = range(0,5,1)
print(len(ran))
print(ran.count(2))

# Linking=================
# List
print("=====List Linking=====")
list1 = [11,22,33,44]
list2 = [55,66]
print(list1)
print(list1 + list2)

# Tuple
print("=====Tupel Linking=====")
tup1 = (1,2,3)
tup2 = (4,5,6)
print(tup1 + tup2)              

# String
print("=====String Linking=====")
str1 = 'hello'
str2 = 'world'
print(str1 + str2)

# Range 
print("=====Range Linking=====")
print(list(range(10)) + list(range(10,20)))
print(tuple(range(10)) + tuple(range(10,20)))

