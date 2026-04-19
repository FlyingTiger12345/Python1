from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def animal(self):
        print("i am animal")
    
class Human(Animal):
    def animal(self):
        print("i can walk two legs")

class Tiger(Animal):
    def animal(self):
        print("i can walk four leegs legs")

class Lion(Animal):
    def animal(self):
        print("i can walk four legs also")


class Crow(Animal):
    def animal(self):
        print("i eat remaining food")


class John(Animal):
    def animal(self):
        print("My name is john")





human1 = Human()
tiger1 = Tiger()
lion1 = Lion()
crow1 = Crow()
john1 = John()

human1.animal()
tiger1.animal()
lion1.animal()
crow1.animal()
john1.animal()

