name = "ICICI"
account_number = 12333
balance = 3433.23
# primitive data types => string , int ,float,bool
# sequence data types => which contains combination of different primitive data types of data
# List ,tuple ,set ,dictionary
# List => it's a combination of different types of data and its mutable type
customer_details = ["ICICI",123333,3433.23]
print(customer_details)
print(type(customer_details))

# Create ,Read ,Update ,delete => CRUD operations
# create =>
customer_details = ["ICICI",123333,3433.23,"IFSC0002323"]

# Read
# Indexing
print(customer_details[0])
print(customer_details[1])
print(customer_details[3])

names = ["chandra","vamsi","naresh","nandu","gopi","nasir","Raghava","sai","swamy"]
print(names[0])
print(names[3])
print(names[6])
print(names[8])
# print(names[9])
print( len(names) )
#
a = names[1]     #[2] # vamsi => [2]
print("name :" , a)
print("character from vamsi" ,a[2])

print("multi indexing  :" ,names[1][2])
# Negative indexing
print(names[-1])
print(names[-9])
print(names[-5])
print(names[4])

print(names[-7])
print(names[2])

company ="microsoft"
print(company[0]) #m
print(company[5]) # s



