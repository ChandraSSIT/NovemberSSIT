# Iterators ,Generators
l1 = [2, 3, 4, 5, 6]


def evennnumbers():
    l2 = []
    for i in l1:
        if i % 2 == 0:
            l2.append(i)
    return l2


evennnumbers()
iterobj = iter(l1)
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))

print("//////////////")


def evennumbers():
    for i in l1:
        if i % 2 == 0:
            yield i


print(evennumbers())
for i in evennumbers():
    print(i)

# Anonymous function /lambda function

x = lambda a,b:print(a,b)

def myname(a):
    print(a)

myname("Hello Python")

x("Hello Python","Test")

# map
# filter

l1=[1,2,3,4,5]
l2 = list(map(lambda z:z*2,l1)) #iteration
print(l2)
# filter => it will apply some conditions
l3 = list(filter(lambda x:(x%2==0),l1))
print(l3)