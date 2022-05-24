
# and operator
a = 12
print(a > 10 and a < 13)
print(a == 14 and a > 33)

# or operator
apple = 20
print(apple == 21 or apple > 12)
print(apple > 88 or apple < 12)

# not operator
car = 44
print(not car == 44)
print(not car < 44)

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
    elif age >= 45 and age <= 55:
        bill = 0
        print("The ride is on the house")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("Do you want a photo? Y for Yes or N for No")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")


else:
    print("Sorry, you can't go the ride")




