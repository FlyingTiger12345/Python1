class parrot:

    species = "Chicken"
    species2 = "Crow"
    def __init__(self,age,name):
        self.age = age
        self.name = name

        pass

parrot1 = parrot(36,"John")
parrot2 = parrot(67,"Albert")


print("Albert is an {}".format(parrot1.species))
print("John is an {}".format(parrot2.species2))


print("parrot1 is aged at{} and its name {}".format(parrot1.age,parrot1.name))
print("parrot2 is  aged at{} and its name {}".format(parrot2.age,parrot2.name))






    