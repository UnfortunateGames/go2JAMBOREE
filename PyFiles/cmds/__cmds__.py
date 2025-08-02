import os
import random
import time

# ! Don't touch these!
# ! These are essentials...

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def rRN(x, y) -> int:
    return random.randint(x, y)

def wait(n) -> None:
    time.sleep(n)

# ! Move to GUI

def Cprint(message=str, spaces=None) -> None:
    if spaces is None:
        spaces = " " * int((40 - len(list(message))) / 2)
    print(spaces + message)