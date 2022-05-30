import random

# For integers
random_integer = random.randint(0,10)
print(random_integer)

# For floating points (b/w 0 & 1)
random_float = random.random()
print(random_float)

# For floating points (b/w other nos.)
# it is from 0.000000..... to 4.9999.... (0 to 5)(doesn't include 5)
random_float_2 = random.random()
print(random_float_2 * 5)

print(random_float_2 * 8)

# shuffle
fruits = ["Cherry", "Mango", "Orange", "Blackberry"]
random.shuffle(fruits)
print(fruits)

numbers = ["One", "Eleven", "Thirty", "Hundred", "Fifty five"]
print(random.choice(numbers))






