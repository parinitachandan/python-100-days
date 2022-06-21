"""
1) File Not Found Error:
with open("a_file.txt") as file
    print("hello")

Error given:
with open("a_file.txt") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

2) Type Error
text = "abc"
print(text + 5)

Error given:
print(text + 5)
TypeError: can only concatenate str (not "int") to str
"""


try:
    file = open("a_file.txt")
    dic = {"Key": "Value"}
    print(dic["kk"])
except FileNotFoundError:
    file = open("a_file.txt",mode="a")
    file.write("Hello")
except KeyError as error_message:
    print(f"The Key {error_message} doesn't exist")
else:
    print("There is an error in your code.Please check.")
finally:
    content = file.readline()
    print(content)
    file.close()


height = float(input("What is your height?: "))

if height < 5:
    raise ValueError("Height should not be less than 5cm.")
