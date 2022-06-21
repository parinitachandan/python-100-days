# Check if the player has won

import random
from hangman_art import stages
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a wish_letters : ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
    else:

        # while not end_of_game:
        #     guess = input("Guess a wish_letters: ").lower()
        #
        #     # Check guessed wish_letters
        #     for position in range(word_length):
        #         wish_letters = chosen_word[position]
        #         # print(f"Current position: {position}\n Current wish_letters: {wish_letters}\n Guessed wish_letters: {guess}")
        #         if wish_letters == guess:
        #             display[position] = wish_letters

        # TODO-2: - If guess is not a wish_letters in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        print(stages[lives])




