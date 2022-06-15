import random


def guessing_game():
    answer = random.randint(10, 30)
    remaining_guesses = 3

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input("What is your guess? "))
        remaining_guesses -= 1

        if user_guess == answer:
            print(f"Right! The answer is {user_guess}")
            break
        elif user_guess < answer:
            print(f"Your guess of {user_guess} is too low!")
        else:
            print(f"Your guess of {user_guess} is too high!")
            
    else:
        print("Oops! You chances are up!")


guessing_game()
