'''
YEAR 1: COMPUTER SCIENCE, ASSIGNMENT on Tue 05 Sept 2023
1. MUGWANEZA MANZI Audace, 233010386
2. IMANISHIMWE MARIE Irene, 223013162
3. MFITUMURENGEZI Danny, 223009207
'''
import random

def get_word():
    words = ["science", "technology", "handsome", "game", "college"]
    return random.choice(words)

def play_hangman():
    word = get_word()
    display_word = "-" * len(word)
    
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    
    vowels = "aeiou"
    
    print("Welcome to Hangman!")
    print("Guess the word by entering one character at a time.")
    
    while guesses_remaining > 0:
        print("\n==============================")
        print(f"Word: {display_word}")
        print(f"Guesses remaining: {guesses_remaining}")
        print(f"Warnings remaining {warnings_remaining}")
        print(f"Letters yet used: {', '.join(set(letters_guessed)) if letters_guessed else 'None'}")
        
        guess = input("Enter your guess: ").lower()
        
        if guess.isalpha() and len(guess) == 1:
            if guess in letters_guessed:
                print("You've already guessed that letter!")
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                else:
                    guesses_remaining -= 1
            else:
                letters_guessed.append(guess)
                
                if guess in word:
                    for i in range(len(word)):
                        if word[i] == guess:
                            display_word = display_word[:i] + guess + display_word[i+1:]
                    
                    if display_word == word:
                        print("\nCongratulations! You won!")
                        score = guesses_remaining * len(set(word))
                        print(f"Your score is: {score}")
                        return
                else:
                    if guess in vowels:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                
        else:
            print("Invalid input. Please enter a single letter.")
            if warnings_remaining > 0:
                warnings_remaining -= 1
            else:
                guesses_remaining -= 1
    
    print("\nGame over! You lost.")
    print(f"The word was: {word}")
get_word()
play_hangman()
