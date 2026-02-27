def factorials(x):
    if x==1:
        return 1
    else:
        return x * factorials(x-1)
print(factorials(5))

