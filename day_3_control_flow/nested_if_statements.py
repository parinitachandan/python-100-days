print("Welcome to the roller coaster")
height = int(input("What is your height(in cm)?"))
if height >= 120:
    print("You can go on the ride!")
    age = int(input("What is your age?"))
    if age <= 18:
        print("You need to pay $7")
    else:
        print("You need to pay $12")
else:
    print("Sorry, you can't go the ride")