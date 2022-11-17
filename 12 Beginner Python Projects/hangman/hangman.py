import random
import string
from wordlist import words
from hangman_visual import lives_visual_dict

# selects a random word
def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase) # creates a list of the uppercase alphabet
    used_letters = set() # what the user has guessed
    lives = len(word) + 3
    user_tries = 0

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        if lives > 7:
            print(lives_visual_dict[7])
        else:
            print(lives_visual_dict[lives])
        print('Current word: ',' '.join(word_list))
        if user_tries > 0:
                print("You have used these letters: ", ' '.join(used_letters))
        user_tries = user_tries + 1
        while True: # verifies valid input
            user_letter = input('Enter a letter to guess: ').upper()
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
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f'\nYour letter, {user_letter}, is not in the word. You have {lives} tries.')

    # end of game
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f'The hangman has done his job.\n You lost.\n The word was {word}.')
    else:
        print(f'You guessed correctly! The word was {word}!')
hangman()