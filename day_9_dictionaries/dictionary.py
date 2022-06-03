programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
# {"Key": "Value"} -  dictionary

print(programming_dictionary)

# Retrieving an item from dictionary
print(programming_dictionary["Bug"])    # should use Key for dictionaries; it returns the value assigned to the Key

# Adding an item to the dictionary
programming_dictionary["Loop"] = "A loop allows us to execute the same line of code multiple times"
print(programming_dictionary)

# Creating an empty dictionary
empty_dict = {}

# Editing an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary)






