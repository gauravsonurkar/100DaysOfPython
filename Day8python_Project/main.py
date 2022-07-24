import random  # its generate the random number


def gamewin(comp, you):  # its an function which is used to check computer win or you win 😎😎
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer Turn : Snake(s) Water(w) or Gun(g)")
# it is used to take any random number (1,3) from the random library
randNo = random.randint(1, 3)
if randNo == 1:  # 1 denotes snake
    comp = 's'
elif randNo == 2:  # 2 denotes water
    comp = 'w'
elif randNo == 3:  # 3 denotes gun
    comp = 'g'
you = input("Your Turn : Snake(s) Water(w) or Gun(g)")

a = gamewin(comp, you)  # function call

print(f"Computer choose : {comp}")
print(f"You choose : {you}")

if a == None:
    print("Game tie!")
elif a:
    print("You win!")
else:
    print("You lose!")
