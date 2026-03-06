
try:
    a =int(input("enter a number"))
    print("the number is",a)
except ValueError as ex:
    print("a error occured",ex)

