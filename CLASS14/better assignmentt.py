shop = input("do u want tto buy 67 dollar item y/n")



def shop12():
    if shop == "y":
        shop2 = int(input("how much cash you have"))
        if shop2 >= 0:
            print(shop2-67)
    elif shop == "n":
        print("ok bye")
    else:
        print("ok")
shop12()
