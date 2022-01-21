import time


def firstlevel():
    print("You are on Starship Epsilon-7, headed for the planet Europa. "
          "\nYou are peacefully asleep, in your bunk. You are awoken a shrieking"
          "\nmetallic sound, as the starship slows down considerably.")
    time.sleep(0.5)
    print("1- Go back to sleep")
    print("2- Get out of bed")
    try:
        getup = input()

        if int(getup) == 1:
            print("yeet")

        elif int(getup) == 2:
            print("yoink")

        else:
            print("1 or 2")

    except:
        print("1 or 2!!!")
