# Python number guessing game

import random

lowest_num = 1
highest_num = 100
guesses = 0
is_playing = True

number = random.randint(lowest_num, highest_num)

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_playing:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Number out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        elif guess < number:
            print("Too low, guess again")

        elif guess > number:
            print("Too high, guess again")

        else:
            print("Correct!!!")
            print(f"The number was {number}")
            print(f"Number of guesses: {guesses}")
            is_playing = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
