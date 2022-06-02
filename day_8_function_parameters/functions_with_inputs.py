# Simple Function
def greet():
    print("Hello")
    print("Hola")
    print("Bonjour")


greet()


# Function that allows for input
def greet_with_name(name):  # name is the parameter here
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Parinita")  # input is the argument here


# Functions with more than one inputs
def info(name, age, gender):
    print("Your details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")


info(input("What is your name?\n"), input("What is your age?\n"), input("What is your gender?\n"))


def greeting(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    print(" ")


# Positional Argument
greeting("Bangalore", "Parinita")

# Keyword Argument
greeting(location="Bangalore", name="Parinita")
