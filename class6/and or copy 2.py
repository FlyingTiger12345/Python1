w = float(input("what your wweight"))
h = float(input("what your height"))

bmi = w/(h*h)
print("your bmi is",bmi)

if bmi < 18.5:
    print("you are under weight")
elif bmi < 25:
    print("you are healthy")
elif bmi < 30:
    print("you are overweight")
else:
    print("you are obese")
    
