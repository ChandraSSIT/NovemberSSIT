# dictionary
# [],(),{} ,{}
l1 =["chandra","icici",233232,232333]
# key and value pair
dict1 = {"accountholdername":"chandra","accountno":1233333,"balance":2334,"bankname":"ICICI"}
print(type(dict1))
# in dictionary keys are immutable , value can be changeable

# CRUD
# Create
dict1 = {"accountholdername":"chandra","accountno":1233333,"balance":2334,"bankname":"ICICI"}
dict2 ={1:"nandini",2:"saicharitha",3:"swamy",4:"nasir",4:"chandra"}
# in keys we can use numbers,string ,tuple
# same key duplicate keys can not be used
print(dict1)
print(dict2)

# Read
# we can read based on key
print(dict1["accountholdername"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
for i in dict1:
    print(dict1[i])

# print(dict1["address"]) # we will get key error if key is not there

# update
dict1["accountholdername"] = "nandini"
print(dict1)
dict1["accountholdername"]="swamy"
dict1["address"] ="ATP"
print(dict1)

# delete
del dict1["accountholdername"]
print(dict1)
del dict1

# [],{"a":1},{2,},()


