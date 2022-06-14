from menu import Menu,MenuItem
from money import MoneyMachine
from coffee_maker import CoffeeMaker
from art import logo
from prettytable import PrettyTable

menu_table = PrettyTable()
menu_table.add_column("Drink Name", ["Latte", "Espresso", "Cappuccino"])
menu_table.add_column("Drink Cost", [5, 3, 7])

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True
while machine_on:
    user_choice = False
    options = menu.get_items()
    print(logo)
    print(menu_table)

    choice = (input(f"What would you like? {options}: ")).lower()
    if choice == "off":
        machine_on = False
        user_choice = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        user_choice = True
    elif choice == "latte":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
        user_choice = True
    elif choice == "espresso":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
        user_choice = True
    elif choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
        user_choice = True
    else:
        print(f"Sorry,{choice} is unavailable.Please re-enter")





