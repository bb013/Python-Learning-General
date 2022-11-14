import random
def computer_guess(l,h,n):
    lowguess = l
    highguess = h
    number_to_guess = n
    feedback = ''
    while feedback != 'c':
        c_guess = random.randint(lowguess,highguess)
        feedback = input(f'Is {c_guess} too high (H) too low (L) or correct (C)?').lower()
        # error check
        if feedback not in ('c','l','h'):
            print("Please, only enter 'c', 'h', or 'l'.")
            continue
        if feedback == "h":
            highguess = c_guess -1
            if highguess < number_to_guess:
                print('You have lied to the compter')
        if feedback == 'l':
            lowguess = c_guess + 1
            if lowguess > number_to_guess:
                print('You have lied to the compter')
    print(f'The compter has correctly guessed {c_guess}!')
    if c_guess != number_to_guess:
        print(f'You lied, for you said the number to guess was {number_to_guess} and then told the computer it was correct when it guessed {c_guess}. These do not match ')
while True:
    try:
        lownumber = int(input('Enter the lowest number for the range in which th computer will guess: '))
    except:
        print('Whole numbers only please.')
        continue
    break
while True:
    try:
        highnumber=int(input('Enter the highest number for the computer to guess: '))
    except:
        print('Whole numbers only please.')
        continue
    if highnumber <= lownumber+1:
            print(f"Please enter a number greater than {lownumber+1}")
            continue
    break
while True:
    try:
        mysecretnumber=int(input("What is the number the computer must guess? "))
    except:
        print('Whole numbers only please.')
        continue
    if mysecretnumber <= lownumber:
        print(f'please enter a number between {lownumber} and {highnumber}.')
        continue
    if mysecretnumber >= highnumber:
        print(f'please enter a number between {lownumber} and {highnumber}.')
        continue
    break
print(f'The compter will now guess between {lownumber} and {highnumber}.')
computer_guess(lownumber,highnumber,mysecretnumber)
