from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 5,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 2500,
}

profit = 0


def resource_sufficient(order_item):
    for item in order_item:
        if order_item[item] > resources[item]:
            print(f"Sorry there is not enough {item} ")
            return False
    return True


def get_float_number(msg):
    number = input(msg)
    try:
        number = int(number)
        return number
    except ValueError:
        return None


def process_coins():
    drink = MENU[choice]
    print(f"You need to pay {drink['cost']} for your drink")
    bill = get_float_number("Insert your money: ")
    while not bill:
        print("Invalid amount.Please re-enter")
        bill = get_float_number("Insert your money: ")
    return bill


def transaction_successful(money_paid, drink_cost):
    if money_paid >= drink_cost:
        change = round(money_paid - drink_cost, 2)
        print(f"Thank you.Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    elif money_paid < 0:
        print("Sorry money can't be negative")
    elif money_paid < drink_cost:
        print("Sorry that's not enough money.Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here's your {drink_name}☕️.Enjoy!!")
        return None


machine_on = True

while machine_on:
    print(logo)
    user_choice = False
    while not user_choice:
        choice = (input("What would you like?(espresso\latte\cappuccino): "))
        if choice == "off":
            machine_on = False
            user_choice =  True
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
            user_choice = True

        elif choice == "latte":
            drink = MENU[choice]
            if resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
            user_choice = True
        elif choice == "cappuccino":
            drink = MENU[choice]
            if resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
            user_choice = True
        elif choice == "espresso":
            drink = MENU[choice]
            if resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
            user_choice = True
        else:
            print(f"Sorry,{choice} is unavailable.Please re-enter")

