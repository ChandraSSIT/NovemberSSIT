a = 2
b = 3
a + b
x = 5
y = 6
x + y
d = 6
f = 7
d + f
l1 = []
# [{"name":"john","name":"test"}]
dict1 = {"name": "john", "address": "ATP"}
l1.append(dict1)
dict1 = {"name": "kelly"}
l1.append(dict1)
dict1 = {"name": "nanda"}
l1.append(dict1)
dict1 = {"name": "python"}
l1.append(dict1)


# functions
# it's a piece of code which can be reusable
# how to define a function => we need keyword called def
def myname1():
    print("My name is Python")


# how to call this function
myname1()
myname1()


# arguments/parameters
def myname(name):
    print("Fullname :", name)


myname("chandra")
myname("python")


def add(a, b):
    print(a + b)


add(5, 6)
add(7, 8)
add(9, 8)
aadhars = []


def aadhardetails(name, aadharnum, address, mobile, dob):
    aadharcard = {"number": aadharnum, "name": name, "Address": address, "Phone": mobile, "DateOfBirth": dob}
    aadhars.append(aadharcard)


aadhardetails("chandra", 2322332, "ATP", 956656556, '23/23/1987')
aadhardetails("john", 12321311231, "ATP", 636565, '23/23/1987')
print(aadhars)
print("///////////")


def getaadhardetails(aadharnumber):
    for item in aadhars:
        if item["number"] == aadharnumber:
            return item


print(getaadhardetails(2322332))


# return
# pass,break,continue

def add(a, b):
    return a + b


print(add(8, 9))
print(add(6, 7))

print("////////")


def emptyreturn():
    for i in range(10):
        if i == 5:
            break
        print(i)
        # for i in range(20,30):
    #     print(i)
    print("After loop execution")


print(emptyreturn())

# the default return type of function is None

# difference between break and return => break will stop the current iteration
# return will completely go out of the function

# pass, break,continue,return

# print prime numbers from 1 to 30

def iseven(num):
    if num %2 == 0:
        return True
    else:
        return False

for i in range(1,31):
    if iseven(i):
        print(i,end=" ")

# arguments/parameters