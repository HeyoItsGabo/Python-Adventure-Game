import time
from functions import title
from level_1 import level1
from level_2 import level2


def terms():
    title()  # Starts the title sequence
    time.sleep(1)
    accept = input("By hitting enter, you are agreeing not to use elements from this game"
                   "\nwithout permission from the developer. ")
    if accept == "":
        level1()  # Starts level 1
        level2()  # Starts level 2

    else:
        exit()


terms()
