from cmds.__cmds__ import cls, wait, Cprint
import backend.__backend__ as BE
import gui.__gui__ as G

# HOOOOOLLYYYYY SHIIIIIIII-
# This code makes me want to rip my insides out.
# No seriously.

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
menuKB: str = "menu"
backKB: str = "back"

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
        G.printAnim("Oh no... Your decay.", "\n\n\n")
        wait(1)
        G.printAnim("It's too severe...", "\n")
        wait(1)
        G.printAnim("I'm sorry...", "\n")
        wait(2)
        cls()
        print("\n\n")
        Cprint("Game over!")
        Cprint("Try again :P")
        G.menuScroll(G.gameOver)
        x = input(f"\n\n\n{" " * 6}< ? ) >> ").lower()
        if x == menuKB or x == backKB:
            initMenu()
        elif x == "continue?" or x == "continue":
            BE.initVar()
            initIntro()
    BE.hPlayer()
    G.printAnim("Oh you poor thing.", "\n\n\n")
    wait(1)
    G.printAnim("You can always try again.", "\n")
    wait(1)
    G.printAnim("As long as I am here.", "\n")
    wait(1)
    cls()
    wait(2)
    initDisplay()

def initMove():
    while True:
        BE.mvGTime()
        BE.updTVal()
        if BE.updTVal() == 1:
            BE.hPlayer("hp", BE.curDrainStats[0])
            BE.hPlayer("stamina", BE.curDrainStats[1])
        if BE.curStats[0] <= 0 or BE.curStats[1] == 0:
            initDeath()
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"{" " * 5}< ! ? ) >> ").lower()
        if x == leftKB and G.checkAct("l") is True:
            BE.curLoc[0] -= 1
            # animation soon!
        elif x == upKB and G.checkAct("u") is True:
            BE.curLoc[1] -= 1
            # animations soon!
        elif x == rightKB and G.checkAct("r") is True:
            BE.curLoc[0] += 1
            # animations soon!
        elif x == downKB and G.checkAct("d") is True:
            BE.curLoc[1] += 1
            # animations soon!
        elif x == backKB:
            break
        else:
            input(f"\n{" " * 6}I'm not allowed to go there!")
    G.curMenu = 0
    initDisplay()

def initPunish() -> None:
    dialogue = ["My creation.", "Why must you ignore me?", "You shalt not disobey.", "You must be punished."]
    for x in dialogue:
        cls()
        G.printAnim(x, "\n\n\n")
        wait(1)
    cls()
    BE.hPlayer("hp", -10)
    BE.hPlayer("stamina", -10)
    print(f"{f"{"#" * 40}\n" * 6}")
    wait(1.5)
    cls()
    print(f"{f"{":" * 40}\n" * 6}")
    wait(1)
    cls()
    print(f"{f"{"." * 40}\n" * 6}")
    wait(0.75)
    cls()
    wait(2)

def initAct():
    while True:
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"\n{" "* 5}< ! ? ) >> ")
        if x == sleepKB and BE.curLoc == [1, 0] and BE.canSleep is True:
            cls()
            BE.mvGTime(None)
            G.printAnim("You went to sleep...", "\n\n\n")
            wait(2)
            if BE.doneTask is False:
                initDisplay()
            cls()
            initDisplay()
        elif x == askKB and BE.curLoc == [0, 1]:
            BE.curTask = BE.taskList["list"][BE.curRNG]
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
            input(f"\n{" " * 6}Press Enter to continue...")
        elif x == backKB:
            break
        else:
            input(f"\n{" " * 6}I'm not allowed to do that here!")
    G.curMenu = 0
    initDisplay()

def initWait() -> None:
    if BE.canWait is False:
        input(f"{" " * 5}I'm tired of waiting...")
        return
    cls()
    G.fLocDisplay()
    print(G.displayStat())
    while True:
        x = int(input(f"\n{" "}For how long? ( 'Back' to exit ) > "))
        if x is not int:
            if x == "back":
                x = 0
                break
            input(f"\n{" " * 5}That's not a number...")
        else:
            BE.canWait = False
            break
    BE.mvGTime(x)
    if x != 0:
        cls()
        G.printAnim("A few hours of waiting...", "\n\n\n")
        wait(1)
    G.curMenu = 0
    initDisplay()

def initDisplay() -> None:
    while True:
        if BE.curStats[0] <= 0 or BE.curStats[1] <= 0:
            initDeath()
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"{" " * 5}< ! ) >> ").lower()
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
                G.printAnim("A few hours later...", "\n\n\n")
                BE.mvGTime(4)
                BE.hPlayer("hp", BE.taskList[BE.curTask]["Drain"][0])
                BE.hPlayer("stamina", BE.taskList[BE.curTask]["Drain"][1])
                BE.doneTask = True
                wait(2)
                cls()
                initDisplay()
            else:
                input(f"\n{" " * 9}I can't do that here.")
        elif x == waitKB:
            G.curMenu = 3
            initWait()
        elif x == menuKB:
            break
        else:
            input(f"\n{" " * 6}{x}? I can't do that...")
    initMenu()

