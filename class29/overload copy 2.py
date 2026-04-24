import random

class amongus:

    def __init__(self):

        self.fruits = {
            'apple':'green',
            'canteloupe':'orange',
            'orange':'orange',
            'banana':'yellow',
            'grapes':'purple'
        }

    def quiz(self):
        while True:
            fruit,color = random.choice(list(self.fruits.items()))

            print('what is the color',(fruit))
            answer = input()

            if answer.lower() == color:
                print('correct annswer')
            else:
                print('wrong answer')

            option = int(input("want pllay again press 1 else 0"))

            if option == 0:
                break
print("welcome to quiz")
ys = amongus()
ys.quiz()


        
