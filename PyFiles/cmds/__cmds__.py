import os
import random
import time

# Just the essentials!
# And do not mess with this, its basically the CORE
# of the whole game.

# Forget all the random spaghetti code, THIS is the
# final boss of debugging.

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def rRN(x, y) -> int:
    return random.randint(x, y)

def wait(n) -> None:
    time.sleep(n)
