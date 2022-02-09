import time
from termcolor import colored


def level1():
    print("You are on Starship Epsilon-7, headed for the planet Europa. "
          "\nYou are peacefully asleep, in your bunk. You are awoken a shrieking"
          "\nmetallic sound, as the starship slows down considerably.")
    partone()


def partone():
    time.sleep(0.5)
    print("What do you do?")
    print("1- Go back to sleep")
    print("2- Get out of bed")
    try:
        getup = input()

        if int(getup) == 1:  # Incorrect path
            print("Choosing to ignore the sound, you go back to sleep. The spaceship plummets to "
                  "\nthe planet below, taking you with it.")

            while True:  # Will not accept any input except for enter
                restart = input(colored("You have died. Input the enter key to restart. ", 'red'))

                if restart == "":
                    level1()  # Restarts the level if you choose the wrong path
                    return False  # Satisfies the while True statement
                else:
                    time.sleep(0.3)

        elif int(getup) == 2:  # Correct path
            print("As your feet touch the metal floor, you notice that it is "
                  "\nmuch hotter than usual. ")
            parttwo()  # Starts the next part

    except ValueError:  # Had to include this or else Python gets picky
        print("Please enter 1 or 2.")
        partone()


def parttwo():
    print("")


def partthree():
    pass
