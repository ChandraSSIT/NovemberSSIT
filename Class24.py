# Date time functions
from datetime import date,datetime,timezone

print("///date////////")
print(date.today())
print(date.today().year)
print(date.today().day)
print(date.today().month)
print(date.fromtimestamp(1670811024))
print("////date time /////")
print(datetime.today())
print(datetime.today().year)
print(datetime.today().time())
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().microsecond)
print("///// time zone info///")
print(timezone.utc)
print(timezone.min)

print("//////Regular expression////////")
# Regular expression
import re

str1="Sample of data fromdata program Sample of data from program 10.20.180.202 12.24.23.124"
print(str1.count("data"))
l1 = str1.split(" ")
print(l1)
dict1= {}
for i in l1:
    if i in dict1:
        dict1[i] = dict1[i]+1
    else:
        dict1[i] = 1

print(dict1)

# 10.20.202.198

pattern = re.compile(r"\bdata\b")
if re.search(pattern,str1):
    print("Matched")
print(re.findall(pattern,str1))

ippattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
print(re.findall(ippattern,str1))

emailpattern = re.compile(r"^([a-z]|[0-9]|\-|\_|\+|\.)+\@([a-z]|[0-9]){2,}\.[a-z]{2,}(\.[a-z]{2,})?$")

# Variables,Datatypes(string,int,float,bool,list,tuple,set,dictionary),datatypeconversions,
# conditional statement,loops , operators,break,pass,contintue, functions , different types of arguments,
# return, decorator,iterator,generator
# oops
# datetime,regex,file operation,exception handling
