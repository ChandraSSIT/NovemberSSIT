# Identifier/Variables
a = 10
b = 20
print(a)
print(a + b)
a = 20
print(a)
name = 'chandra'
balance = 3446.55
isvalid = True

print(name)
# Variable is the one which will store data tempararly in memory
# dynamically typed language
# High level language like english
# syntax , keywords

# Data types
# based on the data which is assigned to variables , python will define some type for those variables
# what are the data types => string , int ,float ,bool

# string
name = 'mohan'  # anything which is between quotes (single or double) will be considered as string
# how to check the type of data/variable
# we have method called type()

print(type(name))
address = "#5-5-566 2nd Cross , ATP"
print(type(address))

# int
account_number = 233393849290887
print(type(account_number))

# float
balance = 3556.67
print(type(balance))

# boolean/bool
is_exists = True
is_not_exists = False

print(type(is_exists))
print(type(is_not_exists))

# standard for variable declaration

# pascal case => it will start with upper case and subsequent words will be in uppercase
# camel case => it will start with lowercase if any other words will start with upper case

# pep8 standards => python programming will follow standards of coding
# variable name should start with alphabets(small letters) ,if there are two words in variable we should
# use _ between words

# string methods
name = "chandra mohan"
print(name.upper())
print(name.lower())
print(name.count('a'))
print(name.capitalize())

bank = "Icic"
print(bank.swapcase())
print(bank.isalpha())
print(bank.isalnum())
account = "3333"
print(account.isdigit())

# string,int,float,bool => Primitive data types/basic data types
