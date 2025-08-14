import os
import random
import time

# ! Don't touch these!
# ! These are essential...

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def rRN(x, y) -> int:
    return random.randint(x, y)

def wait(n) -> None:
    time.sleep(n)