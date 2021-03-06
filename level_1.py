import time as t
import random
from tqdm import tqdm
from functions import Door, Window, Backpack, Mirror, Bookshelf, Spacesuit, Bed, Suitcase, Sink, Toolbox

HasBackPack = False
HasHealthPack = False
NoShoes = False
FlipFlops = False
WorkBoots = False
codesegment1 = random.randint(0, 9)
codesegment2 = random.randint(0, 9)
codesegment3 = random.randint(0, 9)
code = int(str(codesegment1) + str(codesegment2) + str(codesegment3))
items = ["door", "Window", "Backpack", "Mirror", "Bookshelf", "Spacesuit", "Bed", "Suitcase", "Sink", "Toolbox"]
code1location = random.randint(1, 3)
code2location = random.randint(4, 6)
code3location = random.randint(7, 9)


def die():
    while True:  # Will not accept any input except for enter
        restart = input("You have died. Hit the enter key to restart. ")
        if restart == "":
            print("-------------------------------------")
            t.sleep(1)
            level_1()
        else:
            t.sleep(1)


def menu(itemlist, question):
    for item in itemlist:
        print(itemlist.index(item), item)
        
    while True:
        doorcode = input(question)
        try:
            doorcode = int(doorcode)
            break
        except ValueError:
            print("Selection must be whole number between 0-9:")
    return doorcode
        

def level_1():
    t.sleep(1)
    print("Loading level... ")
    t.sleep(1)
    for _ in tqdm(range(int(1000))):
        t.sleep(0.00000001)
    print("Level loaded! ")
    t.sleep(1)

    print("You are on Starship Epsilon-7, headed for the planet Europa. "
          "\nYou are peacefully asleep, in your bunk. You are awoken a shrieking"
          "\nmetallic sound, as the starship slows down considerably.")
    t.sleep(1)

    while True:  # First encounter
        print("What do you do?")
        t.sleep(1)
        print("1- Go back to sleep"
              "\n2- Get out of bed")
        wakeup = input()
        try:
            if int(wakeup) == 1:
                print("Choosing to ignore the sound, you go back to sleep. The spaceship plummets to "
                      "\nthe planet below, taking you with it.")
                t.sleep(1)
                die()

            elif int(wakeup) == 2:  # Correct path
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter either 1 or 2.")

    print("As you awake from your slumber, you notice the floor is warmer than "
          "\nusual. You notice two pairs of shoes by the airlock. A pair of"
          "\nflip-flops, and a pair of work boots.")
    t.sleep(1)

    while True:  # Second encounter
        print("Which do you choose?")
        t.sleep(1)
        print("1- Neither pair of shoes"
              "\n2- The pair of flip flops"
              "\n3- The pair of work boots")
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

    print('You walk over to the bulkhead, and notice the keypad next to it. You must inspect'
          '\nitems around the room in order to retrieve the three-digit code.')
    while True:  # Menu for third encounter, the coded door
        choice = menu(items, "What do you want to inspect?\n")
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
        elif choice == 6:
            Bed(choice, code2location, codesegment2)
        elif choice == 7:
            Suitcase(choice, code3location, codesegment3)
        elif choice == 8:
            Sink(choice, code3location, codesegment3)
        elif choice == 9:
            Toolbox(choice, code3location, codesegment3)
        elif choice == 10:
            print(code)
        else:
            pass
        if Door(code):
            print("The bulkhead slowly opens, revealing a long, empty corridor."
                  "\n The left corridor has two doors, and the right has one.")
            t.sleep(1)
            break

    while True:  # Fourth encounter
        print("Which direction do you go?")
        print("1- Left corridor"
              "\n2- Right corridor")
        corridor = input()
        try:
            if int(corridor) == 1:  # Correct path
                print("As you pass through the corridor, you come across two other doors."
                      "\nOne of them has ice on the door and around the frame. The other"
                      "\nis warm to the touch, and you can hear a deep rumble inside.")
                break
            elif int(corridor) == 2:
                print("As you pass through the corridor, you get an eerie feeling that you are not alone.")
                t.sleep(0.5)
                print("Suddenly, another bulkhead shuts rapidly behind you. You hear a loud hissing sound"
                      "\nas the airlock cycles. The outer bulkhead opens, releasing you into the"
                      "\ninfinite void of space.")
                die()

            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter either 1 or 2.")

    while True:  # Fifth encounter
        print("Which door do you choose to enter?")
        t.sleep(1)
        print("1- The cold door"
              "\n2-The hot door")
        tempdoor = input()
        try:
            if int(tempdoor) == 1:
                print("As you enter the cold room, you notice cryogenic tubes containing what"
                      "\nappear to be bodies. You knew these people at one point. Something"
                      "\nseems off about this room.")
                t.sleep(1)
                print("The room gets colder and colder, as you slowly succumb to sleep.")
                die()
            elif int(tempdoor) == 2:
                print("You push open the door to see the spacecraft's engine sparking rapidly. Perhaps you can fix it.")
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter either 1 or 2.")
