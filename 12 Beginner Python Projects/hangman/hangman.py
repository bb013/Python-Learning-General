import random
import string
from wordlist import words

# selects a random word
def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letter in the word
    alphabet = list(string.ascii_uppercase) # creates a list of the uppercase alphabet
    used_letters = set() # what the user has guessed
    deathcount = len(word)+2

    # what current word is
    word_list = [letter if letter in used_letters else '_' for letter in word]

    # get user input
    while len(word_letters) > 0:
        while True: # verifies valid input
            user_letter = str(input('Enter a letter to guess: ')).upper()
            if user_letter in used_letters:
                print("You've already guessed that one")
                print("You have used these letters: ", ' '.join(used_letters))
                continue
            if user_letter in (alphabet):
                break
            print('Single letters only. Please try again ')
            continue
        if user_letter not in used_letters:
            used_letters.add(user_letter)
            deathcount - 1
        if user_letter in word_letters:
            word_letters.remove(user_letter)


print('You lost.')
print(f'The correct word was {word}.')