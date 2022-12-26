# Condition statements ,Loop statements
x = 8
if x == 6:
    print("both values are equal")
elif x > 7:
    print("greater than 7")
elif x > 4:
    print("greater than 5")
else:
    print("both values are not same")

# loops
# for ,while
# for => it will iterate through records
l1 = [1, 2, 3, 4]
for i in l1:
    print(i)

# range => i=0 , i <5 ,i+2
# range => start index , end index, step size

for i in range(0, 5, 1):
    print(i, end=" ")

print("")
# while
# it will depend on the condition =>until condition is false it will loop through
i = 1
while i <= 10:
    print(i,end=" ")
    i = i + 1  # Arithmetic operator
    # i += 1  # Assignment operator

print("")
i=10
while i >=1:
    print(i,end=" ")
    i -=1

print("")

# pass,break,continue
x= 5
if x==5:
   pass

# pass => it is used to keep unimplemented method/code block , to avoid compile errors
# break => it will stop the iteration and execution comes out of the loop
l1= ["icici","hdfc","sbi","indian","union"]

for i in l1:
    if i == "sbi":
      print("I am inside sbi atm")
      break
    print(i)


print("outside loop")

# continue
l2 = ["H1","h2","h3","h4","h5"]
for i in l2:
    if i=="h3":
        continue
    print(i)

# reverse a string
str1 ="python"
print(str1[::-1]) # by using slicing
# without using inbuilt function /by using loop
# for ,indexing ,range , output
# l1[5:-1:-1]
# 0 1 2 3 4 5
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")

# print first 50 prime numbers

