# The scratch pad is for whatever tidbit of code I'm playing with and trying to make work.

# import the die
from dice_master import die_d4,die_d6,die_d8,die_d10,die_d12,die_d20,die_d100

# rolls d6 x number of times remove the lowest number and print the result
x = int(input('how many die? '))
def d6_roll_list():
    rolls = x
    roll_list = []
    while rolls > 0:
        rolls = rolls-1
        d6roll = [die_d6()]
        roll_list.extend(d6roll)
    print(f'Dice rolls are: {roll_list}')
    roll_list.remove(min(roll_list))
    #print(roll_list)
    roll_total = sum(roll_list)
    print(f'The total removing the lowest number is: {roll_total}')
    return roll_list
print(d6_roll_list())