weather = [1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0]
s = 0
r = 0
for i in weather:
    if i == 1:
        s += 1
    else:
        r += 1


if s > r:
    print("sunny weather")
else:
    print("rainy day")