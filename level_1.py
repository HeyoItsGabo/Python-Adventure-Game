import time
from tqdm import tqdm
from termcolor import cprint

HasHealthPack = False


# def level1():  MAKE SURE TO ADD TO FUNCTION AFTER LEVEL IS DONE! INDENTS TOO!

time.sleep(1)
cprint("Loading level... ", 'green')
time.sleep(1)
for _ in tqdm(range(int(1000))):
    time.sleep(0.00000001)
cprint("Level loaded! ", 'green')
time.sleep(1)

cprint("You are on Starship Epsilon-7, headed for the planet Europa. "
       "\nYou are peacefully asleep, in your bunk. You are awoken a shrieking"
       "\nmetallic sound, as the starship slows down considerably.", 'green')
