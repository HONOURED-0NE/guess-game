import random
print("Numnber guessing game\nI'm thinking of a number between 1 and 100.")
var = random.randint(1 ,100)
difficulty = input("What difficulty do you want?:\n").lower()
print(f"psst, the number is {var}")
num_guess = 0
if difficulty == "hard":
    num_guess = 5
    print(num_guess)
elif difficulty == "easy":
    num_guess = 10
number = input(f"You have {num_guess} guesses left\nGuess a number:\n")

while num_guess > 0 :
    if number == var:
        print("Yay, you guessed correctly")
        num_guess = 0
    else:
        print("Wrong guess.")
        if num_guess > var:
            print("Too high")
        elif num_guess < var:
            print("Too low")
        num_guess -= 1
        number = input(f"You have {num_guess} guesses left\nGuess a number:\n")
