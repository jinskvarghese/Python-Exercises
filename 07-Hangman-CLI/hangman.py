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
