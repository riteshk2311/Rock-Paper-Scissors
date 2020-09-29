# rock paper scissor
# created by Ritesh
#

import random

name = input("Enter Player Name: ")


def game(comp, player):
    if comp == player:
        return 0
    if comp == 's':
        if player == 'p':
            return False
        elif player == 'k':
            return True

    elif comp == 'p':
        if player == 's':
            return False
        elif player == 'k':
            return True

    elif comp == 'k':
        if player == 'p':
            return False
        elif player == 's':
            return True


comp = 'a'
print("Computer: Choose Stone(s) Paper(p) Scissor(k)")
randomno = random.randint(1, 3)
if randomno == 1:
    comp = 's'
elif randomno == 2:
    comp = 'p'
if randomno == 1:
    comp = 'k'

player = input(f"{name}: Choose Stone(s) Paper(p) Scissor(k):= ")

a = game(comp, player)

print(f"{name} Choose: {player}")
print(f"Computer Choose: {comp} ")
if a == 0:
    print("The game is a tie!")

elif a:
    print("You Win!")

else:
    print("You Lose")

# created by Ritesh
