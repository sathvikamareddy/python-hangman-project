import random

# word list
words = [
    "python", "hangman", "computer", "science",
    "developer", "keyboard", "algorithm", "network"
]

# hangman stages
hangman_art = [
"""
   -----
   |   |
       |
       |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
       |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
   |   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\  |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
---------
"""
]

def hangman():
    
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("🎮 WELCOME TO HANGMAN")

    while wrong_guesses <= max_wrong:

        print(hangman_art[wrong_guesses])

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)

        if "_" not in display_word:
            print("🎉 YOU WIN!")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        if wrong_guesses == max_wrong:
            print(hangman_art[wrong_guesses])
            print("💀 YOU LOST!")
            print("The word was:", word)
            break


if __name__ == "__main__":
    hangman()
