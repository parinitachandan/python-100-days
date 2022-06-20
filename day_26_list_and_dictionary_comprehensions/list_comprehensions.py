# list comprehension
numbers = [1, 2, 3, 4]
new_num_list = [n + 1 for n in numbers]
print(new_num_list)

# string as list
character = "Jerry"
character_list = [letter for letter in character]
print(character_list)

# range as list
range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# Conditional list comprehension
names = ["Alex", "Beth", "Hailey", "DJ", "Kimmy"]
names_list = [name.upper() for name in names if len(name) < 5]
print(names_list)