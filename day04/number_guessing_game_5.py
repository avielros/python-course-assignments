import random

sec_num = random.randrange(1, 21)
guess = None
debug_mode = False
move_mode = False

while guess != sec_num:
    if debug_mode:
        print(f"[DEBUG] Secret number is: {sec_num}")

    guess = input("Enter your guess: a number between 1 to 20 (x=quit, s=show, d=debug, m=move mode): ")

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

    if guess == 'm':
        move_mode = not move_mode
        state = "ON" if move_mode else "OFF"
        print(f"Move mode is now {state}.")
        continue

    print("You chose: " + guess)


try:
        guess_num = int(guess)
    except ValueError:
        print("Invalid input. Please enter a valid number, or x/s/d/m.")
        continue

    if guess_num == sec_num:
        print("You are right!")
        break
    elif guess_num > sec_num:
        print("Too high!")
    else:
        print("Too low!")

 if move_mode:
        import random
        move = random.choice([-2, -1, 0, 1, 2])
        sec_num += move

  if sec_num < 1:
            sec_num = 1
        elif sec_num > 20:
            sec_num = 20
