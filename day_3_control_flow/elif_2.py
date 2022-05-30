'''
Kids with age 10 or above and height 120 cm or above should be allowed in the park
For kids of age 10 to 12 - 5$
For kids of age 13 to 18 - 15$
For people 19 and above - 25$


Height:
    - Positive Numbers... Negative numbers throw/print error
    - Less than 120 cm not allowed into park.
    - 120 cm or above allowed into part
Age:
    - Positive Numbers... Negative numbers throw/print error
    - Less than 10 not allowed into park.
    - 10 or above allowed into park.

Billing:
    - For kids of age 10 to 12 - 5$
    - For kids of age 13 to 18 - 15$
    - For people 19 and above - 25$
'''

print("Welcome to the ride")
height = input("What is your height in cm?")
age = input("What is your age?")

if int(height) < 0:
    print("Invalid Input, Height can't be negative")
if int(age) < 0:
    print("Invalid Input, Age can't be negative")

if int(height) >= 120 and int(age) >= 10:

    if int(age) >= 10 and int(age) <= 12:
        print("You need to pay $5")
    elif int(age) >=13 and int(age) <= 18:
        print("You need to pay $15")
    else:
        print("You need to pay $25")
else:
    print("Sorry, You can't go no the ride.")

# /=
a = 22
a /= 2
print(a)

# *=
b = 10
b *= 22
print(b)
