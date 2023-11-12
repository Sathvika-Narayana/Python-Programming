#Internship Task 3

#Password generator

import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not (include_uppercase or include_digits or include_special_chars):
        return "Password must include at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password requirements
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

password = generate_password(length, include_uppercase, include_digits, include_special_chars)
print("Generated password:", password)