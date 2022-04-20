import time
import random
from tqdm import tqdm
from functions import door, Window, Backpack, Mirror, Bookshelf, Spacesuit

HasBackPack = False
HasHealthPack = False
NoShoes = False
FlipFlops = False
WorkBoots = False
codesegment1 = random.randint(0, 9)
codesegment2 = random.randint(0, 9)
codesegment3 = random.randint(0, 9)
code = int(str(codesegment1) + str(codesegment2) + str(codesegment3))
items = ["door", "Window", "Backpack", "Mirror", "Bookshelf", "Spacesuit"]
code1location = random.randint(1, 3)
code2location = random.randint(4, 6)
code3location = random.randint(7, 9)


def menu(itemlist, question):
    for item in itemlist:
        print(itemlist.index(item), item)
        
    while True:
        result = input(question)
        try:
            result = int(result)
            break
        except ValueError:
            print("Selection must be whole number between 0-9:")
    return result
        
    


def level1():
    time.sleep(1)
    print("Loading level... ")
    time.sleep(1)
    for _ in tqdm(range(int(1000))):
        time.sleep(0.00000001)
    print("Level loaded! ")
    time.sleep(1)

    print("You are on Starship Epsilon-7, headed for the planet Europa. "
          "\nYou are peacefully asleep, in your bunk. You are awoken a shrieking"
          "\nmetallic sound, as the starship slows down considerably.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("1- Go back to sleep"
          "\n2- Get out of bed")

    while True:  # First encounter in the first level
        wakeup = input()
        try:
            if int(wakeup) == 1:
                print("Choosing to ignore the sound, you go back to sleep. The spaceship plummets to "
                      "\nthe planet below, taking you with it.")
                time.sleep(1)
                while True:  # Will not accept any input except for enter
                    restart = input("You have died. Input the enter key to restart. ")

                    if restart == "":
                        print("-------------------------------------")
                        time.sleep(1)
                        level1()
                    else:
                        time.sleep(1)

            elif int(wakeup) == 2:
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter either 1 or 2.")

    print("As you awake from your slumber, you notice the floor is warmer than "
          "\nusual. You notice two pairs of shoes by the airlock. A pair of"
          "\nflip-flops, and a pair of work boots.")
    time.sleep(1)
    print("Which do you choose?")
    time.sleep(1)
    print("1- Neither pair of shoes"
          "\n2- The pair of flip flops"
          "\n3- The pair of work boots")

    while True:  # Second encounter in the first level
        footwear = input()
        try:
            if int(footwear) == 1:
                print("Choosing not to take any pair of shoes, you head towards the door.")
                global NoShoes
                NoShoes = True
                break
            elif int(footwear) == 2:
                print("You slip the flip flops on, but still feel the warmth from the floor.")
                global FlipFlops
                FlipFlops = True
                break
            elif int(footwear) == 3:
                print("You put on the boots, and tie the laces.")
                global WorkBoots
                WorkBoots = True
                break
            else:
                print("Please enter a value 1-3.")
        except ValueError:
            print("Please enter either 1, 2, or 3.")

    while True:
        choice = menu(items, "What do you want to inspect?")
        if choice == 1:
            Window(choice, code1location, codesegment1)
        elif choice == 2:
            Backpack(choice, code1location, codesegment1)
        elif choice == 3:
            Mirror(choice, code1location, codesegment1)
        elif choice == 4:
            Bookshelf(choice, code2location, codesegment2)
        elif choice == 5:
            Spacesuit(choice, code2location, codesegment2)
        else:
            result = door(code)
        if result == 1:
            break


level1()
