<div align="center">
  
# 🎮 Hangman Game

</div>

<h2>A simple command-line Hangman game built using Python where the player guesses a hidden word within limited attempts.</h2>

## 📌 Description

```
This project is a Python-based implementation of the classic Hangman game. The program randomly selects a word from a predefined list, and the player attempts to guess it letter by letter.

For each incorrect guess, a part of the hangman is drawn. The game continues until the player either guesses the word correctly or reaches the maximum number of wrong attempts.

The application also includes input validation and prevents repeated guesses to ensure smooth gameplay.

```
🚀 Features
---------

```
*User vs System gameplay
*Random word selection
*ASCII-based hangman visualization
*Input validation (only single letters allowed)
*Duplicate guess detection
*Win / Loss result display

```

## 🛠️ Technologies Used
----------

```
*Python 3
*Built-in random module

```

## 📂 Project Structure
-----------

```

hangman/
│── hangman.py
│── README.md
|──hangman_output.png

```

## ▶️ How to Run the Program
------------

1.Clone the repository:

```
git clone https://github.com/sathvikamareddy/hangman.git

```
2.Navigate to the project folder:

```
cd hangman

```
3.Run the program:

```
python hangman.py

```


## 🎮 Game Rules

```
The system selects a random word
The player guesses one letter at a time
Each incorrect guess adds to the hangman drawing
The game continues until the word is guessed or attempts run out
Maximum incorrect attempts allowed: 6

```
## 🖥️ Example Output


```
🎮 WELCOME TO HANGMAN

   -----
   |   |
       |
       |
       |
       |
---------
Word: _ _ _ _ _ _
Enter a letter:

```
## 🧠 Concepts Used

```
Functions
Loops
Conditional statements
Lists & Strings
Input validation
Random module usage

```
## 📈 Future Improvements

```
Add GUI version (Tkinter / Pygame)
Add difficulty levels
Score tracking system
Multiplayer mode

```
