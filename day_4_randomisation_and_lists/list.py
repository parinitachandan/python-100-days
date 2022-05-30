states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Gao", "Gujarat", "Haryana",
                   "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
                   "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
                   "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                   "Uttarakhand", "West Bengal"]
print(states_of_india[0])     # [0] also known as offset or index
print(states_of_india[-1])
print(states_of_india[-10])
'''print(states_of_india[100]) - gives an index error'''


fruits = ["Cherry", "Mango", "Orange", "Blackberry"]
print(fruits)
print(" ")
# Changing an item in the list
fruits[2] = "Apple"
print(fruits)
print(" ")

# adding a single item to the list
fruits.append("Banana")
print(fruits)
print(" ")

# adding many items to the list
fruits.extend(["Blueberry", "Strawberry", "Kiwi"])
print(fruits)
print(" ")

# inserting an item at a given position
fruits.insert(0, "Watermelon")
print(fruits)
print(" ")

# removing an item
fruits.remove("Apple")
print(fruits)
print(" ")

# pop
fruits.pop(0)
print(fruits)
print(" ")

fruits.pop() # if no index, removes the last item
print(fruits)
print(" ")

# reverse
fruits.reverse()
print(fruits)
print(" ")


# clear
"""fruits.clear("Kiwi")
 fruits.clear("Kiwi")
TypeError: clear() takes no arguments (1 given)"""
fruits.clear()
print(fruits)

