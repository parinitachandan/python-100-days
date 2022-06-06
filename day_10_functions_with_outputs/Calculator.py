from art import logo


def add(no_1, no_2):
    return no_1 + no_2


def subtract(no_1, no_2):
    return no_1 - no_2


def multiply(no_1, no_2):
    return no_1 * no_2


def divide(no_1, no_2):
    return no_1 / no_2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }


def get_float_number(msg):
    number = input(msg)
    try:
        number = float(number)
        return number
    except ValueError:
        return None


def calculator():
    print(logo)
    num1 = get_float_number("What is the first number?:")
    while not num1:
        print("Invalid number.Please re-enter")
        num1 = get_float_number("What is the first number?:")

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        while not operation_symbol in operations:
            print("This is an invalid operation.Please re-enter")
            operation_symbol = input("Pick an operation: ")

        num2 = get_float_number("What's the next number?: ")
        while not num2:
            print("Invalid number.Please re-enter")
            num2 = get_float_number("What's the next number?: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choose_num = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, "
            f"or type 'end' to stop: ")

        if choose_num == 'y':
            num1 = answer
        elif choose_num == 'n':
            should_continue = False
            calculator()
        elif choose_num == 'end':
            should_continue = False


calculator()
