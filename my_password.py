import random
import string
import os
from datetime import datetime

PAS_HIS = "pas_his.txt"

UPPER_CASE = string.ascii_uppercase
LOWER_CASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation
AMBIGOUS = "IOl01"

def build_character_pool(use_upper, use_lower, use_digits, use_symbols, custom_exclude, exclude_ambigous):
    #Generates the password content
    pool = ''

    if use_upper:
        pool += UPPER_CASE
    
    if use_lower:
        pool += LOWER_CASE
    
    if use_symbols:
        pool += SYMBOLS
    
    if use_digits:
        pool += DIGITS
    
    if exclude_ambigous:
        pool = "".join(ch for ch in pool if ch not in AMBIGOUS)

    if custom_exclude:
        pool  = "".join(ch for ch in pool if ch not in custom_exclude)
    
    return pool

def generate_password(pool, must_include, length):
    if not pool:
        return None
    
    #Password generation starts here. This ensures that must include items like uppercase etc are included in the password
    Password_chars = []
    for group in must_include:
        valid = [ch for ch in group if ch in pool]
        if valid:
            Password_chars.append(random.choice(valid))
    
    #this helps to fill in the remaining lengt of password with items from pool
    remaining = length - len(Password_chars)
    Password_chars += [random.choice(pool) for _ in range(remaining)]
    random.shuffle(Password_chars)
    return "".join(Password_chars)

def check_strength(password):
    score = 0
    feedback = []
    
    #This rates the strength of the password based on the length
    if len(password) >= 8:
        score += 1
    
    if len(password) >= 12:
        score += 1
    
    if len(password) >= 16:
        score += 1
    
    #This rates the strength of the password based on attributes such as uppercase etc.
    if any(ch in UPPER_CASE for ch in password):
        score += 1
    else:
        feedback.append("Add upper case letters to your password to increase the strength")
    
    if any(ch in LOWER_CASE for ch in password):
        score += 1
    else:
        feedback.append("Add lower case letters to your password to increase the stregth")
    
    if any(ch in DIGITS for ch in password):
        score += 1
    else:
        feedback.append("Add digits (0-9) to increase the strength of your password")
    
    if any(ch in AMBIGOUS for ch in password):
        score += 1
    else:
        feedback.append("Add ambigous characters(I0l1O) to increase the password strength")
    
    if any(ch in SYMBOLS for ch in password):
        score += 2
    else:
        feedback.append("Add symbols(*&^...) to increase your password strength")
    
    #check for repititive characters
    unique_ratio = len(set(password)) / len(password)
    if unique_ratio < 0.5:
        score -= 1
        feedback.append("Too many repititive characters leaves your password vulnerable")
    
    #Key for rating password strength
    if score >= 8:
        label = "Very strong"
    
    elif score >= 6:
        label = "Strong"
    
    elif score >= 4:
        label = "Password strength is manageable"
    
    else:
        label = "Weak"
    
    return score, label, feedback

def get_yes_no(prompt):
    #A prompt designed specifically to get either a yes or no response from the user
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('yes', 'y'):
            return True
        elif answer in ('no', 'n'):
            return False
        else:
            print("Enter Yes or No to proceed")

def clear_history():
    #The main function of this code is to clear the password history
    if os.path.exists(PAS_HIS):
        confirm = get_yes_no("Are you sure you want to clear your password history? Enter (Yes/No)")
        if confirm:
            with open(PAS_HIS).close():
                print("Password History has been deleted!")
        else:
            print("Operation cancelled!")
    else:
        print("No history file to delete!")

def save_to_history(password, setting_summary):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    with open(PAS_HIS, 'a') as p:
        p.write(f"\n")
        p.write(f"{"-" *50}\n")
        p.write(f"Generated on: {timestamp}\n")
        p.write(f"setting: {setting_summary}\n")
        p.write(f"Password:  \n")
        for i, pw in enumerate(password, start=1):
            p.write(f"{i}. {pw}\n")

    print(f"Password(s) saved to {PAS_HIS}")

def view_history():
    #The main function of this code is to view the content in the password history
    if not os.path.exists(PAS_HIS):
        print("History file not found!")
        return
    
    with open(PAS_HIS, 'r') as p:
        content = p.read()
    
    if content.strip() == '':
        print("History file is empty!")
    
    else:
        print(content)
    
def get_user_input(prompt, min_value, max_value):
    #This code is designed to get the a specific number from the user while also checking if it is in the range of the highest and lowest number
    while True:
        try:
            answer = int(input(prompt).strip())
            if min_value <= answer <= max_value:
                return answer
            else:
                print(f"Please enter a number between {min_value} and {max_value}")
        except ValueError:
            print("Enter a valid whole number")

def generate_flow():
    print('-' * 45)
    print("  Password Generation flow")
    print('-' * 45)

    #This helps us to get the length of password from the user
    length = get_user_input("Enter the length of your password(4-30): ", 4, 30)

    #This helps the code knows how many password the user wants to create
    count = get_user_input("How many password(s) do you want to generate?(1-10): ", 1, 10)

    #This asks the user about the content of the password such as uppercase letters etc
    print("\nWhat should your password contain?")
    use_upper = get_yes_no("Do you want to include upper case letters(A-Z) in your password? (Yes/No): ")
    use_lower = get_yes_no("Do you want to include lower case letters (a-z) in your password? (Yes/No): ")
    use_digits = get_yes_no("Do you want to include numbers (0-9) in your password? (Yes/No): ")
    use_symbols = get_yes_no("Do you want to include special characters(*&^...) in your password? (Yes/No): ")
    exclude_ambigous = get_yes_no("Do you want to exclude similar characters(IOl10) from your password? (Yes/No): ")
    custom_exclude = input("Do you have any characters that you wish to leave out from your password? (Skip if there is none): ").strip()

    pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols, custom_exclude, exclude_ambigous)

    if not pool:
        print("Provide more details for your password creation")
        return None
    
    must_include = []
    if use_upper: must_include.append(UPPER_CASE)
    if use_lower: must_include.append(LOWER_CASE)
    if use_digits: must_include.append(DIGITS)
    if use_symbols: must_include.append(SYMBOLS)
    
    #The password creation starts here
    print("Creating password")
    generated = []
    for i in range(count):
        pw = generate_password(pool, must_include, length)
        score, label, tips = check_strength(pw)
        generated.append(pw)

        print(f"{i + 1}. {pw}")
        print(f"score: {score}/10    label: {label}")
        if tips:
            print(f"tips: {", ".join(tips)}")
    
    save = get_yes_no("Do you want to save to history? (Yes/No): ")
    if save:
        setting_summary = (
            f"Length = {length}, Uppercase letters = {use_upper}, Lowercase letters = {use_lower} "
            f"Numbers = {use_digits}, Special Characters = {use_symbols} "
        )
        save_to_history(generated, setting_summary)

def show_menu():
    print("1. Generate Password")
    print("2. View Password History")
    print("3. Clear Password History")
    print("4. Exit")

def main_menu():
    print('=' * 60)
    print("   Welcome to Korede's Advance Password Generator App")
    print('=' * 60)
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
            print("Password App closed. \nStay protected!")
            break

        else:
            print("Enter a valid number in (1-4)")
        

if __name__ == "__main__":
    main_menu()