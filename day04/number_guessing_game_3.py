import random

sec_num = random.randrange(1, 21)
guess = None

while guess != sec_num:
    guess = input("Enter your guess: a number between 1 to 20 (or 'x' to quit, 's' to show the secret number): ")

    if guess == 'x':
        print("You chose to exit")
        break

    if guess == 's':
        print(f"(you cheated) The secret number is: {sec_num}")
        continue  

    print("You chose: " + guess)
    guess = int(guess)

    if guess == sec_num:
        print("You are right!")
    elif guess > sec_num:
        print("Too high!")
    else:
        print("Too low!")
