import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:  " ))
        if guess < random_number:
            print("Wrong, pick a higher number ")
        elif guess > random_number:
            print(" Wrong, pick a lower number ")

    print(" You guessed right")

guess(10)


def computer_guess():
    low = int(input("Enter your lower range:  "))
    high = int(input("Enter your higher range: "))
    
    feedback = ""
    while feedback != "c":
        if low != high:
            computer_choice = random.randint(low, high)
        else:
            print("Error!! \
             your range cannot be the same value")

        feedback = input(f"Is {computer_choice} too high (h), too low (l), or correct(c)?;  ").lower()
        if feedback == "h":
            high = computer_choice -1
        elif feedback == "l":
            low = computer_choice +1
    print(f"congratulations!!, your guess {computer_choice } was correct")

computer_guess()