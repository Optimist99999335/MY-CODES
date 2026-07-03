def display_welcome():
    print('=' * 45)
    print("Korede's Number Guessing game. Second edition")
    print('=' * 45)

def choose_difficulty():
    print('\n' + 'Select Difficult Level')
    print('-' * 45)
    print('1. Easy Mode   (Range 1 - 10)   |   5   Attempts')
    print('2. Medium Mode (Range 1 - 50)   |   7   Attempts')
    print('3. Hard Mode   (Range 1 - 100)  |   10  Attempts')
    print('-' * 45)



    while True:
        
        choice = input('Select Difficulty Level: ')

        if choice == '1':
            return 5, 10, 'Easy'
        
        elif choice == '2':
            return 7, 50, 'Medium'
        
        elif choice == '3':
            return 10, 100, 'Hard'
        
        else:
            print('Select a Valid Operation!')

def give_hint(guess, secret, amounts_left):
    diff = abs(guess - secret)

    if diff == 0:
        return ''
    
    elif diff <= 2:
        proximity = 'Scorching Hot'
        
    elif diff <= 5:
        proximity = 'Very Warm'

    elif diff <= 10:
        proximity = 'Getting Warm'

    elif diff <= 20:
        proximity = 'Cold...'

    else:
        proximity = 'Freezing Cold'

    direction = 'Go Higher' if guess < secret else 'Go Lower'
    return f"{direction}   | {proximity}  | {amounts_left}"



def play_game():
    display_welcome()
    max_attempts, upper_limit, level = choose_difficulty()
    import random
    secret_number = random.randint(1, upper_limit)
    amount_used = 0

    print(f"{level} Mode Selected")
    print(f"You have {max_attempts} attempt(s)")

    while amount_used < max_attempts:

        remaining = max_attempts - amount_used

        try:
            guess = int(input('Make a Guess: '))
        except ValueError:
            print('Error! Enter a Valid whole number')

        if guess < 1 or guess > upper_limit:
            print(f"Out of range! Select a number between 1 and {upper_limit}") 
        

        amount_used += 1

        if guess == secret_number:
            print('=' * 45)
            print("Congratulations!!!")
            print(f"The secert number was {secret_number}")
            print('=' * 45)
            if amount_used == 1:
                print(f"You are a Psychic!!! \nYou got it on your first trial")
            elif amount_used == max_attempts // 2:
                return f"Impressive!!! \nYou guessed Correctly"
            else:
                print('You got it in the end')
                
        else:
            hint = give_hint(guess, secret_number, remaining - 1)
            print('\n' + hint)
    
    print('=' * 45)
    print("Game Over!!!")
    print(f"The secret number was {secret_number}")
    print('Better luck next time')
    print('=' * 45)

def main():
    while True:
        play_game()
      
        again = input('Do you want to play again? (Yes/No)')
        if again not in ['Yes', 'y']:
            print('Thanks for Playing!!!')
            break


if __name__ == '__main__':
    main()