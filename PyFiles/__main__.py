from cmds.__cmds__ import cls, wait, rRN
from battle.__battle__ import initBattle
import backend.__backend__ as BE
import gui.__gui__ as G

# Might uhhh...
# Run out of passion because of this...

keybinds: dict = {
    "leftKB": "left",
    "upKB": "up",
    "rightKB": "right",
    "downKB": "down",
    "taskKB": "task",
    "actsKB": "acts",
    "bagKB": "bag",
    "checkKB": "check",
    "askKB": "ask",
    "waitKB": "wait",
    "sleepKB": "sleep",
    "getKB": "get",
    "menuKB": "menu",
    "backKB": "back"
}

hasStartedGame: bool = False

# - ACTS MENU -

def gamedisplay() -> None:
    G.fLocDisplay()
    G.displayStat()
    G.actScroll()

def initDisplay() -> None:
    while True:
        if BE.checkDeath() > 0:
            initDeath()
        cls()
        gamedisplay()
        x = input("     < ! ) >> ").lower()
        if x == "move":
            G.curMenu = 1
            initMove()
        elif x == keybinds["actsKB"]:
            G.curMenu = 2
            initAct()
        elif x == keybinds["taskKB"]:
            if G.checkAct("do") is True:
                cls()
                wait(1)
                G.taskAnim()
                BE.curBadges += BE.taskList[BE.curTask]["prize"]
                BE.mvGTime(4)
                BE.hPlayer("hp", BE.taskList[BE.curTask]["Drain"][0])
                BE.hPlayer("stamina", BE.taskList[BE.curTask]["Drain"][1])
                BE.hPlayer("hunger", BE.taskList[BE.curTask]["Drain"][2])
                BE.doneTask = True
                wait(2)
                cls()
                initDisplay()
            else:
                input(f"\n{" " * 9}I can't do that here.")
        elif x == keybinds["waitKB"]:
            initWait()
        elif x == keybinds["bagKB"]:
            G.curMenu = 3
            initBag()
        elif x == keybinds["menuKB"]:
            break
        else:
            input(f"\n{" " * 6}{x}? I can't do that...")

def initMove() -> None:
    def arrivalAnim() -> None:
        cls()
        G.fLocDisplay()
        print("\n")
        G.printAnim(BE.locList[BE.locList["list"][BE.curLoc[1]][BE.curLoc[0]]])
        wait(1)
    while True:
        BE.mvGTime()
        BE.updTVal()
        if BE.updTVal() == 1:
            BE.hPlayer("hp", BE.curDrainStats[0])
            BE.hPlayer("stamina", BE.curDrainStats[1])
        if BE.checkDeath() > 0:
            initDeath()
        cls()
        gamedisplay()
        x = input(f"{" " * 6}< ! ? ) >> ").lower()
        if x == keybinds["leftKB"] and G.checkAct("l") is True:
            BE.curLoc[0] -= 1
            G.moveAnim()
            arrivalAnim()
        elif x == keybinds["upKB"] and G.checkAct("u") is True:
            BE.curLoc[1] -= 1
            G.moveAnim()
            arrivalAnim()
        elif x == keybinds["rightKB"] and G.checkAct("r") is True:
            BE.curLoc[0] += 1
            G.moveAnim()
            arrivalAnim()
        elif x == keybinds["downKB"] and G.checkAct("d") is True:
            BE.curLoc[1] += 1
            G.moveAnim()
            arrivalAnim()
        elif x == keybinds["backKB"]:
            break
        else:
            input(f"\n{" " * 6}I'm not allowed to go there!")
    G.curMenu = 0

def initBag() -> None:
    while True:
        cls()
        gamedisplay()
        x = input(f"{" " * 6}< ! ? ) >> ").lower()
        if x == "meat":
            if BE.inventory["meat"] > 0:
                BE.inventory["meat"] -= 1
                for x in range(0, 2):
                    BE.curStats += BE.itemList["meat"]["heal"][x]
            else:
                input("     There is no Meat...")
        elif x == "apple":
            if BE.inventory["apple"] > 0:
                BE.inventory["apple"] -= 1
                for x in range(0, 2):
                    BE.curStats += BE.itemList["apple"]["heal"][x]
            else:
                input("     There is no Apples...")
        elif x == "water":
            if BE.inventory["water"] > 0:
                BE.inventory["water"] -= 1
                for x in range(0, 2):
                    BE.curStats += BE.itemList["water"]["heal"][x]
            else:
                input("     There is no Water...")
        elif x  == keybinds["backKB"]:
            break
        else:
            input(f"     {x} is not an item!")
    G.curMenu = 0

