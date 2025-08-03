from cmds.__cmds__ import cls, wait, Cprint
import backend.__backend__ as BE
import gui.__gui__ as G

# HOOOOOLLYYYYY SHIIIIIIII-
# This code makes me want to rip my insides out.
# No seriously.

# ? Can this be multiple statements?
# ? or either hardcoded only..?

leftKB: str = "left"
upKB: str = "up"
rightKB: str = "right"
downKB: str = "down"
taskKB: str = "task"
actsKB: str = "acts"
checkKB: str = "check"
askKB: str = "ask"
waitKB: str = "wait"
sleepKB: str = "sleep"
getKB: str = "get"
menuKB: str = "menu"
backKB: str = "back"
bagKB: str = "bag"

hasStartedGame: bool = False

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
        dialogue = ["Oh...", "I'm sorry...", "You did not pass my test...", "You were perfect...", "MY CREATION.", "Though you have failed me..."]
        for x in dialogue:
            G.printAnim(x, "\n")
            wait(1)
        wait(1)
        while True:
            cls()
            print("\n\n")
            G.menuScroll(G.gameOver)
            x = input(f"\n\n\n{" " * 6}< ? ) >> ").lower()
            if x == menuKB or x == backKB:
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
    dialogue = ["Oh...", "Do not worry...", "For I am here...", "I will always forgive you..."]
    for x in dialogue:
        G.printAnim(x, "\n")
        wait(1)
    wait(1)
    cls()
    wait(2)
    initDisplay()

def initMove() -> None:
    while True:
        BE.mvGTime()
        BE.updTVal()
        if BE.updTVal() == 1:
            BE.hPlayer("hp", BE.curDrainStats[0])
            BE.hPlayer("stamina", BE.curDrainStats[1])
        if BE.checkDeath() > 0:
            initDeath()
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"{" " * 6}< ! ? ) >> ").lower()
        if x == leftKB and G.checkAct("l") is True:
            BE.curLoc[0] -= 1
            G.moveAnim()
        elif x == upKB and G.checkAct("u") is True:
            BE.curLoc[1] -= 1
            G.moveAnim()
        elif x == rightKB and G.checkAct("r") is True:
            BE.curLoc[0] += 1
            G.moveAnim()
        elif x == downKB and G.checkAct("d") is True:
            BE.curLoc[1] += 1
            G.moveAnim()
        elif x == backKB:
            break
        else:
            input(f"\n{" " * 6}I'm not allowed to go there!")
    G.curMenu = 0

def initPunish() -> None:
    dialogue = ["My creation.", "Why must you ignore me?", "You shalt not disobey.", "You must be punished."]
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

def initAct() -> None:
    while True:
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"\n{" "* 6}< ! ? ) >> ")
        if x == sleepKB and BE.curLoc == [1, 0] and BE.canSleep is True:
            cls()
            BE.mvGTime(None)
            G.fRandomDialogue("sleep")
            wait(2)
            if BE.doneTask is False:
                initPunish()
            break
        elif x == askKB and BE.curLoc == [0, 1]:
            for x in G.fTaskDialogue():
                cls()
                G.fLocDisplay()
                G.printAnim(x, "\n\n")
                wait(1)
            BE.heardTask = True
            wait(1)
        elif x == checkKB:
            cls()
            print(G.fcheckSprite())
            print(G.fcheckActs())
            input("\n     Press Enter to continue...")
        elif x == getKB:
            items = [None, "apple", "water", "meat"]
            if G.canCollect() == 0:
                input(f"{" " * 5}There is nothing here!")
            else:
                BE.inventory[items[G.canCollect()]] += 1
        elif x == backKB:
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
        print(G.displayStat())
        x = input(f"\n{" " * 6}Wait for night? [Y/n] > ").lower()
        if x == "n":
            break
        BE.GTime = 2
        BE.WTime = "Night"
        BE.updTVal()
        cls()
        wait(2)
        G.fRandomDialogue("wait", "\n\n\n")
        wait(1)
        break

def initInventory() -> None:
    while True:
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
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
        elif x  == backKB:
            break
        else:
            input(f"     {x} is not an item!")
    G.curMenu = 0

def initDisplay() -> None:
    while True:
        if BE.checkDeath() > 0:
            initDeath()
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input("     < ! ) >> ").lower()
        if x == "move":
            G.curMenu = 1
            initMove()
        elif x == actsKB:
            G.curMenu = 2
            initAct()
        elif x == taskKB:
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
        elif x == waitKB:
            initWait()
        elif x == bagKB:
            G.curMenu = 3
            initInventory()
        elif x == menuKB:
            break
        else:
            input(f"\n{" " * 6}{x}? I can't do that...")

