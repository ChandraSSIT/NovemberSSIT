# Types of arguments/parameters
# positional arguments
# keyword arguments
# default arguments
# arbitrary arguments
# keyword arbitrary arguments

# positional arguments
# we need to pass the data in same order of the parameters defined

def bankcustomer(name,custid,accountnumber):
    customer = {"name":name,"CustomerId":custid,"AccountNumber":accountnumber}
    print(customer)

# positional arguments
bankcustomer("chandra",4356555,234556666)
bankcustomer(3555555,12223234333,"mohan")

# key word arguments => we will pass the data by  defining key as argument
bankcustomer(accountnumber=3456666,name="nandini",custid=2323233)

print("////////")
# default arguments
def createbankaccount(name,accountnuber,ifsccode="ICICI002"):
    customer ={"name":name,"accountnumber":accountnuber,"IFSCCode":ifsccode}
    print(customer)


createbankaccount("abc",12323233,"ICICI12232")
createbankaccount("john",333333)

# arbitrary arguments
print("arbitrary arguments")
def add(*args):
    sum=0
    for i in args:
       sum+=i
    print("sum of ", args," ",sum)

add(2,3)
add(1)
add(3,4,5,6)
add(6,7,78,3,5,8,7)
add()

# keyword arbitrary arguments
def add(**kwargs):
    print(kwargs)

add(a=2,b=5,c=6,d=8,e=10)
add(a=3, b=5)

def orderofarguments(name,id,*args,ifsc="ICICI033",**kwargs,):
    print(name," ",id," ",ifsc," ",args," ",kwargs)

orderofarguments("chandra",1232,1,2,3,4,ifsc="ICI2333",a=4,b=5)
