import os
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ceasar(message, key, action):
    cipher_text = ""
    if action == "decode":
        key *= -1
    for letter in message:
        if letter in alphabet:
            pos = alphabet.index(letter)
            if pos + key < -26:

                
                while pos + key < -26:
                    pos += 26
            elif pos + key > 25:
                while pos + key > 25:
                    pos -= 26
            cipher_text += alphabet[pos + key]
        else: cipher_text += letter
    print(f"The {action}d text is {cipher_text}")


game_over = False

while not game_over:
    print(art.logo)
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(message=text, key=shift, action=direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if choice == "no":
        game_over = True

    clear_screen()