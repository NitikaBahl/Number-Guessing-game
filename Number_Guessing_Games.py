import random

print("Welcome to the number guessing game!\nYou have 7 chances to guess the correct number.\n")

# Randomly select a number between 1 and 100
number_to_guess = random.randint(1, 100)
guess_counter = 0
chances = 7

while guess_counter < chances:
    guess_counter += 1
    guess = int(input(f"Chance {guess_counter}/{chances} - Enter your guess: "))

    if guess == number_to_guess:
        print(f"🎉 Congratulations! You guessed the correct number: {number_to_guess}.")
        break
    elif guess > number_to_guess:
        print("❌ Too high! Try guessing a lower number.")
    elif guess < number_to_guess:
        print("❌ Too low! Try guessing a higher number.")

    if guess_counter == chances:
        print(f"💔 Sorry, you've used all your chances. The correct number was {number_to_guess}.")