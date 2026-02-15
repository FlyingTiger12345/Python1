n = int(input("how many rows do u want"))
space = 20
for i in range(1,n+1,2):
    for j in range(space):
        print(end = " ")
    for k in range(1,i+1):
            print(k,end = "")
    space -= 1
    print()

space += 2
for i in range(n-2,0,-2):
    for j in range(space):
        print(end = " ")
    for k in range(1,i+1):
            print(k,end = "")
    space += 1
    print()