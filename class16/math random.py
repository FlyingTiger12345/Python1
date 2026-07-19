import random

rapper = random.randint(1,10)

while True:
    a = int(input("guess my favorite number"))
    if a == rapper:
        print("wow amazing")
        break
    else:
        print("no no ")