"""PASSWORD GENERATOR APP"""
import random
import string

def welcome():
    print('=' * 45)
    print("          A Password Generator App")
    print('=' * 45)

    try:
        length = int(input("\nWhat lenth of password do you want? \nEnter the number: "))
    except ValueError:
        print("Error! Enter a valid whole number")
        exit()
    
    print("\nWhat should your calculator contain? ")
    use_upper = input("Do you want your password to contain uppercase letters(A-Z)? \nEnter (Yes/No): ").lower().strip()
    use_lower = input("Do you want your password to contain lowercase letters (a-z)? \nEnter (Yes/No): ").lower().strip()
    use_digits = input("Do you want your password to contain numbers(0-9)? \nEnter (Yes/No): ").lower().strip()
    use_symbols = input("Do you want your password to contain symbols(%$$ etc.)? \nEnter (Yes/No): ").lower().strip()

    character = ''
    if use_upper == 'yes':
        character = character + string.ascii_uppercase
    
    if use_lower == 'yes':
        character = character + string.ascii_lowercase

    if use_digits == 'yes':
        character = character + string.digits
    
    if use_symbols == 'yes':
        character = character + string.punctuation
    
    if character == '':
        print("Provide more details for your password!")
        exit()
    
    else:
        password = ''
        for i in range(length):
            random_password = random.choice(character)
            password = password + random_password
    
    print('-' * 45)
    print(f"Your generated password is: {password}")
    print('-' * 45)
    print('\nKeep it safe!')

if __name__ == "__main__":
    welcome()