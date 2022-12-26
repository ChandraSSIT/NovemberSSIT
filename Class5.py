# tuple
# it's a constant and immutable (not changeable)
# list = []
# tuple = () or if we seperated data with , => that also will be considered as tuple 1,
# tuple is read only
t1 = (1, 2, 3, 4, 3, "chandra")
print(type(t1))
t2 = 2,
print(type(t2))
# CRUD
# Create
t1 = (1, 2, 3, 4, "icici", "hdfc", "sbi")
# Read
# same as list => Indexing,Slicing
print(t1[0])
print(t1[3])
print(t1[2:4])
print(t1[-1])

# update => tuple will not support update , it's not changeable/immutable
# t1[0] = 20 #TypeError: 'tuple' object does not support item assignment
# delete
# it will not support individual item deletion /it will support complete object deletion
# del t1[0] # 'tuple' object doesn't support item deletion
del t1
# print(t1)


# set
l1 = [1, 2, 1, 2, 3, 2, 45, 23, 67, 23]
print(l1)
# set will remove duplicate elements in side set
# syntax => {}
s1 = {1, 2, 1, 2, 3, 2, 45, 23, 67, 23}
print(s1)
# CRUD
# Read
# it will not support indexing => because as it will not allow duplicates it will change elements positions
# while removing duplicate records
for i in s1:
    print(i, end=" ")

print("")
# update
# we can not update existing elements , but we can add new elements
s1.add(100)
s1.update([200, 300])
print(s1)

# delete
s1.remove(200)
s1.pop()
print(s1)

# type conversion
l1 = [1,2,2,3,3,4,5,6]
t1 = (3,4,6,7)
print(set(l1))
print(list(t1))

# set has some different functionalities
s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 40, 50, 60}
s3 = s1.union(s2)
print("Union ", s3)
s4 = s1.intersection(s2)
print("intersection ",s4)
s5 = s1.difference(s2)
print("difference of s1",s5)
s6 = s2.difference(s1)
print("difference of s2", s6)

s7 = s1.symmetric_difference(s2)
print("Symmetric differe" ,s7)

s1.difference_update(s2)
print("S1 after update ",s1)







