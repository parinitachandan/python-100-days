class MoneyMachine:
    CURRENCY = "$"
    DRINK_COST = {
       "latte": 5,
       "espresso":3,
       "cappuccino":7
   }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        money_received = input("Please pay for your drink: ")
        if money_received.isnumeric():
            self.money_received += int(money_received)
            return self.money_received
        else:
            return False

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        money_received = self.process_coins()
        while not money_received:
            money_received = self.process_coins()

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        elif self.money_received < 0:
            print("Sorry money can't be negative.Order canceled")
        elif self.money_received < cost:
            print("Sorry that's not enough money. Order canceled.")
            self.money_received = 0
            return False
        elif self.money_received != int:
            print("Invalid amount.Please re-enter")
            self.money_received += int(input(f"Please Pay for your drink: "))
            return self.money_received

