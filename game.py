
import random

hidden=random.randrange(1,10)
hidden = 5


guess= int(input("enter the guess:"))

if guess == hidden:
    print("you won !")
elif guess<hidden:
    print("your guess is too low")
else:
    print("your guess is too high")
