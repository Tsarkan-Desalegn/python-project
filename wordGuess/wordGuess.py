import random

name = input("What is your name: ")
print("Good luck!", name)

wordList = ['rainbow', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'reverse', 'water', 'board', 'geeks']
selectFromList = random.choice(wordList)

guessedChar = []
counter = 12
lengthOfList = len(selectFromList)

print("Guess the word")
print("_" * lengthOfList)

while counter > 0:
    charFromUser = input("Guess a letter: ")
    if charFromUser in selectFromList:
        if charFromUser not in guessedChar:
            guessedChar.append(charFromUser)
        else:
            print("You already guessed that letter!")

        displayWord = ""
        for char in selectFromList:
            if char in guessedChar:
                displayWord += char
            else:
                displayWord += "_"
        print(displayWord)

        if "_" not in displayWord:
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        counter -= 1
        print(f"That is not correct. You have {counter} tries left.")
        break

print("Better luck next time! The word was:", selectFromList)
