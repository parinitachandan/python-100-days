import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []  # Empty list
    computer_cards = []  # Empty list

    for _ in range(2):  # [using an underscore - as variable isn't needed here]
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    game_over = False
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, Your Current Score: {user_score}\n"
              f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_card_deal = False
            while not user_card_deal:
                user_deal = input("Type 'yes' to get another card or Type 'no' to pass:  ")
                if user_deal == 'yes':
                    user_cards.append(deal_card())
                    user_card_deal = True

                elif user_deal == 'no':
                    game_over = True
                    user_card_deal = True
                else:
                    print("Invalid Input\n"
                          "Continuing")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


new_game = False
while not new_game:
    play = input("Do you want to start a new game of Blackjack? Type 'y' for yes or 'n' for no: ")
    if play == 'n':
        new_game = True
    elif play == 'y':
        play_game()
    else:
        print("Invalid Input\n"
              "Continuing")
