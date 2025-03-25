import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts_left = 10
        break
    elif difficulty == "hard":
        attempts_left = 5
        break
    else:
        print("Enter correct input (easy or hard)")

while attempts_left > 0:
    print(f"You have {attempts_left} attempts remaining to guess the number.")
    try:
        user_input = int(input("Make a guess: "))
        if user_input > number:
            print("Too high")
            attempts_left -= 1
            if attempts_left > 0:
                print("Guess again")
        elif user_input < number:
            print("Too low")
            attempts_left -= 1
            if attempts_left > 0:
                print("Guess again")
        elif user_input == number:
            print(f"You Win! The number was {number}")
            break
    except ValueError:
        print("Please enter a valid number")
        attempts_left -= 1
        continue

if attempts_left == 0:
    print(f"Game Over! The number was {number}")
