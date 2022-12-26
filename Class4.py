# slicing
# taking out as part of data based on start index , end index ,step size

names = ["chandra", "vamsi", "naresh", "nandu", "gopi", "nasir", "Raghava", "sai", "swamy"]

# start index => start point of slicing
# end index => end point of slicing => we need to consider end index as endpoint value - 1 , for example
# if endpoint/end index is 3 we need to consider till 2(i.e 3-1)
print(names[0:4])
print(names[1:7])
print(names[4:9])
print(names[11:14])  # even if we provide start index out of range of data it will not give any exception
# it will handle by the python and provide us as empty list
print(names[:])  # if we wont provide start index it will consider as 0 , if we wont provide end index it will
# consider as total elements/till last index

# step size
print(names[0:4:2])

print(names[0:4:2])  # chandra ,naresh
print(names[0:4:3])  # chandra,nandu

print(names[0:5:2])  # chandra,naresh,gopi
print(names[0:5:3])  # chandra ,nandu
print(names[0:5:4])  # chandra,gopi
print(names[0:5:5])  # chandra

print(names[2:7:2])  # naresh,gopi,raghava
print(names[2:7:3])  # naresh,nasir
print(names[2:7:4])  # naresh,raghava

print(names[2:2])  # [2,1]
print(names[1::2])

print(names[0:3])
print(names[-9:-6:2])

print(names[4:0:-1])
print(names[-2:-6:-1])
print(names[-2:-6:-2])

print(names[::])
print(names[::-1])

str1 = "hello"
print(str1[1])
# reverse string with slicing
print(str1[::-1])

# List
# Crud
# Create

# Read

# update
# updating existing data , we can insert new data
names[0] = 'mohan'
print(names)
names[0:1] = 'mohan', 'nanda'
print(names)

# we have two methods to add data => append,extend
# append => we can add single data
# extend => we can add multiple data
print(names)
names.append("IDBI")
names.append(["ICICI", "HDFC"])
print(names)
# names.extend("SBI")
names.extend(["SBI", "IDFC"])
print(names)

# delete
del names[0]
print(names)
del names[0:3]
print(names)

# del names # it will delete completely
# print(names)
names.clear()  # it will clear the items ,but object will persist(exists)
print(names)

# crud => list is mutable type , it is changeable ,internally the memory will also reuse

# string => is immutable or mutable  => immutable
str1 ="chandra"
str1="mohan"
print(str1)

# operations
names = ["chandra", "vamsi", "naresh", "nandu", "gopi", "nasir", "Raghava", "sai", "swamy","chandra"]
print(names.index("vamsi"))
names.remove("chandra")
print(names)
names.pop()
print(names)
names.pop()
print(names)


