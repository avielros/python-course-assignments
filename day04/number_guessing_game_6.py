import random

debug_mode = False
move_mode = False

while True:
   sec_num = random.randrange(1, 21)
    guess = None
    print("\nNew game started! Guess the number between 1 and 20.")

    while guess != sec_num:
        if debug_mode:
            print(f"[DEBUG] Secret number is: {sec_num}")

        guess = input("Enter your guess (x=quit, s=show, d=debug, m=move mode, n=new game): ")

        if guess == 'x':
            print("You chose to exit. Goodbye!")
            exit()

        if guess == 'n':
            print("Skipping current game, starting a new game!")
            break

           if guess == 's':
            print(f"(you cheat) The secret number is: {sec_num}")
            continue

        if guess == 'd':
            debug_mode = not debug_mode
            state = "ON" if debug_mode else "OFF"
            print(f"Debug mode is now {state}.")
            continue

        if guess == 'm':
            move_mode = not move_mode
            state = "ON" if move_mode else "OFF"
            print(f"Move mode is now {state}.")
            continue

        print("You chose: " + guess)

        try:
            guess_num = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number, or x/s/d/m/n.")
            continue

        if guess_num == sec_num:
            print("You are right!")
            break

        elif guess_num > sec_num:
            print("Too high!")
        else:
            print("Too low!")

        if move_mode:
            move = random.choice([-2, -1, 0, 1, 2])
            sec_num += move
            if sec_num < 1:
                sec_num = 1
            elif sec_num > 20:
                sec_num = 20
