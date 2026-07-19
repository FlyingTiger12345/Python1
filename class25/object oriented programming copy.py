class names:

    def __init__(self):
        print("Employee")

    def __del__(self):
    
        print("Destructor called")

def prints():
    print("making object")
    obj = names()
    print("function end")
    return names

obj1 = prints()
del obj1


