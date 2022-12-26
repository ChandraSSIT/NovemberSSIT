# Exception handling , file operations , Date time functions
# Exception handling
# Exception , error
# Exception => which can be handled by program , and we can expect this earlier
# Error => which can not be expected and not able to handle by the system.

l1 = ["chandra", "Nasir", "Nandini", "Supriya", None, "Swamy", "Vamsi", 1233, '#((**(', 'jj@#@122']
for str1 in l1:
    try:
        print(str1.upper())
        if str1 == "Vamsi":
            10/0
    except AttributeError as ex :
        print("Exception occured for data related" ,str1 , " ",ex)
    except ZeroDivisionError as ex:
        print(ex)
    except Exception as ex:
        print("general exception")
    finally:
       pass

    print("//////////")

    try:
        print("try block executed")
        10/0
    except:
        print("except block executed")
    else:
       print("else exception not occured")

print("////////////")
print("I am printing names in upper case")
print(1 + 2)

# try ,except ,finally
# try => we will keep the which we are going except the exception
# except => it will catch the exception, when ever there is an exception occurred then this block will execute
# finally => this will execute whether exception occurred or not irrespective of that
# else => this will execute if no exception occurred in try block

print("////////for with else ////////")
# for with else block
for i in range(4):
    print(i)
    # if i == 2:
    #     break
else:
    print("else from for ")
# else block will execute if complete for loop executes without any break or return in between
