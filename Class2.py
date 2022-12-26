 # Data type conversion
# converting from one data type to another datatype
# Implicit data type conversion
# Explicit data type conversion

# Implicit data type conversion => converting from one data type to another data
# type automatically by python interpreter
# it will convert to higher datatype
initial_amount = 2000  # int
intrest = 233.44   # float

total = initial_amount+ intrest
print(total)
print("total datatype :",type(total))

with_draw = int(total) #explicit data type conversion
# Explicit data type conversion => converting from one data type to another by mentioning target data type
print(with_draw)
print(type(with_draw))

pincode = 515001
location ="#23 2nd floor , Ramnagar,ATP"
street ="100 feet road"
address = location + street + str(pincode)
print(address)
print(type(address))

amount = "5666"
balance = 455
total = balance + int(amount) # 4555666
print(total)
# comments => which will give the explanation/information about the
# lines of code , for that we have to
# user #
'''
Below I am writing code about 
data type conversion
'''

