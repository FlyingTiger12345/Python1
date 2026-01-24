a = int(input("insert money notes here"))

bigbill = a//1000
medbill = (a%1000)//500
smallbill = ((a%1000)//500)//200
print("the count of bigbill is", bigbill)
print("the count of medbill is", medbill)
print("the count of smallbill is", smallbill)