# Exercise Name:
# 	10-wordle
# Description:
# 	Create the wordle game
# Resources:
# 	Valid Words List: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93

import random

def load_word_list(filename):
    with open(filename, 'r') as file:
        words = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return words

def check_guess(secret, guess):
    result = []
    for i in range(5):
        if guess[i] == secret[i]:
            result.append('🟩')
        elif guess[i] in secret:
            result.append('🟨')
        else:
            result.append('⬜')
    return ''.join(result)

def wordle_game():
    word_list = load_word_list(r'D:/Python-Exercises/10-wordle/valid-wordle-words.txt')

    secret_word = random.choice(word_list)
    attempts = 6

    print("Welcome to Wordle! Guess the 5-letter word.")

    while attempts > 0:
        guess = input("Enter your guess: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        if guess not in word_list:
            print("Invalid word. Please try again.")
            continue

        feedback = check_guess(secret_word, guess)
        print(feedback)

        if guess == secret_word:
            print("🎉 Congrats! You guessed it right!")
            return

        attempts -= 1

    print(f"Game Over! The word was: {secret_word}")

if __name__ == "__main__":
    wordle_game()
