'''
This code runs a simulation of the monty hall probability problem.
'''

from random import choice, shuffle

# the host of the gameshow
def monty(doors,guess):
    for x in range(3):
        if doors[x] != 'car' and x != guess:
            return x

# the guest doesn't use anything but the indexes of the doors

# the first guess
def guess1():
    return choice(range(3))

# the second guess
def guess2(stick,reveal,guess):
    # stay on the same door or not?
    if stick == True:
        return guess
    else:
        options = [0,1,2]
        options.remove(reveal)
        options.remove(guess)
        return options[0]

def game():
    # options behind each door
    doors = ['goat','goat','car']
    shuffle(doors)
    # guess 1
    g1 = guess1()
    # guess 2
    g2 = guess2(False,monty(doors,g1),g1)
    # if car is found
    if doors[g2] == "car":
        return 1
    else:
        return 0

# tests probability
def main():
    wins = 0
    n = 100000
    for i in range(n):
        wins += game()
    # n of success / n of trials = probability of success
    print(float(wins/n))

main()
