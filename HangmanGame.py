import random

# Step 1: Predefined word list
word_list = ["apple", "banana", "orange", "grape", "mango"]

# Step 2: Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Step 3: Game variables
display = ["_"] * word_length
lives = 6
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(display))

# Step 4: Main game loop
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'!")
        continue

    guessed_letters.append(guess)
    
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
    
    print(" ".join(display))

# Step 5: End of game
if "_" not in display:
    print(f"Congratulations! You guessed the word '{chosen_word}'!")
else:
    print(f"Game over! The word was '{chosen_word}'.")
