import random
import string
import os
from datetime import datetime

NEW_PASSWORD = "new_password.txt"

UPPER_CASE = string.ascii_uppercase
LOWER_CASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation
AMBIGOUS = "iOl10"

def build_character_pool(use_upper, use_lower, use_digits, use_symbols, custom_exclude, exclude_ambigous):
    pool = ''

    if use_upper:
        pool += UPPER_CASE
    
    if use_lower:
        pool += LOWER_CASE
    
    if use_digits:
        pool += DIGITS
    
    if use_symbols:
        pool += SYMBOLS
    
    if custom_exclude:
        pool = "".join(ch for ch in pool if ch not in custom_exclude)
    
    if exclude_ambigous:
        pool = "".join(ch for ch in pool if ch not in AMBIGOUS)
    
    return pool

def generate_password(pool, must_include, length):
    if not pool:
        return None
    
    password_chars = []
    for group in must_include:
        valid = [ch for ch in group if ch in pool]
        if valid:
            password_chars.append(random.choice(valid))

    remaining = length - len(password_chars)
    password_chars += [random.choice(pool) for _ in range(remaining)]

    random.shuffle(password_chars)
    return "".join(password_chars)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    
    if len(password) >= 12:
        score += 1
    
    if len(password) >= 16:
        score += 1
    
    if any(ch in UPPER_CASE for ch in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if any(ch in LOWER_CASE for ch in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if  any(ch in DIGITS for ch in password):
        score += 1
    else:
        feedback.append("Add digits")
    
    if any(ch in SYMBOLS for ch in password):
        score += 2
    else:
        feedback.append("Add Special Characters")
    
    unique_ratio = len(set(password)) / len(password)
    if unique_ratio < 0.5:
        score -= 1
        feedback.append("Too many repititive characters leaves your password vulnerable")

    if score >= 8:
        label = "Very strong"
    
    elif score >= 6:
        label = "strong"
    
    elif score >= 4:
        label = "Moderate"
    
    else:
        label = "Weak"
    
    return score, label, feedback

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('yes', 'y'):
            return True
        elif answer in ('no', 'n'):
            return False
        else:
            print("Enter either Yes or No")

def get_user_input(prompt, min_value, max_value):
    while True:
        try:
            answer = int(input(prompt).strip())
            if min_value <= answer <= max_value:
                return answer
            else:
                print(f"Enter a value between {min_value} and {max_value}")
        except ValueError:
            print("Enter a valid whole number!")

def save_to_history(password, setting_summary):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    with open(NEW_PASSWORD, 'a') as p:
        p.write(f"{'-' * 50}\n")
        p.write(f"Generated on: {timestamp}\n")
        p.write(f"setting: {setting_summary}\n")
        p.write(f"Passwords: \n")
        for i, pw in enumerate(password, start=1):
            p.write(f"{i}. {pw}\n")
    
    print(f"\nPassword has been successfully saved to '{NEW_PASSWORD}'")

def clear_history():
    if os.path.exists(NEW_PASSWORD):
        confirm = get_yes_no("Are you sure you want to clear password history? (Enter Yes/No): ")
        if confirm:
            open(NEW_PASSWORD).close()
            print("Password History has been cleared")
        else:
            print("Operation has been cancelled")
    else:
        print("No password history to clear")

def view_history():
    if not os.path.exists(NEW_PASSWORD):
        print("No history file found!")
        return None
    
    with open(NEW_PASSWORD, 'r') as p:
        content = p.read()
    
    if content.strip() == '':
        print("No content found!")
    else:
        print(content)

def generate_flow():
    print("-" * 30)
    print("  Password Generation:")
    print('-' * 30)

    length =  get_user_input("Password Length(4-30): ", 4, 30)

    count = get_user_input("How many password do you want to create? (1-10): ", 1, 10)

    print("\nPassword features: ")
    use_upper = get_yes_no("Use uppercase letters? (Yes/No): ")
    use_lower = get_yes_no("Use lowercase letters? (Yes/No): ")
    use_digits = get_yes_no("Use Digits? (Yes/No): ")
    use_symbol = get_yes_no("Use Special Characters? (Yes/No): ")
    exclude_ambigous = get_yes_no("Exclude similar characters(IOl10)? (Yes/No): ")
    custom_exclude = input("Do you have any character you wish to omit? (Skip if none): ")

    pool = build_character_pool(use_upper, use_lower, use_digits, use_symbol, custom_exclude, exclude_ambigous)

    if not pool:
        print("Provide more details for your password!")
        return None
    
    must_include = []
    if use_upper: must_include.append(UPPER_CASE)
    if use_lower: must_include.append(LOWER_CASE)
    if use_digits: must_include.append(DIGITS)
    if use_symbol: must_include.append(SYMBOLS)
    if not exclude_ambigous: must_include.append(AMBIGOUS)

    print("\nPassword Geerated: \n")
    generated = []
    for i in range(count):
        pw = generate_password(pool, must_include, length)
        score, label, tip = check_password_strength(pw)
        generated.append(pw)

        print(f"{i+ 1}. {pw}")
        print(f"Score: {score}/10,  Label: {label}")
        if tip:
            print(f"tips: {", ".join(tip)}")
    
    save = get_yes_no("Do you want to save password? Enter (Yes/No): ")
    if save:
        setting_summary = (
            f"Length: {length}, Uppercase: {use_upper}, Lowercase: {use_lower}, "
            f"Numbers: {use_digits}, Special Characters: {use_symbol}"
        )
        save_to_history(generated, setting_summary)
    else:
        return
    
def show_menu():
    print("1. Generate Password")
    print("2. View Password History")
    print("3. Clear Password History")
    print("4. Exit")

def main_menu():
    print('=' * 65)
    print("   Welcome to Korede's Advance Password Generator App")
    print('=' * 65)

    while True:
        show_menu()
        choice = input("Enter the operation you want to perform in (1-4): ").strip()

        if choice == '1':
            generate_flow()
        
        elif choice == '2':
            view_history()
        
        elif choice == '3':
            clear_history()
        
        elif choice == '4':
            print("App closed! \nStay protected out there!")
            break

        else:
            print("Enter a valid number in 1-4")
        
if  __name__ == "__main__":
    main_menu()