PLACEHOLDER = "[name]"

with open("./input/name/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./input/letter/starting_letter.txt") as letter_file:
    content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, name)
        print(new_letter)
        with open(f"./Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
           completed_letter.write(new_letter)

