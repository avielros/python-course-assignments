import random

sec_num = random.randrange(1, 21)
guess = None
debug_mode = False 
while guess != sec_num:
    if debug_mode:
        print(f"[DEBUG] Secret number is: {sec_num}")

    guess = input("Enter your guess: a number between 1 to 20 (x=quit, s=show, d=debug): ")

    if guess == 'x':
        print("You chose to exit")
        break

    if guess == 's':
        print(f"(you cheat) The secret number is: {sec_num}")
        continue

    if guess == 'd':
        debug_mode = not debug_mode  
        state = "ON" if debug_mode else "OFF"
        print(f"Debug mode is now {state}.")
        continue

    print("You chose: " + guess)

     try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Please enter a number, or x/s/d.")
        continue

    if guess == sec_num:
        print("You are right!")
    elif guess > sec_num:
        print("Too high!")
    else:
        print("Too low!")
