from art import logo

print(logo)
print("Welcome to the secret auction program 🤫")

bids = {}  # Empty dictionary
bidding_complete = False


def high_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if int(bid_amount) > int(highest_bid):
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_complete:
    name = input("What is your name?\n")
    price = input("What is your bid?\n $")

    while not price.isnumeric():
        print("Bid should be a positive integer greater than zero. Please re-enter")
        price = input("What is your bid?\n $")

    bids[name] = price  # adding items to the bid dictionary
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_complete = True
        high_bidder(bids)
    elif should_continue == "yes":
        pass
    else:
        print("Invalid Input\n"
              "Continuing")
