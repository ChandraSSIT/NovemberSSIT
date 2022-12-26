# Operators
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators

# Arithmetic operators :
# + , - ,* ,%,/,**,//

a = 2 + 3
print("+ :", a)
b = 5 - 4
print("- :", b)
c = 3 * 4
print("* :", c)
d = 5 % 2  # modulation => it will take remainder from division
print("% :", d)
e = 4 / 2  # division
print("/ :", e)
f = 2 ** 4  # exponential power of => 2powerof => 2*2*2*2
print("** :", f)
g = 2345 // 10  # floor division
print("g :", g)

# Assignment operators
# = ,+=,-=,*= , /=,%=,//=,**=
a = 5
a = a + 3
a += 3  # its same as a = a+3
print(a)

a -= 1  # its same as a = a-1
a *= 2  # its same as a = a*2
a /= 2  # its same as a = a/2
a %= 2  # its same as a = a%2
a **= 3  # its same as a = a**3
a //= 3  # its same as a = a//3

# Comparison operators
# will always give True or False
x = 6
print("== :", x == 5)  # False
print("!= :", x != 5)  # True
print("> :", x > 10)  # False
print("< :", x < 10)  # True
print(">= :", x >= 5)  # True
print("<= :", x <= 10)  # True

# Logical operators
# and, or, not
# and  => both conditions should match then only it will give True
x > 4 and x < 10  # True
x > 4 and x < 6  # False
x > 7 and x < 8  # False
x > 7 and x < 5  # False

# True and True => True
# True and False => False
# False and True => False
# False and False => False

x=6
# or
# any one condition matches it will return True
x > 4 or x < 10  # True
x > 4 or x < 6  # True
x > 7 or x < 8  # Tru
x > 7 or x < 5  # False

# not
not(x > 4 or x < 10) # False
not(x > 7 or x < 5 ) # True

# Membership operator
# this has in , not in
l1=[1,2,3,4]
dict1={"a":1,"b":2}

print("in :" ,1 in l1)
print("in dict :","a" in dict1)
print("in dict1" , "a" in dict1.keys())
print("in dict1" , 1 in dict1.values())
print("in dict1" , 11 not in dict1.values())

# Identity operator
x = 5
y = 6
z=x
print(x is z)
print(x is not z)
