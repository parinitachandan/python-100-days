# Replacing the blank with guesses

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter : ").lower()

for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter

print(display)



