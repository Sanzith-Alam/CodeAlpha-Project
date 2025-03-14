import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'computer', 'algorithm']
    
    word = random.choice(words)

    max_attempts = 6
    attempts = 0

    guessed_letters = set()

    current_word = ['_' for _ in word]
    
    print("Welcome to Hangman!")
    print(" ".join(current_word))
    
    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")

            for i, letter in enumerate(word):
                if letter == guess:
                    current_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts += 1
        print(" ".join(current_word))

        if "_" not in current_word:
            print("Congratulations! You've guessed the word:", word)
            break

        print(f"Attempts remaining: {max_attempts - attempts}")

    if attempts == max_attempts:
        print("You've run out of attempts. The word was:", word)
        
hangman()
