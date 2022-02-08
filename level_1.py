import time


def level1():
    partone()


def partone():
    print("You are on Starship Epsilon-7, headed for the planet Europa. "
          "\nYou are peacefully asleep, in your bunk. You are awoken a shrieking"
          "\nmetallic sound, as the starship slows down considerably.")
    time.sleep(0.5)
    print("1- Go back to sleep")
    print("2- Get out of bed")
    try:
        getup = input()

        if int(getup) == 1:
            print("Choosing to ignore the sound, you go back to sleep. The spaceship plummets to "
                  "\nthe planet below, taking you with it.")

            while True:
                restart = input("You have died. Input the enter key to restart. ")

                if restart == "":
                    partone()  # Restarts the level if you choose the wrong path
                    return False
                else:
                    print("Please hit the enter key to continue. ")

        elif int(getup) == 2:
            print("As your feet touch the metal floor, you notice that it is "
                  "\nmuch hotter than usual. ")
            parttwo()  # Starts the next part

    except ValueError:
        print("Please enter 1 or 2.")
        partone()


def parttwo():
    print("")


def partthree():
    pass
