import time
from tqdm import tqdm
from termcolor import cprint, colored

HasBackPack = False
HasHealthPack = False


def level1():
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

    while True:  # First encounter in the first level
        wakeup = input()
        try:
            if int(wakeup) == 1:
                cprint("Choosing to ignore the sound, you go back to sleep. The spaceship plummets to "
                       "\nthe planet below, taking you with it.", 'green')
                time.sleep(1)
                while True:  # Will not accept any input except for enter
                    restart = input(colored("You have died. Input the enter key to restart. ", 'green'))

                    if restart == "":
                        cprint("-------------------------------------", 'green')
                        time.sleep(1)
                        level1()
                    else:
                        time.sleep(1)

            elif int(wakeup) == 2:
                print("yoink")
                break
            else:
                cprint("Please enter either 1 or 2.", 'green')
        except ValueError:
            cprint("Please enter either 1 or 2.", 'green')

    cprint("As you awake from your slumber, you notice the floor is warmer than "
           "\nusual. You notice two pairs of shoes by the airlock. A pair of"
           "\nflip-flops, and a pair of work boots.", 'green')
    time.sleep(1)
    cprint("Which do you choose?", 'green')
    time.sleep(1)

    while True:  # Second encounter in the first level
        footwear = input()
        try:
            if int(footwear) == 1:
                pass
            elif int(footwear) == 2:
                pass
            elif int(footwear) == 3:
                pass
            else:
                pass
        except ValueError:
            cprint("Please enter either 1, 2, or 3.", 'green')


level1()
