# Author: Lauren Brown
# Program Name: Rock Paper Scissors
# A fun mini game written in Python, the user has to guess between Rock, Paper, or Scissor against
# the computer, and if the user picks rock but the computer picks scissor the user will win
# Created: 12/4/2018
# License: Open Apache License
# Github:

import random

from pip._vendor.distlib.compat import raw_input


# Generate a Random Number and save it to Choice
def number(a, b):
    choice = random.randint(a, b)
    return choice


# Print Ai's choice
ai = (number(1, 3))

# Game Menu Screen
print("#######################")
print("Welcome to Rock, Paper, and Scissors ")
print("Rock = 1 ")
print("Paper = 2 ")
print("Scissor = 3 ")
print("#######################")

player = raw_input("Enter a number between 1-3: \n")
num = int(player)

if num == 1 and ai == 2:
    print("You picked:", player, "Ai picked:", ai, "Rock covers Paper, so Player wins")
if num == 2 and ai == 3:
    print("You picked:", player, "Ai picked:", ai, "Scissor cuts Paper, so AI wins")
if num == 3 and ai == 1:
    print("You picked:", player, "Ai picked:", ai, "Rock breaks Scissor, so AI wins")

if num == 1 and ai == 1:
    print("You picked:", player, "Ai picked:", ai, "You both picked Rock, it's a draw")
if num == 2 and ai == 2:
    print("You picked:", player, "Ai picked:", ai, "You both picked Paper, it's a draw")
if num == 3 and ai == 3:
    print("You picked:", player, "Ai picked:", ai, "You both picked Scissors, it's a draw")

