string = input("enter your word")

char = input("enter your character")

i = 0
count = 0

while (i<len(string)):
    if(string[i]==char):
        count = count + 1
    i = i + 1
print("TThe tottal of number times repeated in this character is",count)
