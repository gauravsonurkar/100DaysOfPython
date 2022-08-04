# project in python 2nd project number guessing.
import random
randNumber = random.randint(1, 100)
print(randNumber)
userChoice = None
guess = 0

while (userChoice != randNumber):

    guess = guess + 1
    userChoice = int(input(f" Enter your guess no. {guess} :  "))

    if(userChoice == randNumber):
        print(f" ************** Bravo!! , You win the game in  {guess} guesse's ************** ")
    else:
        if(userChoice > randNumber):
            print(" Please enter the smaller number  ")
        else:
            print(" Please enter the greater number  ")


with open("highscore.txt", 'r') as f:
    highscore = int(f.read())
if(guess < highscore):

    print(" ******************************** Congratulations , You broke the high score!! ******************************** ")
    with open("highscore.txt", 'w') as f:
        f.write(str(guess))
