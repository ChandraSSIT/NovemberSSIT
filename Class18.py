# abstraction,encapsulation
# abstraction => exposing the functionality to outside by hiding the logic
# Encapsulation => hiding the members and member functions/methods => by making them as private
# in python by using __ we can make it as private
class bank:

    def __init__(self, atmpin):
        self.__atmpin = atmpin

    def withdraw(self, amount):
        if self.__atmpin == 3445:
            return amount
        else:
            return "Wrong pin entered"


obj = bank(3445)
print(obj.withdraw(10000))


# polymorphism
# many forms
# defining same function multiple times with different signature
# signature => the number of parameters which we passed to function
# over loading , overriding

from multipledispatch import dispatch
class calculator:
    def addition(self,a,b):
        return a+b

    def addition(self,a,b,c):
        return a+b+c

    def addition(self,a,b,c,d):
        return a+b+c+d

    # we can solve overloading problem by using *args
    def addition(self,*args):
       sum =0
       for i in args:
           sum +=i

    @dispatch(int, int)
    def sub(self,a, b):
        return a - b

    @dispatch(int, int, int)
    def sub(self,a, b, c):
        return a - b - c


# over loading => defining same function with different signature in same class
# is python supports over loading => No , it will not support => it will take the last function from top
# to bottom
# MRO => method resolution order
obj = calculator()
print(obj.addition(2,3,5))
obj.sub(6,5)
obj.sub(7,6,5)



def add(*args,**kwargs):
    sum =0
    for i in args:
        sum += i


add(2,3)
add(3,4,5)
add(5,6,7,7)
add(a=3,b=5)

