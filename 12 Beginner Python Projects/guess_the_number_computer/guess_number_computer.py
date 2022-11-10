import random
"""
def guess(x):
    secret_number=random.randint(1, x)
    guessing = 0
    while guessing != secret_number:
        try:
            guessing=int(input(f"Guess a number between 1 and {x}: "))
        except:
            print("whole numbers only please")
            continue  
        if guessing < secret_number:
            print(f'You guessed low:')
        if guessing > secret_number:
            print(f'You guessed high')
    print(f'Thats right! {secret_number} is the correct number!')
guess(20)
"""
def computer_guess(l,h,n):
    lowguess = l
    highguess = h
    number_to_guess = n
    while True:
        c_guess = random.randrange(lowguess,highguess)
        if c_guess == number_to_guess:
            print(f'The compter has correctly guessed {number_to_guess}!')
            break
        if c_guess > number_to_guess:
            print(f'the computer guessed high at {c_guess}')
            highguess = c_guess
            # print(f'high {highguess} low {lowguess} ')
        if c_guess < number_to_guess:
            print(f'The computer guessed low at {c_guess}')
            lowguess = c_guess
            # print(f'high {highguess} low {lowguess} ')
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
