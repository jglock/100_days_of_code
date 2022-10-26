"""
Caesar Cipher decryption tool.
"""
import art
from string import ascii_lowercase

def caesar(text:str, shift:int, direction:str):
    crypted_text = ""

    for letter in text:
        if letter in ascii_lowercase:
            if direction == "encode":
                new_index = ascii_lowercase.index(letter) + shift
                indentation_check = new_index > 25
                starting_letter = "a"
                new_shift =  shift - (26 - ascii_lowercase.index(letter))
            else:
                new_index = ascii_lowercase.index(letter) - shift
                indentation_check = new_index < 0
                starting_letter = "z"
                new_shift =  shift - (1+ascii_lowercase.index(letter))

            if indentation_check:
                crypted_text += caesar(starting_letter, new_shift,  direction)
            else:
                crypted_text += ascii_lowercase[new_index]
        else:
            crypted_text += letter
    
    return crypted_text



def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(caesar(text, shift, direction))

    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == "yes":
        main() 

print(art.logo)
main()