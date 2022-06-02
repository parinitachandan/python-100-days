# Decryption

from art import alphabets

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""   # Empty string
    for letter in plain_text:        # Looping through plain_text
        position = alphabets.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabets[new_position]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""    # Empty string
    for letter in cipher_text:      # Looping through cipher_text
        position = alphabets.index(letter)
        new_position = position - shift_amount
        plain_text += alphabets[new_position]
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid Input, As you haven't used 'encode' or 'decode'")
