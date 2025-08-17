from cmds.__cmds__ import cls, wait, rRN
import backend.__backend__ as BE
import gui.__gui__ as G

localAStats: dict = {
    "HP": int,
    "Defense": int,
    "MoveSet": {}
}

localCDs: dict = {
    0: 0,
    1: 0,
    2: 0
}

inBattleTime: int = 0

def initBattleStats() -> None:
    localAStats["HP"] = BE.curAnimal["HP"]
    localAStats["Defense"] = BE.curAnimal["defense"]
    localAStats["MoveSet"][0] = BE.curAnimal["moveSet"][BE.curAnimal["moveSet"]["list"][0]]
    localAStats["MoveSet"][1] = BE.curAnimal["moveSet"][BE.curAnimal["moveSet"]["list"][1]]

def dealDMG(move=int) -> None or bool:
    DMG = BE.curmoveSet[BE.curmoveSet["list"][move]]
    rng = rRN(0, DMG)
    dealt = (DMG + rng) - (localAStats["Defense"] * 0.15)
    localAStats["HP"] -= dealt
    if rng >= DMG / 2:
        return True

def animalChoice() -> None:
    L = [False, True]
    x = rRN(0, 1)
    if L[x] is True:
        choice = BE.curAnimal["moveSet"]["list"][1]
        BE.curAnimal["HP"] += BE.curAnimal["moveSet"][choice]
    else:
        choice = BE.curAnimal["moveSet"]["list"][0]
        BE.curStats[0] -= BE.curAnimal["moveSet"][choice]
    return choice

def initBattle() -> None:
    def display() -> None:
        cls()
        G.displayStat()
        G.fAnimalSprite()
    def useMove(n=int) -> None:
        move = BE.curmoveSet[BE.curmoveSet["list"][n]]
        dealDMG(n)
        localCDs[n] = move[1]
    initBattleStats()
    while True:
        display()
        G.fBattleMenu()
        x = input(f"\n{" " * 6}< !! ) >> ").lower()
        if x == BE.curmoveSet["list"][0]:
            display()
            G.printAnim(f"{" " * 5}You used {BE.curmoveSet["list"][0]}!")
            useMove(0)
            wait(1)
        elif x == BE.curmoveSet["list"][1]:
            display()
            G.printAnim(f"{" " * 5}You used {BE.curmoveSet["list"][1]}!")
            useMove(1)
            wait(1)
        elif x == BE.curmoveSet["list"][2]:
            display()
            G.printAnim(f"{" " * 5}You used {BE.curmoveSet["list"][2]}!")
            useMove(2)
            wait(1)
        else:
            display()
            G.input(f"{" " * 5}{x} is not a valid option!")
        for x in range(0, 2):
            localCDs[x] -= 0
        animalChoice()
        y = animalChoice()
        display()
        G.printAnim(f"{" " * 5}The enemy used {y}!")
        if localAStats["HP"] <= 0:
            return 0
        elif BE.checkDeath > 0:
            return 1
