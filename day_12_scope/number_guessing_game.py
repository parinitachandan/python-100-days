from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_num(guess, answer, turns):
    if guess > answer:
        print("Too high👆, Try guessing a bit lower👇")
        return turns - 1
    elif guess < answer:
        print("Too low👇, Try guessing a bit higher👆")
        return turns - 1
    elif guess == answer:
        print(f"You got it🥳🥳, The number is {answer}")
        return -1


def difficulty_level():
    levels = False
    while not levels:
        level = input("Choose a difficulty level. Type 'easy' for an easy level or Type 'hard' for a hard level:  ")
        if level == 'easy':
            levels = True
            return EASY_LEVEL
        elif level == 'hard':
            levels = True
            return HARD_LEVEL
        else:
            print("Invalid Input\n"
                  "Continuing")


def get_int_number(msg):
    number = input(msg)
    try:
        number = int(number)
        return number
    except ValueError:
        return None


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = difficulty_level()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = make_a_guess()
        turns = check_num(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct number is {answer}")
            return
        elif turns == -1:
            # Return from the loop because you have already won
            return
        elif guess != answer:
            print("Guess again.")


def make_a_guess():
    guess = get_int_number("Make a guess: ")
    while not guess:
        print("Invalid guess.Please re-enter")
        guess = get_int_number("Make a guess: ")
    return guess


game()
