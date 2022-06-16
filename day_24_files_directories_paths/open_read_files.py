"""
file = open("my_file.txt")  # opens the file
content = file.read()       # reads the content in the file
print(content)              # prints the content
file.close()                # closes the file (else takes up space/resources);thus we have to tell it manually
"""

# Over here we don't need to tell python manually to close the file
with open("my_file.txt") as files:   # the mode here to open the file is read(r) which is default
    contents = files.read()
    print(contents)

with open("my_file.txt", mode="a") as file:   # the mode here as been set to write(w)
    content = file.write("\nI'm currently learning python.\n"
                         "This Day 18 of learning python.")




