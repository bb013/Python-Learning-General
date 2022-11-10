import random
low=10
high=500
number_to_guess=77

# need the computer to choose a random number in a range, tell me what it is and if it is correct, break out of loop,\
# otherwise use the information of it being too small or large to redefine the range and guess again.

def checkitout(l,h):
    lowguess = l
    highguess = h
    while True:
        c_guess = random.randrange(lowguess,highguess)
        if c_guess == number_to_guess:
            print(f'The compter has correctly guessed {number_to_guess}!')
            break
        if c_guess > number_to_guess:
            print(f'the computer guessed high at {c_guess}')
            highguess = c_guess
            #print(f'high {highguess} low {lowguess} ')
        if c_guess < number_to_guess:
            print(f'The computer guessed low at {c_guess}')
            lowguess = c_guess
            #print(f'high {highguess} low {lowguess} ')
checkitout(low,high)