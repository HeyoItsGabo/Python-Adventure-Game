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

    getup = input()

    if int(getup) == 1:
        print("Choosing to ignore the sound, you go back to sleep. You die.")
        partone()  # Restarts the level if you choose the wrong path

    elif int(getup) == 2:
        print("As your feet touch the metal floor, you notice that it is "
              "\nmuch hotter than usual. ")
        parttwo()  # Starts the next part

    else:
        print("1 or 2")


def parttwo():
    print("")


def partthree():
    pass
