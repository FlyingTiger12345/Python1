class ab:
    def __init__(self, a):
        self.a = a
    
    def __lt__(self, other):
        if (self.a<other.a):
            return "ob1 is more than ob2"
        else:
            return "ob2 is more than ob1"
        
    def __eq__(self, other):
        if (self.a==other.a):
            return "ob1 is equal than ob2"
        else:
            return "ob2 is not equal than ob1"

ob1 = ab(3)
ob2 = ab(67)

print("value",ob1.a,ob2.a)
print(ob1 > ob2)

ob1 = ab(67)
ob2 = ab(67)

print("value",ob1.a,ob2.a)
print(ob1 == ob2)

   