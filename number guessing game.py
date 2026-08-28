import random
low=int(input("enter a low number:"))
high=int(input("enter a high number:"))
guesses=0
number=random.randint(low,high)
while True:
    guess=int(input("guess the number:"))
    guesses+=1
    if guess<number:
        print(f"{guess} is too low")
    elif guess>number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct")
        break
print(f"this round took you {guesses} guesses")    


      