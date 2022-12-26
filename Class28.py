import random
import string

print(random.randint(0, 100))
s= 10
temp = random.choices(string.ascii_lowercase+string.ascii_uppercase + string.digits, k = s)
print(temp)
output  = ''.join(temp)
print(output)

# Pytest => framework
# the file name should be start with test_
# the method name should start with test
# API testing
# by using Post man
# Get,Post,Put,Patch
# Automation of API Testing
# fixture,mark,parametrize,confest

# UI testing

# Rest API => stateless API ,it will not keep cookies or history of API call which we made , every time it
# will consider as fresh call
# it supports different protocols => https, TCP ,named pipes
# its supports different types of data =>  Json,XML,Text

# web services => this supports only http protocol
# this supports only XML

# to test API manually => we need Postman
# to do automation => Pytest,Python,Requests library from python
# API => get,post,put,patch,delete
# Authorization => Bearer token
# what are the status codes which we will get from API =>
# 200 series => Success responses
# 400 series => Client error
# 500 series => Server error
# convert response into json and access the data based on key then assert
# Pytest => how to write te cases =>
# test file name should start with test_
# the method name should start with test
# Pytest => mark,parametrise,fixture,xskip,xfail,
# pytest -v
# pytest filename -v
# pytest -k testmethodname -v
# pytest -m markname -v


