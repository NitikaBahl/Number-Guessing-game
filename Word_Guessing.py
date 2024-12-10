import random

# Welcome message and input
name = input("What is your name? ")
print(f"Welcome {name}! Good luck with the word guessing game. You have 10 guesses in total.")

# Word pool and initialization
words = ["guess", "name", "manifesto", "dead", "print", "gallon", "dark", "reality", "fantastic", "hello", "weather", "opposite"]
word = random.choice(words)  # Randomly select a word
turns = 10
guessed_letters = set()  # Keep track of guessed letters

# Main game loop
while turns > 0:
    # Display the word with guessed letters
    display_word = ''.join([char if char in guessed_letters else '_' for char in word])
    print(f"\nWord: {display_word}")

    # Check if the user has guessed the word
    if '_' not in display_word:
        print(f"Congratulations {name}! You guessed the word: {word}")
        break

    # Take a guess
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    # Update guessed letters
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.add(guess)

    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        turns -= 1
        print(f"Wrong guess! You have {turns} guesses left.")

# If user runs out of turns
if turns == 0:
    print(f"you loose!, since you are out of guesses. The word was: {word}")