try:
    a = int(input("check if it is a family tree of the number 3: "))
    if a % 3 == 0:
        print("this number is a family by 3")
    elif a == 67:
        print("six seven")
    else:
        print("not family by 3")
except ValueError:
    print("only numbers")


