print('A simple rock-paper-scissors-lizzard-Spock game.')

import random

def play():
    print("Scissors cut paper.\n\
Paper covers rock.\n\
Rock crushes lizard.\n\
Lizard poisons Spock.\n\
Spock smashes scissors.\n\
Scissors decapitates lizard.\n\
Lizard eats paper.\n\
Paper disproves Spock.\n\
Spock vaporizes rock.\n\
Rock crushes scissors")
    while True:
        userinput = input("Select 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizzard, or 'sp' for Spock: ").lower()
        # error check
        if userinput not in ('r','p','s','l','sp'):
            print('Invalid input. Please try again.')
            continue
        # quit() # debug
        break
    computerinput = random.choice(['r','p','s','l','sp'])
    print(f'Your opponent chooses {computerinput}')
    if userinput == computerinput:
        return "It's a tie"
    if is_win(userinput, computerinput):
        return 'You won!'
    return 'You lost!'
def is_win(player, opponent):
    # return true if player wins
    if (player == 's' and opponent == 'p')\
        or (player == 's' and opponent == 'l')\
        or (player == 'p' and opponent == 'r')\
        or (player == 'p' and opponent == 'sp')\
        or (player == 'r' and opponent == 's')\
        or (player == 'r' and opponent == 'l')\
        or (player == 'l' and opponent == 'sp')\
        or (player == 'l' and opponent == 'p')\
        or (player == 'sp' and opponent == 's')\
        or (player == 'sp' and opponent == 'r'):
        return True
print(play())