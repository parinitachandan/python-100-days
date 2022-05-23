# Changing a piece of data from one particular data type to another
# also known as type casting

'''
no_char = len(input("What is your name?)")
print("Your name has " + no_char + " characters.")

it gives you a type error; because you can't add strings and integers together
'''

no_char = len(input("What is your name?"))
new_no_char = str(no_char)         # type conversion
print("Your name has " + new_no_char + " characters.")