def initIntro() -> None:
    dialogue1 = ["Hello?", "Are you here?", "Good.", "Open your eyes..."]
    dialogue2 = ["You are my creation.", "You are not ready.", "Now, you should go to my altar", "Go explore for yourself."]
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
            elif x == 3:
                input("     He hasnt fallen.")
            elif stats[x]["price"] > BE.curBadges:
                input("     Badges are too low.")
        elif y == "equip":
            if BE.charUnlock[x] is True:
                BE.curChar = names[x]
                BE.updCharVal()
                input(f"     You have chosen {names[x]}!")
            else:
                input("     Buy the character first!")
        elif y == backKB:
            break
        else:
            input("\n     {y} is not a valid Command!")
    initMenu()

def initKeyChange() -> None:
    global leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB, bagKB, getKB
    while True:
        cls()
        print(G.logo)
        G.menuScroll(G.fKeyCh())
        x = input(f"\n{" " * 6}< ? ) >> ").lower()
        if BE.curMenu == 0:
            if x == "left":
                leftKB = input(f"     < Current KB: {leftKB} ) >> ").lower()
            elif x == "up":
                upKB = input(f"     < Current KB: {upKB} ) >> ").lower()
            elif x == "right":
                rightKB = input(f"     < Current KB: {rightKB} ) >> ").lower()
            elif x == "down":
                downKB = input(f"     < Current KB: {downKB} ) >> ").lower()
        if BE.curMenu == 1:
            if x == "act":
                actsKB = input(f"     < Current KB: {actsKB} ) >> ").lower()
            elif x == "check":
                checkKB = input(f"     < Current KB: {checkKB} ) >> ").lower()
            elif x == "ask":
                askKB = input(f"     < Current KB: {askKB} ) >> ").lower()
            elif x == "wait":
                waitKB = input(f"     < Current KB: {waitKB} ) >> ").lower()
            elif x == "sleep":
                sleepKB = input(f"     < Current KB: {sleepKB} ) >> ").lower()
            elif x == "get":
                getKB = input(f"     < Current KB: {getKB} ) >> ").lower()
        if BE.curMenu == 2:
            if x == "back":
                backKB = input(f"     < Current KB: {backKB} ) >> ").lower()
            elif x == "menu":
                menuKB = input(f"     < Current KB: {menuKB} ) >> ").lower()
            elif x == "bag":
                bagKB = input(f"     < Current KB: {bagKB} ) >> ").lower()
            if x == "task":
                taskKB = input(f"     < Current KB: {taskKB} ) >> ").lower()
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
            KBlist = [leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB]
            for x in KBlist:
                F.write(f"{x}\n")
    except PermissionError:
        Cprint("Unable to save settings...")
        Cprint("Game is not allowed to write")
    except FileNotFoundError:
        Cprint("File doesn't exist.")
        Cprint("Recreate the settings file in:")
        Cprint("( PyFiles/settings )")
    except Exception as e:
        raise e

def initSettings() -> None:
    global leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB, getKB, bagKB
    cls()
    Cprint("Make sure to remember")
    Cprint("Your Keybinds! UI elements")
    Cprint("Will not change!")
    input(f"\n{" " * 6}Press Enter to continue...")
    while True:
        cls()
        G.menuScroll(G.settingMenu)
        x = input(f"\n{" " * 6}< ? ) >> ").lower()
        if x == "keybind" or x == "keybinds":
            initKeyChange()
        elif x == "load" or x == "load kbs" or x == "loadkb":
            try:
                with open('PyFiles/settings/__settings__.txt', 'r') as F:
                    L = F.readlines()
                    KBlist = [leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB, getKB, bagKB]
                    y = 0
                    for x in KBlist:
                        x = L[y]
                        y += 1
            except PermissionError:
                Cprint("Unable to read!", 5)
                input("     Press Enter to continue...")
            except FileNotFoundError:
                Cprint("File is deleted or doesn't ecit...")
                input("     Press Enter to continue...")
            except Exception as e:
                raise e
        elif x == "save":
            BE.saveG()
            if BE.saveG() is True:
                input("\n     Game saved successfully!")
            elif BE.saveG() is False:
                input("     An error was raised... Press enter to abort... ")
        elif x == "back":
            break
        else:
            input(f"     {x} is not a valid option")

def initMenu() -> None:
    global hasStartedGame
    while True:
        cls()
        G.menuScroll(G.mainMenu)
        x = input("\n\n     < ) >> ").lower()
        if x == "continue":
            BE.loadG()
            if BE.loadG() is False:
                input("     An error was raised... Press enter to abort... ")
            if hasStartedGame is False:
                hasStartedGame = True
                cls()
                G.printAnim(G.fLocDisplay(True))
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
    G.curMenu = 0
    initMenu()

if __name__ == "__main__":
    initGame()