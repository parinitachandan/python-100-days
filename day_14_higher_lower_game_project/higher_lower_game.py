from game_data import data
from art import logo, vs
import random


def random_choice():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    print(f"{name}, a {description}, from {country}")


def check_ans(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():

    score = 0
    game_continue = True
    account_a = random_choice()

    while game_continue:
        print(logo)
        account_b = random_choice()

        while account_a == account_b:
            account_b = random_choice()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        should_guess = False

        while not should_guess:
            user_guess = input("Who has more followers.Type 'A' or 'B': ").lower()
            if user_guess == "a" or user_guess == "b":
                should_guess = True
            else :
                print("Invalid Input")

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_ans(user_guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b
        else:
            game_continue = False
            print(f"Sorry, your wrong.Final score: {score}")


game()
