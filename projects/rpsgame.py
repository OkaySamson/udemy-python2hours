#Rock wins over Scissors
#Scissors wins over Paper
#Paper wins over Rock

from random import randint
#from is the keyword used to refer to a library 

#tuple 
objects = ("rock", "paper", "scissors")

computer = objects[randint(0, 2)]

while True:
    user = input("rock, paper or scissors?:  ").lower().lstrip()
    if (user == computer):
        print("Tie Game!")
    elif user == "rock":
        if computer == "paper":
            print("You Lose! -", computer, "covers", user)
        else:
            print("You Win! -", user, "smashes", computer)
    elif user == "scissors":
        if computer == "rock":
            print("You Lose! -", computer, "smashes", user)
        else:
            print("You Win! -", user, "cuts", computer)
    elif user == "paper":
        if computer == "scissors":
            print("You Lose! -", computer, "cuts", user)
        else:
            print("You Win! -", user, "covers", computer)
    else: 
        print("Invalid Input - ONLY rock, paper, and scissors recognized.")
    computer = objects[randint(0, 2)]


#print(randint(0, 2))
#displays random number from 0 to 2

#module is a seperate sigular file thats outside 
#library is a set of modules all together