def initAct() -> None:
    while True:
        cls()
        gamedisplay()
        x = input(f"\n{" "* 6}< ! ? ) >> ")
        if x == keybinds["sleepKB"] and BE.curLoc == [1, 0] and BE.canSleep is True:
            cls()
            BE.mvGTime(None)
            G.fRandomDialogue("sleep")
            wait(2)
            if BE.doneTask is False:
                initPunish()
            break
        elif x == keybinds["askKB"] and BE.curLoc == [0, 1]:
            for x in G.fTaskDialogue():
                cls()
                G.fLocDisplay()
                G.printAnim(x, "\n\n")
                wait(1)
            BE.heardTask = True
            wait(1)
        elif x == keybinds["checkKB"]:
            cls()
            print(G.fcheckSprite())
            print(G.fcheckActs())
            input("\n     Press Enter to continue...")
        elif x == keybinds["getKB"]:
            items = [None, "apple", "water", "meat"]
            if G.canCollect() == 0:
                input(f"{" " * 5}There is nothing here!")
            elif G.canCollect() > 2 and BE.IsThereAnimal is True:
                cls()
                G.fLocDisplay()
                G.displayStat()
                x = input(f"\n{" " * 6}Hunt the animal? (Y/n) >> ").lower()
                if x != "n":
                    y = initBattle()
                    if y == 0:
                        pass
                    elif y == 1:
                        initDeath()
            elif BE.IsThereAnimal is False:
                input(f"\n{" " * 6}It's not here yet...")
            else:
                BE.curBag[items[G.canCollect()]] += 1
        elif x == keybinds["backKB"]:
            break
        else:
            input("\n     I'm not allowed to do that here!")
    G.curMenu = 0

def initWait() -> None:
    if BE.canWait is False:
        input("     I'm tired of waiting...")
        return
    elif BE.WTime == "Night":
        input("     I would rather sleep than wait...")
        return
    while True:
        cls()
        G.fLocDisplay()
        G.displayStat()
        x = input(f"\n{" " * 6}Wait for night? [Y/n] > ").lower()
        if x == "n":
            break
        BE.GTime = 13
        BE.updTVal()
        cls()
        wait(2)
        G.fRandomDialogue("wait", "\n\n\n")
        wait(1)
        break

# - SEQUENCES -

def initDeath() -> None:
    cls()
    wait(2)
    G.printAnim("Your vision starts to fade...", "\n\n\n")
    wait(1)
    cls()
    if BE.checkDeath() == 1:
        BE.deaths += 1
        BE.curLoc == [2, 0]
        G.printAnim("Nggghh... My wounds...", "\n\n\n")
        wait(1)
        cls()
    elif BE.checkDeath() == 2:
        BE.curLoc == [1, 0]
        G.printAnim("I should have slept by now...", "\n\n\n")
        wait(1)
        cls()
    wait(2)
    if BE.deaths >= 3:
        dialogue = [
            "Oh...",
            "I am sorry...",
            "You did not pass my test...",
            "You were perfect...",
            "MY CREATION.",
            "Though you have failed me..."
        ]
        for x in dialogue:
            G.printAnim(x, "\n")
            wait(1)
        wait(1)
        while True:
            cls()
            print("\n\n")
            G.menuScroll(G.gameOver)
            x = input(f"\n\n\n{" " * 6}< ? ) >> ").lower()
            if x == keybinds["menuKB"] or x == keybinds["backKB"]:
                func = initMenu()
                break
            elif x == "retry?" or x == "retry":
                BE.updCharVal()
                BE.initVar()
                func = initIntro()
                break
            else:
                input(f"     {x} is not an option...")
        func()
        return
    BE.hPlayer()
    dialogue = [
        "Oh...",
        "Do not worry...",
        "For I am here...",
        "I will always forgive you..."
    ]
    for x in dialogue:
        G.printAnim(x, "\n")
        wait(1)
    wait(1)
    cls()
    wait(2)
    initDisplay()

