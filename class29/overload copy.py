class ab:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        
        return self.word+' ('+self.meaning+')'
    
    
flash = []
while(True):
    word = input("what word you like")
    meaning = input("what meaning you like")

    flash.append(ab(word,meaning))
    option = int(input("want to continne reply 0 else 1"))

    if option == 1:
        break

print("your flashcard")
for i in flash:
    print(">",i)
   