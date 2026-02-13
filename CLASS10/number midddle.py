num = int(input("enter the number"))

str1 = str(num)
len1 = len(str1)
if len1%2 == 0:
    mid = int(len1/2)-1
else:
    mid = int(len1/2)
midproduct = int(str1[mid]) * int(str1[mid+1])
print("the mid product is",midproduct)