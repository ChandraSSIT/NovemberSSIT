# Inner function

def get_my_details(name):
    a = 20
    print("My details will be available")

    def get_my_bank_details():
        print("My Bank details are ICCIC :", name)

    return get_my_bank_details


def add(a, b):
    return a + b


c = add(3, 4)
print(c)

funct1 = get_my_details("Python")

funct1()


# closure function


# Decorators,iterators,generators
# Decorators => extending the functionality of a function without modifying
# In python every thing is an object, so we can pass function as a parameter to other function
def calculator(fun1):
    print("I am from decorator ")

    def inner1(a,b):
        print("I am from Inner function")
        if a>b:
          result = fun1(a,b)
          print("result from Inner function ", result)
        else:
            print("a is lesser than b")

    return inner1


@calculator
def sub(a, b):
    return a - b


sub(5, 6)
