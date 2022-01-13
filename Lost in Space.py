import time


def title():
    line1 = r"""  _              _        _            ____                    """

    line2 = r""" | |    ___  ___| |_     (_)_ __      / ___| _ __   __ _  ___ ___ """

    line3 = r""" | |   / _ \/ __| __|    | | '_ \     \___ \| '_ \ / _` |/ __/ _ \ """

    line4 = r""" | |__| (_) \__ \ |_     | | | | |     ___) | |_) | (_| | (_|  __/ """

    line5 = r""" |_____\___/|___/\__|    |_|_| |_|    |____/| .__/ \__,_|\___\___| """

    line6 = r"""                                            |_| """

    creds = "Developed by Gabe Wightman"

    time.sleep(0.4)
    print(line1)
    time.sleep(0.4)
    print(line2)
    time.sleep(0.4)
    print(line3)
    time.sleep(0.4)
    print(line4)
    time.sleep(0.4)
    print(line5)
    time.sleep(0.4)
    print(line6)
    time.sleep(2)
    print(creds)
    time.sleep(2)


def startgame():
    print("asd")



accept = False

if not accept:
    title()
    time.sleep(1)
    terms = input("By hitting enter, you are agreeing not to use elements from this game"
                  "\nwithout permission from the developer. ")
    if terms == "":
        startgame()
        accept = True

    else:
        exit()
