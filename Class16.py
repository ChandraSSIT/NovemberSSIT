# Magic /special methods
# these methods are inbuilt methods which we can override

class bank:
    bank_name1 = "RBI"
    def __init__(self,bankname,ifsccode):
        self.bank_name=bankname
        self.IFSCcode = ifsccode

    def get_bank_details(self):
        print(self.bank_name)
    def get_address(self,branchcode):
        pass


obj = bank("icici","ifsc333")
obj.get_bank_details()
obj.bank_name
obj.get_address("icici")

# __init__ => initialization => constructor => constructing of object => this will be called automatically
# while creating object
# default constructor => without any parameter

# obj1 = bank("hdfc")
# obj1.get_bank_details()
#
# obj2 = bank("sbi")
# obj2.get_bank_details()


# Instance methods,class methods ,static methods
# Instance methods => the methods which are accessible with object




