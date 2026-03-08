import random
choices = ['rock','paper','scissors']



while True:
    rapper = random.choice(choices)
    a = input("rock paper scissors")
    if a == rapper:
        print("tie")
    elif (a == "rock" and rapper == "scissors") or (a == "scissors" and rapper == "paper") or (a == "paper" and rapper == "rock"):
        print("you win")
        print(rapper)
    else:
        print("you lose")
        print(rapper)
    ab = input("you want to play: y/n")
    if ab == "n":
        break