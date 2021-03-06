import time
from termcolor import cprint


# "Animation" for title screen, with credits
def title():
    line1 = r"""  _              _        _            ____                    """
    line2 = r""" | |    ___  ___| |_     (_)_ __      / ___| _ __   __ _  ___ ___ """
    line3 = r""" | |   / _ \/ __| __|    | | '_ \     \___ \| '_ \ / _` |/ __/ _ \ """
    line4 = r""" | |__| (_) \__ \ |_     | | | | |     ___) | |_) | (_| | (_|  __/ """
    line5 = r""" |_____\___/|___/\__|    |_|_| |_|    |____/| .__/ \__,_|\___\___| """
    line6 = r"""                                            |_| """
    creds = "Developed by Gabe Wightman"
    time.sleep(0.4)
    cprint(line1, 'green')
    time.sleep(0.4)
    cprint(line2, 'green')
    time.sleep(0.4)
    cprint(line3, 'green')
    time.sleep(0.4)
    cprint(line4, 'green')
    time.sleep(0.4)
    cprint(line5, 'green')
    time.sleep(0.4)
    cprint(line6, 'green')
    time.sleep(1)
    cprint(creds, 'green')


# Menu for items to find door code
def menu(menulist, question):
    for item in menulist:
        print(menulist.index(item), item)
    while True:
        result = input(question)
        try:
            result = int(result)
            break
        except ValueError:
            cprint("Selection must be a whole number 0-9.", 'green')
    return result


# Input for code to door
def Door(code):
    print("You walk to the bulkhead, and see a keypad. Based on what you see,"
          "\nthe code must be 3 digits long. ")
    while True:
        try:
            option1 = int(input("Digit one: "))
            break
        except ValueError:
            print("Digit one must be a whole number 0-9.")
    while True:
        try:
            option2 = int(input("Digit two: "))
            break
        except ValueError:
            print("Digit two must be a whole number 0-9.")
    while True:
        try:
            option3 = int(input("Digit three: ", ))
            break
        except ValueError:
            cprint("Digit three must be a whole number 0-9.")

    chosencode = int(str(option1) + str(option2) + str(option3))
    print("")
    if chosencode == code:
        print("The keypad flashes green, as the bulkhead opens.")
        return True
    else:
        print("The keypad beeps once, and flashes red. The "
              "\ninputted code is wrong. ")
        return False


# Code #1 check location: Window
def Window(choice, codelocation, codevalue):
    print("")
    print("You look at the window. Only four inches of reinforced glass"
          "\nbetween you and the void.")
    if choice == codelocation:
        print("Carved into the frame, you see the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #1 check location: Backpack
def Backpack(choice, codelocation, codevalue):
    print("")
    cprint("Rifling through the backpack, you find a scratched up notebook.")
    if choice == codelocation:
        print("Scribbled into one of the pages, you see the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #1 check location: Mirror
def Mirror(choice, codelocation, codevalue):
    print("")
    print("Glancing in the mirror, You see fingerprints. Fingerprints belonging"
          "\nto someone else.")
    if choice == codelocation:
        print("As you study your reflection, you notice the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #2 check location: Bookshelf
def Bookshelf(choice, codelocation, codevalue):
    print("")
    print("A steel bookshelf bolted to the wall. Many of the books have not been opened"
          "\n in years.")
    if choice == codelocation:
        print("You notice all the books are of the same volume, that"
              "\n volume number being " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #2 check location: Spacesuit
def Spacesuit(choice, codelocation, codevalue):
    print("")
    print("The spacesuit lays still in the locker. It looks like it has been used recently.")
    if choice == codelocation:
        print("Scratched into the helmet, you can faintly see the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #2 check location: Bed
def Bed(choice, codelocation, codevalue):
    print("")
    print("You pick up the shaggy, tattered pillow and see a piece of paper.")
    if choice == codelocation:
        print("Written on the paper, you see the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #3 check location: Suitcase
def Suitcase(choice, codelocation, codevalue):
    print("")
    print("The suitcase seems rather familiar. Strange.")
    if choice == codelocation:
        print("On the bottom, you feel the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #3 check location: Sink
def Sink(choice, codelocation, codevalue):
    print("")
    print("The leaky faucet drips persistently and annoyingly, as if on purpose.")
    if choice == codelocation:
        print("The faucet drips in sequences of " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


# Code #3 check location: Toolbox
def Toolbox(choice, codelocation, codevalue):
    print("")
    print("The red toolbox has a few basic tools, but nothing that would help you.")
    if choice == codelocation:
        print("You find " + str(codevalue) + "wrenches in the case.")
        print("")
    else:
        print("You find no code.")
        print("")
