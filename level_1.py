import time
from tqdm import tqdm
from termcolor import cprint, colored


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
    partone()


def partone():  # Part 1 of level 1
    time.sleep(1)
    cprint("What do you do?", 'green')
    cprint("1- Go back to sleep", 'green')
    cprint("2- Get out of bed", 'green')
    try:
        getup = input()

        if int(getup) == 1:  # Incorrect path
            cprint("Choosing to ignore the sound, you go back to sleep. The spaceship plummets to "
                   "\nthe planet below, taking you with it.", 'green')

            while True:  # Will not accept any input except for enter
                restart = input(colored("You have died. Input the enter key to restart. ", 'red'))

                if restart == "":
                    level1()  # Restarts the level if you choose the wrong path
                    return False  # Satisfies the while True statement
                else:
                    time.sleep(0.3)

        elif int(getup) == 2:  # Correct path

            cprint("As your feet touch the metal floor, you notice that it is "
                   "\nmuch hotter than usual. By the door, you notice two pairs "
                   "\nof shoes. A pair of flip flops, and a pair of work boots. ", 'green')
            parttwo()  # Starts the next part

    except ValueError:  # Had to include this or else Python gets picky. Definitely need to troubleshoot
        cprint("Please enter 1 or 2.", 'green')
        partone()


def parttwo():  # Part 2 of level 1
    print("")


def partthree():  # Part 3 of level 1
    pass
