import random

def guess_number_game():
    # this generates a random number between like 1 and 10 wowzers  
    secret_number = random.randint(1, 10)
    
    attempts = 0
    max_attempts = 3  
    invalid_input_count = 0
    max_invalid_inputs = 3  
    
    print("welcome, i chose a number between 1 and 10. try to guess it")
    
    while attempts < max_attempts:
        try:
            # this gets users guess
            guess = int(input("input your guess: "))
            
            # is the guess correct or not
            if guess == secret_number:
                print("hey good job")
                break
            else:
                print("not correct, try again.")
                attempts += 1
        except ValueError:
            invalid_input_count += 1
            print("thats not a correct input, only input numbers.")
            
            # checks if the player reached max invalid inputs
            if invalid_input_count == max_invalid_inputs:
                print(f"the game ended because you put too much invalid inputs.. what the actual hell")
                break
    
    if attempts == max_attempts:
        print(f"sorry. you ran outta attempts!! the correct number was {secret_number}.")

# Run the game
guess_number_game()