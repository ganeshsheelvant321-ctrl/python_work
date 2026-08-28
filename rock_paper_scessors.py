#rock paper sceissors
import random
options=("rock","paper","sceissers")
player=None
running=True
while running:
    #player choise
    while player not in options:
        player=input("enter the (rock,paper,sciessors):")
    #compputer choise
    computer=random.choice(options)
   
    print(f"player:{player}")
    print(f"computer:{computer}")
    if computer==player:
        print("it's a tie!")
    elif player == "rock" and computer == "scissors":
         print("You win!")
    elif player == "paper" and computer == "rock":
         print("You win!")
    elif player == "scissors" and computer == "paper": 
         print("You win!")
    else:
         print("You lose!")
    #reset player to none
    player=None
    play_again=input("play again?(y or n):").lower()
    if play_again=="n":
         running=False     

print("Thanks for playing the game")        

    