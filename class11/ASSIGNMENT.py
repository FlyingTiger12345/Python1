n = int(input("how many rows do u want"))
space = 20
for i in range(1,n+1):
    for j in range(1,space):
        print(end = " ")
    for k in range(1,i+1):
        print("*",end = " ")
    print()
    space -= 2
