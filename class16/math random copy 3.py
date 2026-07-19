import math

a = input("Do you want all functions or just one function? (all/one): ")
c = int(input("What number? "))
b = input("Which function? (sin/cos/tan): ")

if a == "one":
    if b == "sin":
        print("The sin:", math.sin(c))
    elif b == "cos":
        print("The cos:", math.cos(c))
    elif b == "tan":
        print("The tan:", math.tan(c))
    else:
        print("Invalid function")

elif a == "all":
        print("The sin:", math.sin(c))
        print("The cos:", math.cos(c))
        print("The tan:", math.tan(c))

else:
    print("Invalid choice")



