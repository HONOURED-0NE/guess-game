import random
print("Numnber guessing game\nI'm thinking of a number between 1 and 100.")
var = random.randint(1 ,100)
difficulty = input("What difficulty do you want?:\n").lower
if difficulty == "hard":
    num_guess = 5
elif difficulty == "easy":
    num_guess = 10
number = input(f"You have {num_guess} guesses left\nGuess a number:\n")

while num_guess > 0 :
    if number == var:
        print("Yay, you guessed correctly")
        num_guess = 0
    else:
        print("Wrong guess.")
        num_guess -= 1
        number = input(f"You have {num_guess} guesses left\nGuess a number:\n")
