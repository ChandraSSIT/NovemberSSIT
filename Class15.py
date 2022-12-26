x = 10
name = "Python"


# list,tuple,set,dictionary
# reusable code => functions
# OOPS => it will be combination of member variables ,functions
# Memory re-usability ,scalability

# class,object,abstraction,encapsulation,polymorphism,Inheritance
# Class => class is a container which contains members and member functions
# how to create class
class bank:
    bank_name = "RBI"
    address = "ATP"



    def get_my_bank_details(self,branchcode):
        self.ifsccode = "ICIC002"
        print("My bank details")

    def add(self):
        pass


#  object => instance of a class
bank_obj = bank()
print(bank_obj.bank_name)
print(bank_obj.address)
bank_obj.get_my_bank_details("TP")
bank_obj.ifsccode

# self => it represents current instance of a class , with self we can access the variables and functions
# inside a class

# abstraction => exposing the details to outside without showing logic/implementation behind

class atmMachine:

    def __init__(self,atmcard,atmpin):
        self.CardNo = atmcard
        self.PIN = atmpin

    def withdraw(self,money):
        balance = 20000
        if self.atmcard == 12232323 and self.atmpin == 1234 and money <= balance :
            return money


atmobj = atmMachine(122333,1234)
atmobj.withdraw(10000)
# withdraw => is the function works here as abstraction

