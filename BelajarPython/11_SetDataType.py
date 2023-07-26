# declaration set
print("-----Declaration-----")
# Use List
print("-----DeclarationUseList-----")
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' , 'Sun' ] # list
days_set = set(days_list) # membuat set dari list
print(days_set)
# Use Tupple
print("-----DeclarationUseTupple-----")
fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple) # membuat set dari tuple
print(fruits_set)
print()

# add & remove 
print("-----Add&Remove-----")
myList = {"Ahmad","Kuriniawan", "Bambang"}
print(myList)
print("-----Add Ryan-----")
myList.add("Ryan")
print(myList)
print("-----Remove Ahmad-----")
myList.remove("Ahmad")
print(myList)
print()

# Union and Intersection
print("-----Union&Intersection-----")
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
# Union
print("-----Union-----")
print("Cara 1",s1.union(s2))
# or
print("Cara 2",s1 | s2)
# Intersection 
print("-----Intersection-----")
print("Cara 1",s1.intersection(s2))
# or
print("Cara 2",s1 & s2)
print()

# Difference and Symmetric Difference
print("-----Difference and Symmetric Difference-----")
# Difference
print("-----Difference-----")
print("Cara 1",s1.difference(s2))
# or
print("Cara 2",s1 - s2)
# Symmetric Difference
print("-----Symmetric Difference-----")
print("Cara 1",s1.symmetric_difference(s2))
# or
print("Cara 2",s1 ^ s2)
print()

# Subset and Superset
print("-----Subset and Superset-----")
s1 = {1,2,3,4,5}
s2 = {1,2,3}
s3 = {1,2,6}

print("s2 subset s1 =",s2.issubset(s1))
print("s3 subset s1 =",s3.issubset(s1))
print("s1 superset s2 =", s1.issuperset(s2))
print("s1 superset s3 =", s1.issuperset(s3))
