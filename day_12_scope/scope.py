# Global scope
name = input("What is your name?: ")


def info():
    # Local scope
    age = input("What is your age?: ")
    print(f"Name: {name}\n"
          f"Age: {age}")


info()

# Global constant
PI = 3.14159


