import hangman_art
from wordlist import word_list
from random import choice



print(hangman_art.hangman_text)

chosen_word = choice(word_list)

display = []

lives = 6

for character in range(len(chosen_word)):
    display.append("_")


while True:

    print(display)

    guess = input("\nGuess a letter: ").lower()


    for index in range(len(display)):
        if guess == chosen_word[index]:
            display[index] = guess
       
    if guess not in chosen_word:
        lives -= 1

    print(hangman_art.hangmanpics[6 - lives])

    if lives == 0:
        result = "lose"
        break

    if not "_" in display:
        result = "win"
        break


print(f"You {result}.")