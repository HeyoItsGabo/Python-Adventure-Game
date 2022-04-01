import time
from tqdm import tqdm
from termcolor import cprint, colored

HasBackPack = False
HasHealthPack = False


def die():
    while True:  # Will not accept any input except for enter
        restart = input(colored("You have died. Input the enter key to restart. ", 'green'))

        if restart == "":
            return False  # Satisfies the while True statement
        else:
            time.sleep(0.3)


# def level1():  MAKE SURE TO ADD TO FUNCTION AFTER LEVEL IS DONE! INDENTS TOO!

time.sleep(1)
cprint("Loading level... ", 'green')
time.sleep(1)
for _ in tqdm(range(int(1000))):
    time.sleep(0.00000001)
cprint("Level loaded! ", 'green')
time.sleep(1)

cprint("You are on Starship Epsilon-7, headed for the planet Europa. "
       "\nYou are peacefully asleep, in your bunk. You are awoken a shrieking"
       "\nmetallic sound, as the starship slows down considerably.", 'green')
time.sleep(1)
cprint("What do you do?", 'green')
time.sleep(1)
cprint("1- Go back to sleep", 'green')
cprint("2- Get out of bed", 'green')

while True:
    wakeup = input()
    try:
        if int(wakeup) == 1:
            cprint("Choosing to ignore the sound, you go back to sleep. The spaceship plummets to "
                   "\nthe planet below, taking you with it.", 'green')
            die()

        elif int(wakeup) == 2:
            print("yoink")
            break
        else:
            print("Please enter either 1 or 2.")
    except ValueError:
        print("Please enter either 1 or 2.")
