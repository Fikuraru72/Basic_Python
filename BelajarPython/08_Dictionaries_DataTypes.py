import json

# Declaration dictionaries
mydict = {
    "Nama" : "Ahmad",
    "Umur" : "23",
    "Asal" : "Malang"
}
print(mydict)

# Modify key
mydict["Asal"] = "Mojokerto"
print(mydict)

# Add New Key
mydict["Pekerjaan"] = "UI/UX Designer"
print(mydict)

#  deleting items 
del mydict["Pekerjaan"]
print(mydict)

# Len function 
print("lenght mydict :",len(mydict))

# in opperator
print("Nama di mydict :",'Nama' in mydict )
print("Malang di mydict :",'Malang' in mydict )

# operator in digunakan untuk mengecek sebuah key bukan data

# json method
# Read Json data (Loads())
mydict2 = '{"Nama" : "Ahmad", "Umur" : "23", "Asal" : "Malang"}'
    
json_data = json.loads(mydict2)
print("Tipe :",type(json_data))
print(json_data["Nama"])
print(json_data["Umur"])
print(json_data["Asal"])

# Read Json data (dumps())
my_json = json.dumps(mydict)
print("Tipe :",type(my_json) )
print(my_json)

