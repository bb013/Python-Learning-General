#Clear screen
import os
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

# start of program
from art import logo
print(logo)

print("Welcome to the secret auction program.")
auction_dic = {}
game_continue = True
while game_continue == True:
    name = input("What is your name?: ").capitalize()
    while True:
        try:
            bid = int(input("What's your bid?: $"))
        except:
            print("Whole Numbers above zero only please. Try again.")
            continue
        break
    while True:
        continue_or_not = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if continue_or_not not in ('yes', 'no'):
            print("Invalide input, please type 'yes' or 'no'.")
            continue
        else: break
    auction_dic[name] = bid
    clear()
    # check if continue
    if continue_or_not == "no":
        game_continue == False
        break
    else:continue
# loop through dictionary and compare bids
# TODO: clarify naming
highest_bid = 0
for each_bidder in auction_dic:
    bid_amount = auction_dic[each_bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        the_winner = each_bidder

print(f"The Winner is {the_winner} with a bid of ${highest_bid}!")