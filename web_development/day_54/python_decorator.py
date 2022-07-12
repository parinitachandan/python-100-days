import time

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(multiply, 5, 5)
print(result)

# Functions can be nested in other functions


def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function()


inner_function = outer_function()
inner_function


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


say_hello()
say_bye()