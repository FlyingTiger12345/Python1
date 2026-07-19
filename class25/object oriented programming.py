class ostring():

    def __init__(self):
        self.str1 = ""

    def strings (self):
        self.str1 = input("enter string")
    def prints(self):
        self.str1 = print("result",self.str1.upper())
str1 = ostring()

str1.strings()
str1.prints()