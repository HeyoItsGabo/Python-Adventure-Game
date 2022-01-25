import time
from functions import title
from level_1 import partone


accept = False

if not accept:
    title()
    time.sleep(1)
    terms = input("By hitting enter, you are agreeing not to use elements from this game"
                  "\nwithout permission from the developer. ")
    if terms == "":
        accept = True
        partone()


    else:
        exit()
