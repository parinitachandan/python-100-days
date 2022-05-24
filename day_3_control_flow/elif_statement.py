# The elif keyword is pythons way of saying "if the previous conditions was not true, then try this condition"
# Stands for else if


'''
Kids with age 10 or above and height 120 cm or above should be allowed in the park
For kids of age 10 to 12 - 5$
For kids of age 13 to 18 - 15$
For people 19 and above - 25$
'''

print("Welcome to the sky line")
height = int(input("What is your height(in cm)?"))
if height >= 120:
    print("You can go on the ride!")
    age = int(input("What is your age?"))
    if age < 12:
        print("You need to pay $5")
    elif age <= 18:
        print("You need to pay $7")
    else:
     print("You need to pay $12")
else:
     print("Sorry, you can't go the ride")