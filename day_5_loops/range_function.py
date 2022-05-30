for number in range(0, 11, 3):
    print(number)

total = 0
for no in range(1, 101):
    total += no
print(total)

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)