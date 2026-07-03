# ================================
#     PASSWORD GENERATOR
# ================================

import random
import string

print("Welcome to the Password Generator!")
print("===================================")

# Ask the user how long they want the password
length = input("How long do you want your password? Enter a number: ")
length = int(length)

# Ask what to include
print("\nWhat should the password contain?")
use_letters = input("Include letters? (yes/no): ")
use_numbers = input("Include numbers? (yes/no): ")
use_symbols = input("Include symbols? (yes/no): ")

# Build the character pool based on user choices
characters = ""

if use_letters == "yes":
    characters = characters + string.ascii_letters  # a-z and A-Z

if use_numbers == "yes":
    characters = characters + string.digits          # 0-9

if use_symbols == "yes":
    characters = characters + string.punctuation     # !@#$%^&* etc.

# Check if the user selected at least one option
if characters == "":
    print("\nYou didn't select anything! Please run the program again.")

else:
    # Generate the password
    password = ""

    for i in range(length):
        random_character = random.choice(characters)
        password = password + random_character

    print("\nYour generated password is:")
    print("---------------------------")
    print(password)
    print("---------------------------")
    print("Keep it safe!")