import random
low=10
high=500
number_to_guess=77

# need the computer to choose a random number in a range, tell me what it is and if it is correct, break out of loop,\
# otherwise use the information of it being too small or large to redefine the range and guess again.

def checkitout(l,h):
    c_guess = random.randrange(l,h)
    print(c_guess)
    if c_guess == number_to_guess:
        print(f'The compter has correctly guessed {number_to_guess}!')
        quit()
    while c_guess != number_to_guess:
        if c_guess > number_to_guess:
            print(f'the')



checkitout(low,high)