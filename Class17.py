# Instance methods,static methods,class methods
class bank:

    branch="BLR"
    def __init__(self, name):
        self.bank_name = name

    def get_bank_details(self,ifssc):
        temp = self.get_bank_deposits()
        print("Bank :", self.bank_name,self.branch,temp)

    def get_bank_deposits(self):
        return 1000000

    @staticmethod
    def get_my_branch_location(branch):
        print("my brank location ",branch)

    @classmethod
    def get_bank_customers(cls,customers):
        print(cls.branch)
        print("bank has  customers",customers)

obj = bank("HDFC")
# instance method
# instance method => accessing methods/functions with class object/instance
obj.get_bank_details("ICICI122")
print(bank.branch)
# static method => the method which we can access without instance of a class
# but inside this method we can not access class variables,instance variables ,instance methods
bank.get_my_branch_location("ATP")

# Class methods => a method which can be accessed without object but inside class method we can access
# class variables
bank.get_bank_customers(100000)



