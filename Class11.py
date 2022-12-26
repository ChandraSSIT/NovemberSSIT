def add(a, b):
    return a + b


def add(a, b, c):
    return a + b + c


def add(*args):
    sum1 = 0
    for i in args:
        sum1 += i
    print(sum1)


dict1 = {"name": "John", "name": "kelly"}
print(dict1)
add(2, 3, 8)
add(3, 4, 5, 8)
add(3, 4)
# MRO =>method resolution order
# is there any workaround to solve this problem

from multipledispatch import dispatch


@dispatch(int, int)
def sub(a, b):
    return a - b


@dispatch(int, int, int)
def sub(a, b, c):
    return a - b - c


print(sub(5, 4))
print(sub(8, 7, 6))

# Global variable
# Local variable
# Global => declaring a variable in the module level which can access across the module as well as if
# we import module outside we can access there too
# local scope => defining a variable inside a function which can not be accessed outside
x = 20

z = 0


def samplevariablescope():
    # local variable
    y = 10
    print(x)
    print(y)
    # to make local variable to access outside we need to use global keyword
    global z
    z = 70
    print("Local Z:",z)

samplevariablescope()
print("Z value for global : ",z)
print(x)
