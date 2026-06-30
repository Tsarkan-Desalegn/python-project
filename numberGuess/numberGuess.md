# Number Guessing Game

The number guessing game is a programming project used to demonstrate concepts such as number generation, loops, conditional statements, and user interaction.  
The program randomly selects a number from a user-defined range and guides the player toward the correct answer by indicating whether each guess is higher or lower than the target number.

## How the Game Works

Example: Suppose the user chooses the upper bound **100** and lower bound **1**.  
Therefore, the number range is between 1 and 100. The system randomly selects **60** as the target number, and you have **7 chances** to attempt.  
The guessing process might look like this:

- Guess 1: 50 → The number is too low  
- Guess 2: 75 → The number is too high  
- Guess 3: 56 → The number is too low  
- Guess 4: 64 → The number is too high  
- Guess 5: 59 → The number is too low  
- Guess 6: 62 → The number is too high  
- Guess 7: 60 → Correct! 

## Algorithms to Write the Program

1. Read the lower and upper bounds from the user.  
2. Generate a random number between the specified bounds.  
3. Repeatedly accept guesses from the user until the maximum number of attempts is reached.  
4. Indicate whether each guess is too high or too low.  
5. Stop the game when the correct number is guessed and display the result.  
6. If the user fails to guess the number, display the correct answer and a game-over message.

## Installation 
1. Clone the repository 
````bash
git clone git@github.com:Tsarkan-Desalegn/python-project.git
````
2. Navigate into the folder
````bash
cd python-project
````
3. Navigate into the folder where the program is found 
````bash
cd numberGuess
````
4 Run the program 
````bash
python guess.py
````