def initIntro() -> None:
    dialogue1 = ["Hello.", "Are you here?", "Good.", "Open your eyes."]
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
    heads = [" o ", "<+>", "'@'", "(*)"]
    x = 0
    while True:
        stats = [BE.newbieStats, BE.expertStats, BE.sustainerStats, BE.fallenStats]
        names = ["Newbie", "Expert", "Sustainer", "Fallen"]
        cls()
        if x < 0:
            x = len(stats) - 1
        elif x > len(stats) - 1:
            x = 0
        localcharHead = heads[x]
        G.menuScroll(G.fCharMenu(x, localcharHead))
        y = input(f"\n\n{" " * 5}< \o/ ) >> ").lower()
        if y == "left":
            x -= 1
        elif y == "right":
            x += 1
        elif y == "equip":
            for y in range(0, 1):
                BE.curMaxStats[y] = stats[x]["max"][y]
                BE.curDrainStats[y] = stats[x]["drain"][y]
            input(f"{" " * 5}You have chosen {names[x]}!")
        elif y == backKB:
            break
        else:
            input(f"\n{" " * 6}{y} is not a valid Command!")
    initMenu()

def initKeyChange() -> None:
    global leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB
    while True:
        cls()
        print(G.logo)
        print(G.fkeyChange())
        x = input(f"\n{" " * 6}< ? ) >> ").lower()
        if x == "left":
            leftKB = input(f"{" " * 5}< Current KB: {leftKB} ) >> ").lower()
        elif x == "up":
            upKB = input(f"{" " * 5}< Current KB: {upKB} ) >> ").lower()
        elif x == "right":
            rightKB = input(f"{" " * 5}< Current KB: {rightKB} ) >> ").lower()
        elif x == "down":
            downKB = input(f"{" " * 5}< Current KB: {downKB} ) >> ").lower()
        elif x == "task":
            taskKB = input(f"{" " * 5}< Current KB: {taskKB} ) >> ").lower()
        elif x == "act":
            actsKB = input(f"{" " * 5}< Current KB: {actsKB} ) >> ").lower()
        elif x == "check":
            checkKB = input(f"{" " * 5}< Current KB: {checkKB} ) >> ").lower()
        elif x == "ask":
            askKB = input(f"{" " * 5}< Current KB: {leftKB} ) >> ").lower()
        elif x == "wait":
            waitKB = input(f"{" " * 5}< Choose a Keybind ) >> ").lower()
        elif x == "sleep":
            sleepKB = input(f"{" " * 5}< Choose a Keybind ) >> ").lower()
        elif x == "back":
            backKB = input(f"{" " * 5}< Choose a Keybind ) >> ").lower()
        elif x == "menu":
            menuKB = input(f"{" " * 5}< Choose a Keybind ) >> ").lower()
        elif x == "exit":
            break
        else:
            input(f"{" " * 5}{x} is not a Keybind!")
    cls()
    x = input(f"\n\n\n{" " * 5}Save Changes? [Y/n] > ").lower()
    if x == "n":
        return
    try:
        with open('PyFiles/settings/__settings__.txt', 'w') as F:
            KBlist = [leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB]
            for x in KBlist:
                F.write(f"{x}")
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
    global leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB
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
                    KBlist = [leftKB, upKB, rightKB, downKB, taskKB, actsKB, checkKB, askKB, waitKB, sleepKB, backKB, menuKB]
                    y = 0
                    for x in KBlist:
                        x = L[y]
                        y += 1
            except PermissionError:
                Cprint("Unable to read!", 5)
                input(f"{" " * 5}Press Enter to continue...")
            except FileNotFoundError:
                Cprint("File is deleted or doesn't ecit...")
                input(f"{" " * 5}Press Enter to continue...")
            except Exception as e:
                raise e
        elif x == "save":
            BE.saveG()
            if BE.saveG() is True:
                input(f"\n{" " * 5}Game saved successfully!")
            elif BE.saveG() is False:
                input(f"{" " * 5}An error was raised... Press enter to abort... ")
        elif x == "back":
            break
        else:
            input(f"{" " * 5}{x} is not a valid option")
    initMenu()

def initMenu() -> None:
    global hasStartedGame
    cls()
    G.menuScroll(G.mainMenu)
    x = input(f"\n\n{" " * 5}< ) >> ").lower()
    if x == "continue":
        BE.loadG()
        if hasStartedGame is False:
            hasStartedGame = True
            cls()
            G.printAnim(G.fLocDisplay(True))
            wait(1)
        initDisplay()
    elif x == "new game" or x == "new":
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
        initMenu()
    elif x == "exit":
        exit()
    input(f"\n{" " * 10}{x} is not a valid command! ")
    initMenu()

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