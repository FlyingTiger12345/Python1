from abc import ABC, abstractmethod

class abstract:
    def print(self,x):
        print("value", x)
    
    @abstractmethod
    def print1(self):
        print("i am inside abstractmethod")
class abstract1(abstract):
     def print1(self):
        print("i am inside abstractmethod")

among = abstract1()
among.print1()
among.print(100)

    

