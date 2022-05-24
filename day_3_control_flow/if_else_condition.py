# if height isn't converted into an integer it gives a type error as below
# TypeError: '>=' not supported between instances of 'str' and 'int'

print("Welcome to the roller coaster")
height = int(input("What is your height(in cm)?"))
if height >= 120:
    print("You can go on the ride!")
else:
    print("You are too short for the ride")

print("Welcome to the scary house!!")
age = int(input("May I know your age please?"))
if age >= 15:
    print("You can enter the scary house")
    print("Choose any door in front of you to enter ")
    print("Enjoy")
else:
    print("Sorry you can't enter the scary house")



