import random
upperBound = int(input("Enter the upper bound number: "))
lowerBound = int(input("Enter the lower bound number: "))
print("You have 7 chances to try. Enter your attempt:")
maxAttempt = 7
targetGuess = random.randint(lowerBound, upperBound)
counter = 0
while counter <= maxAttempt:
    acceptGuess = int(input("Enter your guess: "))
    if acceptGuess == targetGuess:
        print("You have successfully guessed the number!")
        break
    elif acceptGuess > targetGuess:
        print("The number is too high!")
    elif acceptGuess < targetGuess:
        print("The number is too low!")
    counter += 1
    continue

if counter > maxAttempt:
    print("The target number was", targetGuess)
    print("Try again next time, good luck!")

