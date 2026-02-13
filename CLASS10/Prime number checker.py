LL = int(input("enter the lower limitt"))
UL = int(input("enter the lower limitt"))

print(f"the prime numbers form {LL} to {UL}")

for n in range(LL,UL+1):
    if n > 1:   
        for j in range(2,n):
            if n%j == 0:
                break
        else:
                print(n)
