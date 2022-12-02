rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

art_list = [rock,paper,scissors]

# input
# Note: This does not account for anything other than a number, I like to use while loops to catch errors but won't take the time in this program
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice <0:
    print("You typed an invalid number and therefore forfeit and lose.")
else:
    # prints art
    print(art_list[player_choice])

    # logic for compter to choose
    computer_choice = random.randint(0, 2)
    # prints art
    print("Computer choses: \n",art_list[computer_choice])

    # logic for win or lose:

    if player_choice == computer_choice: print("A game for the ages! It is a tie!")
    elif ((player_choice == 0) and (computer_choice == 2))\
        or ((player_choice == 1) and (computer_choice == 0))\
            or ((player_choice == 2) and (computer_choice == 1)):
            print("You Win!")
    else: print("You lose!")