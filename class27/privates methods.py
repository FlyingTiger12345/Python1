class MyClass:
    __number = 27

    def __privMethods(self):
        print("ok")

    def yes(self):
        print("hello",MyClass.__number)
among = MyClass()
among.yes()
among.__privMethods()