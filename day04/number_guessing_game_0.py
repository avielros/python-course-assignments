import random

sec_num = random.randrange(1, 21)

guess = input("Enter your guess: a number between 1 to 20: ")
print("You chose: " + guess)

guess = int(guess)

if guess == sec_num:
    print("You are right!")
elif guess > sec_num:
    print("Too high!")
else:
    print("Too low!")
