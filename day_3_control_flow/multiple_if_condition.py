# It checks all the conditions and if all of them are true, it will execute all of them.

print("Welcome to the roller coaster")
height = int(input("What is your height(in cm)?"))
bill = 0

if height >= 120:
    print("You can go on the ride!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("Do you want a photo? Y for Yes or N for No")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")


else:
    print("Sorry, you can't go the ride")