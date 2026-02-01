mc = input("enter the studdent has medical causee (y/n):")
if mc =='y':
    print("the student is allowed to write")
elif mc == "n":
    at = int(input("enter student attendance"))
    if at >= 75:
            print("the student is allowed to write exam")
    else:
        print("the student is not allowed to write exam")
else:
    print("invalid")


