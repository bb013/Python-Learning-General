alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_promt = True
from caesar_cipher_art import logo
while continue_promt == True:
    print(logo)
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction not in ("encode","decode"):
            print("Invalid input, try again.")
            continue
        else: break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar_text(start_text, shift_amount, cipher_direction):
        cipher_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for each_letter in start_text:
            if each_letter in alphabet:
                original_position = alphabet.index(each_letter)
                new_position = (original_position + shift_amount)                 
                while new_position > 25:
                    new_position -= 26
                while new_position < 0:
                    new_position += 26                
                new_letter = alphabet[new_position]
            else:
                new_letter = each_letter
            cipher_text += new_letter
        print(f"The {cipher_direction}d text is {cipher_text}")

    caesar_text(start_text=text, shift_amount=shift,cipher_direction=direction)
    while True:
        continue_question = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
        if continue_question not in ("yes","no"):
            print("Invalid input, try again.")
            continue
        else: break
    if continue_question == "no":
        continue_promt = False