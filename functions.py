import time
from termcolor import colored, cprint


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


def menu(list, question):
    for item in list:
        print(list.index(item), item)
    while True:
        result = input(question)
        try:
            result = int(result)
            break
        except ValueError:
            cprint("Selection must be a whole number 0-9.", 'green')
    return result


def door(code):
    cprint("You walk to the bulkhead, and see a keypad. Based on what you see,"
           "\nthe code must be 4 digits long. ")
    while True:
        try:
            option1 = int(input(colored("Digit one: ", 'green')))
            break
        except ValueError:
            cprint("Digit one must be a whole number 0-9.", 'green')
    while True:
        try:
            option2 = int(input(colored("Digit two: ", 'green')))
            break
        except ValueError:
            cprint("Digit two must be a whole number 0-9.", 'green')
    while True:
        try:
            option3 = int(input(colored("Digit three: ", 'green')))
            break
        except ValueError:
            cprint("Digit three must be a whole number 0-9.", 'green')

            
    chosencode = int(str(option1) + str(option2) + str(option3))
    print("")
    if chosencode == code:
        cprint("The keypad flashes green, as the bulkhead opens.", 'green')
        return 1
    else:
        cprint("The keypad beeps once, and flashes red. The "
               "\ninputted code is wrong", 'green')
        return 0


def Window(choice, codelocation, codevalue):
    print("")
    cprint("You look at the window. Only four inches of reinforced glass"
           "\nbetween you and the void.", 'green')
    if choice == codelocation:
        cprint("Carved into the frame, you see the number", 'green' + str(codevalue) + ".", 'green')
        print("")
    else:
        cprint("You find no code.", 'green')
        print("")
    
    
def Backpack(choice, codelocation, codevalue):
    print("")
    cprint("Rifling through the backpack, you find a scratched up notebook.", 'green')
    if choice == codelocation:
        cprint("Scribbled into one of the pages, you see the number", 'green' + str(codevalue) + ".", 'green')
        print("")
    else:
        cprint("You find no code.", 'green')
        print("")
        
        
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


def Spacesuit(choice, codelocation, codevalue):
    print("")
    print("The spacesuit lays still in the locker. It looks like it has been used recently.")
    if choice == codelocation:
        print("Scratched into the helmet, you can faintly see the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")


def Bed(choice, codelocation, codevalue):
    print("")
    print("You pick up the shaggy, tattered pillow and see a piece of paper.")
    if choice == codelocation:
        print("Written on the paper, you see the number " + str(codevalue) + ".")
        print("")
    else:
        print("You find no code.")
        print("")
