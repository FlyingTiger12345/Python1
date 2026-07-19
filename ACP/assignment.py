class doggos:

    species = "Bulldogs"
    species2 = "Golden Retriever"
    def __init__(self,age,name,hobby):
        self.age = age
        self.name = name
        self.hobby = hobby

        pass

doggy1 = doggos(42,"James","play bones and poop")
doggy2 = doggos(76,"Michael","Eat and sleep")


print("Albert is an {}".format(doggy1.species))
print("John is an {}".format(doggy2.species2))


print("This Dog is aged at{} and its name {} and they love to {}".format(doggy1.age,doggy1.name,doggy1.hobby))
print("This Dog is  aged at{} and its name {} and they love to {}".format(doggy2.age,doggy2.name,doggy2.hobby))






    