def initPunish() -> None:
    dialogue = [
        "My creation.",
        "Why must you ignore me?",
        "You shalt not disobey.",
        "You must be punished."
    ]
    for x in dialogue:
        cls()
        G.printAnim(x, "\n\n\n")
        wait(1)
    BE.hPlayer("hp", -10)
    BE.hPlayer("stamina", -10)
    dur = 1.5
    for x in range(0, 2):
        letters = ["#", ":", "."]
        for y in letters:
            cls()
            print(f"{f"{y * 40}\n" * 6}")
            wait(dur)
        dur -= 0.5
    cls()
    wait(2)

def initIntro() -> None:
    dialogue1 = [
        "Hello?",
        "Are you here?",
        "Good.",
        "Open your eyes..."
    ]
    dialogue2 = [
        "You are my creation.",
        "You are not ready.",
        "Now, you should go to my altar",
        "Go explore for yourself."
    ]
    for x in dialogue1:
        cls()
        G.printAnim(x, "\n\n\n")
        wait(2)
    cls()
    G.printAnim(G.fLocDisplay(True), "")
    for x in dialogue2:
        cls()
        G.fLocDisplay()
        G.printAnim(x, "\n")
        wait(1)
    cls()
    initDisplay()

# - MAIN MENU -

def initMenu() -> None:
    global hasStartedGame
    while True:
        cls()
        G.menuScroll(G.mainMenu)
        x = input("\n\n     < ) >> ").lower()
        if x == "continue":
            cls()
            G.printAnim(G.fLocDisplay())
            wait(1)
            initDisplay()
        elif x == "new game" or x == "new":
            hasStartedGame = True
            BE.updCharVal()
            BE.initVar()
            BE.curLoc = [2, 0]
            initIntro()
        elif x == "settings" or x == "setting":
            initSettings()
        elif x == "characters" or x == "character":
            initChChar()
        elif x == "credits" or x == "credit":
            cls()
            G.menuScroll(G.creditMenu)
            input(f"\n\n{" " * 6}Press Enter to continue...")
        elif x == "exit":
            break
        else:
            input(f"\n{" " * 10}{x} is not a valid command! ")

def initSettings() -> None:
    cls()
    G.Cprint("Make sure to remember")
    G.Cprint("Your Keybinds! UI elements")
    G.Cprint("Will not change!")
    input(f"\n{" " * 6}Press Enter to continue...")
    while True:
        cls()
        G.menuScroll(G.settingMenu)
        x = input(f"\n{" " * 6}< ? ) >> ").lower()
        if x == "keybind" or x == "keybinds":
            initKeyChange()
        elif x == "load kbs" or x == "loadkb":
            try:
                with open('PyFiles/settings/__settings__.txt', 'r') as F:
                    L = F.readlines()
                    y = 0
                    for x in keybinds:
                        x = L[y]
                        y += 1
            except PermissionError:
                G.Cprint("Unable to read!", 5)
                input("     Press Enter to continue...")
            except FileNotFoundError:
                G.Cprint("File is deleted or doesn't exist...")
                input("     Press Enter to continue...")
            except Exception as e:
                raise e
        elif x == "save":
            BE.saveG()
            if BE.saveG() is True:
                input("\n     Game saved successfully!")
            elif BE.saveG() is False:
                input("     An error was raised... Press enter to abort... ")
        elif x == "load":
            BE.loadG()
        elif x == "back":
            break
        else:
            input(f"     {x} is not a valid option")

def initChChar() -> None:
    global charHead
    cls()
    x = 0
    while True:
        stats = [BE.newbieStats, BE.expertStats, BE.sustainerStats, BE.fallenStats]
        names = ["Newbie", "Expert", "Sustainer", "Fallen"]
        cls()
        if x < 0:
            x = len(stats) - 1
        elif x > len(stats) - 1:
            x = 0
        G.fCharMenu(x)
        y = input(f"\n\n{" " * 6}< \o/ ) >> ").lower()
        if y == "left":
            x -= 1
        elif y == "right":
            x += 1
        elif y == "get":
            if BE.charUnlock[x] is True:
                input("     This character is already bought.")
            elif stats[x]["price"] < BE.curBadges:
                BE.curBadges -= stats[x]["price"]
                input("     Successfully bought character!")
            elif stats[x]["price"] > BE.curBadges:
                input("     Badges are too low.")
        elif y == "equip":
            if BE.charUnlock[x] is True:
                BE.curChar = names[x]
                BE.updCharVal()
                G.updAVal()
                input(f"     You have chosen {names[x]}!")
            else:
                input("     Buy the character first!")
        elif y == keybinds["backKB"]:
            break
        else:
            input(f"\n     {y} is not a valid Command!")
    initMenu()

