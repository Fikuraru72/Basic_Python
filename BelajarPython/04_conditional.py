# if statement
age = int(input("Masukan Umur = "))
print("Umur =", age)
if age < 20 :
    print("diskon 20%")
print("Thanks")

# Pass Keyword
print('===============')
num = int(input("Masukan Num = "))
if num % 2 == 0:
    print('Nomor Genap')
if num % 3 == 0:
    pass

# if-else statement
print('=============')
score = int(input("Masukan Score = "))
if score > 80 :
    print("Anda Lulus")
else :
    print("Anda Gagal")

# elif statement
print('=============')
score = int(input("Masukan Score = "))
if score > 80 :
    print("Anda Lulus")
elif score < 80 and score > 75 :
    print("Sedikit Lagi")
else :
    print("Coba Lagi")
    
# nested codition
print('=============')
num = int(input("Masukan Data = "))
if num < 0:
    print(num, 'adalah bilangan negatif. ')
else:
    print(num, 'adalah bukan bilangan negatif ')
    if num % 2 == 0:
        print(num, 'adalah bilangan genap')
    else:
        print(num, 'adalah bilangan ganjil')

