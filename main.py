import random

def guess_number_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    attempts = 0
    max_attempts = 3  # You can adjust the number of attempts as needed
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10. Can you guess it?")
    
    while attempts < max_attempts:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            
            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Sorry, that's not the correct number. Try again.")
                attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
guess_number_game()