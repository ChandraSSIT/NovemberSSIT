# File operations
file1 = open("sample1.txt", "a")
file1.write("\nis dynamic language")
file1.close()
# print(file1.read())
# filepath
# mode => write(w) , read (r), append(a)
# w+,r+,a+

# context management => it will release the memory of object once we moved out of block of code , for this
# we will use with
with open("sample2.txt","r+") as file2:
    print(file2.read())
    file2.write("New progrm with11")

with open("sample3.txt","w+") as file2:
    file2.write("Sample of data from program")
    file2.seek(0)
    print(file2.read())

with open("sample3.txt","a+") as file2:
    file2.write("\nSample of data from program")
    file2.seek(0)
    print(file2.read())
    
# Read= > to read file , if file not exists it will give error
# write => to write data into file ,if file not exists it will create and write , if exists it will override data
# append=> it will append to existing data in file ,if file not exists it will create
# read plus(r+) => you will read file first then you will wrire into it
# write plus(w+) => you will write first and then you will read , to read from starting position you need to use seek
# append plus(a+) => you will append the data to existing file and read

# Data time functions
