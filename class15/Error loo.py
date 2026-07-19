try:
    valid = False
    while not valid:
        n = int(input("enter a number"))
        while n%2 == 0:
            print("bye")
        print("the number is odd")
        valid = True
except ValueError as ex:
    print("the enterd value is wronng",ex)