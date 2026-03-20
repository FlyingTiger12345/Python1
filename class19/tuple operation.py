def tables1(tuple1):
    s = 0
    e = len(tuple1)-1
    while (s < e):
        if tuple1[s] != tuple1[e]:
            return False
        s+=1
        e-=1
    return True

tuple1 = (1,2,3,353345453,2,1)
print(tuple1)
if tables1(tuple1):
    print("palidrome")
else:
    print("non palidrome")