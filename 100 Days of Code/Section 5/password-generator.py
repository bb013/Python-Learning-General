#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("You will be asked how many letters, symbols, and numbers you would like. So take you desired total charators and split it up how you want!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# grab letters using random
letter_range = len(letters) - 1
letter_choice_list = []

for letter in range(nr_letters):
    random_letter = random.choice(letters)
    letter_choice_list.append(random_letter)
#print(letter_choice_list)

# grab symbols using random
symbol_range = len(symbols) - 1
symbol_choice_list = []

for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    symbol_choice_list.append(random_symbol)
#print(symbol_choice_list)

# grab numbers using random
number_range = len(numbers) - 1
number_choice_list = []

for number in range(nr_numbers):
    random_number = random.choice(numbers)
    number_choice_list.append(random_number)
#print(number_choice_list)

# create one list from all of it
master_list = number_choice_list + symbol_choice_list + letter_choice_list
#print(master_list)

# randomly reorder list
random.shuffle(master_list)
#print(master_list)

# change list to string
password_str = ""
for each_thing in master_list:
    password_str += each_thing
print(f'Your password is: {password_str}')