# Import needed modules
import random, string, os # os gives ability to clear on windows: see line 30
from hangman_art import stages, logo
from hangman_words import word_list

# Play again loop and games played
wins = 0
loses = 0
plays = 0
game_continue = True
while game_continue == True:
    plays += 1

    # Get word, set lives, create blank spaces, print logo, get length of word
    print(logo)
    generated_word = random.choice(word_list)
    lives = len(generated_word) + 3
    display_list = []
    for each_letter in generated_word:
        display_list += "_"

    # Loop for guesses continuing  
    guessed_list = []
    print("The word is: ",*display_list)
    while ("_" in display_list) and (lives > 0):
        
        # ask for guess, check if it is a letter and if it has already been guessed
        while True:
            guess = input("Guess a letter: ").lower()
            os.system('cls')
            if guess not in string.ascii_lowercase:
                print("Single Letters Only Please. Try Again.")
                continue
            elif (guess not in generated_word) or (guess in generated_word):
                if guess in guessed_list:
                    print(f"You've already guessed: {guessed_list}\nPlease Try Again.")
                    continue
                else:
                    guessed_list += guess
                    if guess in generated_word:
                        break
                    else:
                        print("\nNope, guess again.")
                        lives -= 1
                        break
    
        # Replace blanks
        for index_position in range(len(generated_word)):
            letter = generated_word[index_position]
            if letter == guess:
                display_list[index_position] = guess

        # Display artwork according to lives
        if lives >= 6:
            print(stages[6])
        else: print(stages[lives])
        print("The word is: ",*display_list)

    # Win conditions
    if "_" not in display_list:
        print(f"You correctly guessed {generated_word}!\nYou Win!")
        wins += 1

    # Lose conditions
    else:
        print(f"You didn't guess {generated_word}!\nYou Lose!")
        loses += 1

    # continue or not
    while True:
        continue_question = input("Would you like to keep playing? y or n ?").lower()
        if continue_question not in ("y","n"):
            print("Invalid input, please try again.")
            continue
        elif continue_question == 'y':
            break
        elif continue_question == "n":
            game_continue = False
            break

# End of Game
print(f"You played {plays} times, won {wins} times and lost {loses} times.")