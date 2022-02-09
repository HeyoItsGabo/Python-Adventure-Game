import time
from functions import title
from level_1 import level1
from level_2 import level2
from level_3 import level3
from termcolor import cprint



def terms():
    title()  # Starts the title sequence
    time.sleep(1)
    accept = input("By hitting enter, you are agreeing not to use elements from this game"
                   "\nwithout permission from the developer. ")
    if accept == "":
        time.sleep(1)
        cprint("NOTE: You will need an internet connection for some puzzles!", 'red', attrs=['underline'])
        time.sleep(1)
        level1()  # Starts level 1
        level2()  # Starts level 2 once level 1 is completed
        level3()  # Starts level 3 once both level 1 and 2 are completed

    else:
        exit()


terms()
