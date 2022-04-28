import time
from functions import title
from level_1 import level_1
from level_2 import level_2
from level_3 import level_3
from termcolor import cprint, colored


def terms():
    title()  # Starts the title sequence
    time.sleep(1)

    accept = input("By hitting enter, you are agreeing not to use elements from this game"
                   "\nwithout permission from the developer. ")
    if accept == "":
        time.sleep(1)
        print("")  # Formatting
        cprint("NOTE: You will need an internet connection for some puzzles!", attrs=['underline'])
        print("")  # Formatting
        time.sleep(2)

        cprint("To play this game, you must choose from a list of options presented "
               "\nto you. Insert the number of the choice you want to make. Keep in "
               "\nmind that your decisions will affect the later portions of the game!", attrs=['underline'])
        print("")
        while True:  # Conditional for accepting the rules of the game
            accept_rules = input("Hit the enter key if you understand the rules of this game. ")
            if accept_rules == "":
                level_1()  # Starts level 1
                level_2()  # Starts level 2 once level 1 is completed
                level_3()  # Starts level 3 once both level 1 and 2 are completed
                return False
            else:
                time.sleep(0.3)
    else:
        exit()


terms()
