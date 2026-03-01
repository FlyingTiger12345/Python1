str5 = input("enter a text")

for i in str5:
    if i.lower() == "a":
        print("this has letter a")
        break
else:
    print("no letter a")