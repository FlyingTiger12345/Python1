class vehicle:
    def fare(self,n,amt):
        print("the totaal farer is ", n *amt)

class bus(vehicle):
    pass

b1 = bus()
b1.fare(20,678777777777)