def initKeyChange() -> None:
    lf = keybinds["leftKB"]
    up = keybinds["upKB"]
    ri = keybinds["rightKB"]
    do = keybinds["rightKB"]
    ac = keybinds["ac"]
    ch = keybinds["checkKB"]
    ask = keybinds["askKB"]
    wa = keybinds["waitKB"]
    sl = keybinds["sleepKB"]
    ge = keybinds["getKB"]
    bac = keybinds["backKB"]
    me = keybinds["menuKB"]
    bag = keybinds["bagKB"]
    ta = keybinds["taskKB"]
    while True:
        cls()
        print(G.logo)
        G.menuScroll(G.fKeyCh())
        x = input(f"\n{" " * 6}< ? ) >> ").lower()
        if BE.curMenu == 0:
            if x == "left":
                lf = input(f"     < Current KB: {lf} ) >> ").lower()
            elif x == "up":
                up = input(f"     < Current KB: {up} ) >> ").lower()
            elif x == "right":
                ri = input(f"     < Current KB: {ri} ) >> ").lower()
            elif x == "down":
                do = input(f"     < Current KB: {do} ) >> ").lower()
        if BE.curMenu == 1:
            if x == "act":
                ac = input(f"     < Current KB: {ac} ) >> ").lower()
            elif x == "check":
                ch = input(f"     < Current KB: {ch} ) >> ").lower()
            elif x == "ask":
                ask = input(f"     < Current KB: {ask} ) >> ").lower()
            elif x == "wait":
                wa = input(f"     < Current KB: {wa} ) >> ").lower()
            elif x == "sleep":
                sl = input(f"     < Current KB: {sl} ) >> ").lower()
            elif x == "get":
                ge = input(f"     < Current KB: {ge} ) >> ").lower()
        if BE.curMenu == 2:
            if x == "back":
                bac = input(f"     < Current KB: {bac} ) >> ").lower()
            elif x == "menu":
                me = input(f"     < Current KB: {me} ) >> ").lower()
            elif x == "bag":
                bag = input(f"     < Current KB: {bag} ) >> ").lower()
            if x == "task":
                ta = input(f"     < Current KB: {ta} ) >> ").lower()
        if x == "L":
            BE.curMenu += 1
            if BE.curMenu > 2:
                BE.curMenu = 0
        elif x == "R":
            BE.curMenu -= 1
            if BE.curMenu < 0:
                BE.curMenu = 2
        elif x == "exit":
            break
        else:
            input(f"     {x} is not a Keybind in the menu!")
    cls()
    x = input("\n\n\n     Save Changes? [Y/n] > ").lower()
    if x == "n":
        return
    try:
        with open('PyFiles/settings/__settings__.txt', 'w') as F:
            for x in keybinds.values():
                F.write(f"{x}\n")
    except PermissionError:
        G.Cprint("Unable to save settings...")
        G.Cprint("Game is not allowed to write")
    except FileNotFoundError:
        G.Cprint("File doesn't exist.")
        G.Cprint("Recreate the settings file in:")
        G.Cprint("( PyFiles/settings )")
    except Exception as e:
        raise e

# - INITIALIZER -

def initGame() -> None:
    cls()
    wait(2)
    G.printAnim("ElectricSplash Presents...", "\n\n\n")
    wait(1)
    cls()
    BE.curLoc = [1, 0]
    print(G.logo + "\n")
    G.fLocDisplay()
    wait(2)
    input(f"\n\n{" " * 6}Press Enter to continue... ")
    BE.initVar()
    G.curMenu = 0
    initMenu()

if __name__ == "__main__":
    initGame()