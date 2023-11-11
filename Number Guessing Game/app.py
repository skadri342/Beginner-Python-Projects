from logo import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return set_difficulty()

def check_answer(guess, number):
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {number}")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
number_of_attempts = set_difficulty()
guess = 0
# Let user guess a number
while guess != number:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_answer(guess, number)
    number_of_attempts -= 1
    if number_of_attempts == 0:
        print("You've run out of guesses, you lose.")