n = int(input("how many rows do u want"))
k=0
for i in range(1,n+1):
    for j in range(1,i+1):
        k+=1
        print(k,end = " ")
    print()