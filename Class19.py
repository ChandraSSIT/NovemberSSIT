# Inheritance => Parent and child relationship
# where child can access all the functionality from parent and we can extend the functionality as well as
# we can modify existing functionality
# Grand father
# Father
# children

class A:
    Name ="Python"
    def M1(self):
        print("From A method M1")
    def M3(self):
        print("From A method M3")

    def house(self):
        print("House from parent ")

class B(A):
    def M2(self):
        print("From B method M2")
    def M3(self):
        print("From B Method M3")



class C(B):
    def house(self):
        print("I sold the house")

class D(C):
    pass
# Over-riding  => defining same function in child class , it will override the parent functionality in child

obj = B()
print(obj.Name)
obj.M1()
obj.M2()
obj.M3()
obj.house()

obj = C()
obj.M2()
obj.house()
obj.M3()
# Single level,multilevel,multiple
# Single level => Parent to child
# Multi level => parent => child => grand child =>

# Multiple Inheritance

print("//////Multiple Inheritance //////")
class father:
    def get_lands(self):
        print("My father earned lands")

class mother:
    def get_lands(self):
        print("My mother earned lands")

    def get_house(self):
        print("My mother earned house")

    def get_car(self):
        print("My mother car")

class spouse:
    def get_car(self):
        print("My spouse car")

class child(father,mother,spouse):
    def get_lands(self):
        print("My own lands")

obj = child()
obj.get_lands()
obj.get_house()
obj.get_car()
# MRO => method resolution order

print("////////////")











