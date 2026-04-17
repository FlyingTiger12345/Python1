class Comps:
     def __init__(self):
        self.__price = 900
     def displayprice(self):
        print("the price",(self.__price))
     def price1(self,price):
        self.__price = price

y = Comps()
y.displayprice()

y.__price = 1000000000
y.displayprice()
y.price1(1000000)
y.displayprice()


   
