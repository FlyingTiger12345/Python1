choice = input("enteer your choice \n1.bike \n2.car")
if choice == "1":
    bikes = input("which bike \n1.goodbike \n2.bestbike")
    if bikes == "1":
        print("chose good bike")
    elif bikes == "2":
        print("chose best bike")
    else:
        print("invalid")

if choice == "2":
    cars = input("which bike \n1.goodcar \n2.bestcar")
    if cars == "1":
        print("chose good car")
    elif cars == "2":
        print("chose best car")
    else:
        print("invalid")