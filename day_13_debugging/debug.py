"""
# Describe Problem - Question
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it") - it doesn't print this out because range function only goes from 1 to 19
my_function()
"""


# Describe Problem - Solution
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

"""
# Reproduce the Bug
from random import randint 
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] 
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# We get an index error occasionally, when the dice_num tries to get hold of the 6th item in the list, which doesn't 
exist. The error is given only when we try to get the hold of the 6th item. 
"""

# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

"""# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millennial.")
elif year > 1994:
  print("You are a Gen Z.")
  
# When you give the input 1994; it prints nothing
"""
# Play Computer
year = int(input("What's your year of birth?\n"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

"""
# Fix the Errors
age = input("How old are you?")
if age > 18:
  print("You can drive at age {age}.")
  
# TypeError: '>' not supported between instances of 'str' and 'int'
"""

# Fix the Errors
age = int(input("How old are you?\n"))
if age > 18:
    print(f"You can drive at age {age}.")

"""
# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # has two equal signs
total_words = pages * word_per_page
print(total_words) # prints 0
"""
# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# print(pages)
word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
total_words = pages * word_per_page
print(total_words)

"""
#Use a Debugger
def mutate(a_list):
   b_list = []
   for item in a_list:
    new_item = item * 2
   b_list.append(new_item) # should be inside the for loop
   print(b_list)           # should be inside the for loop

mutate([1,2,3,5,8,13])
"""


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
        print(b_list)


mutate([1, 2, 3, 5, 8, 13])
