class vehicle:
    def __init__(self,name,maxspeed,maxmileage):
        self.name = name
        self.maxspeed = maxspeed
        self.maxmileage = maxmileage
        pass
class bus(vehicle):
    pass


busone = bus("BUS",67,677)

print("the name of the bus",busone.name,"the max speed is",busone.maxspeed , "the max mileage is", busone.maxmileage)