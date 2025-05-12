# Exercise Name:
# 	07-Hangman-CLI
# Description:
# 	Create a hangman CLI game
# Rough game logic:
# 	1. Pick a random word. (Initially just use a hardcoded word like 'watermelon'. Random selection can be done later.)
# 	2. Initialize Guess Count to 6
# 	3. Show one underscore for each character in the word. For example, in case of 'watermelon', show 10 underscores like: _ _ _ _ _ _ _ _ _ _ 
# 	4. Prompt user to input their guess
# 		- Show a sorted list of already guessed characters
# 		- Guess should be ONE character from the alphabet
# 		- Guessed character should be new and not have been previously guessed
# 	5. Check if that character exists in the selected word
# 		a. If the character exists, reveal the character in its position. 
# 		   For example, in case of 'watermelon' and user guessed 'e', show: _ _ _ e _ _ e _ _ _
# 		b. If the character does not exist in the selected word, show warning and decrement Guess Count by one
# 	6. If the Guess Count
# 		a. is greater than zero, loop and take another input
# 		b. becomes zero before guessing all the characters in the word, Game Over.
# For improvement:
# 	https://random-word-api.herokuapp.com/word

def hangman():
    word = "watermelon"
    word = word.lower()
    guessed = set()
    correct_guesses = set()
    guess_count = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while guess_count > 0:
        print("\nGuessed letters:", sorted(guessed))
        display = [letter if letter in correct_guesses else '_' for letter in word] 
        print("Current word: " + ' '.join(display))

        if set(word) == correct_guesses:
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("Enter your guess (a single alphabet letter): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter. Try another.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Good guess!")
            correct_guesses.add(guess)
        else:
            guess_count -= 1
            print(f"Wrong guess! You have {guess_count} tries left.")

    else:
        print("\nGame Over! The word was:", word)

hangman()
