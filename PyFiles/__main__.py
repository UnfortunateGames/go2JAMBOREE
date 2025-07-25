from cmds.__cmds__ import cls, wait
import backend.__backend__ as BE
import gui.__gui__ as G

# hopefully this isn't filled with a BUNCH of
# spaghetti code that is a whole wrap-around and
# can be written in like, idk under 300 lines.

# i'm deeply sorry for this lol

# yeah ngl we cooked if we try to read ts

hasStartedGame: bool = False

def initDeath() -> None:
    BE.deaths += 1
    cls()
    wait(2)
    G.printAnim("Your vision starts to fade...", "\n\n\n")
    wait(1)
    cls()
    if BE.checkDeath() == 1:
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
        print(f"\n\n\n{" " * 15}Game over!\n{" " * 14}Try again? :P")
        G.menuScroll(G.gameOver)
        x = input(f"\n\n\n{" " * 6}< ? ) >> ").lower()
        if x == "menu" or x == "back":
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
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"{" " * 5}< ! ? ) >> ").lower()
        if x == "left" and G.checkAct("l") is True:
            BE.curLoc[0] -= 1
            # animation soon!
        elif x == "up" and G.checkAct("u") is True:
            BE.curLoc[1] -= 1
            # animations soon!
        elif x == "right" and G.checkAct("r") is True:
            BE.curLoc[0] += 1
            # animations soon!
        elif x == "down" and G.checkAct("d") is True:
            BE.curLoc[1] += 1
            # animations soon!
        elif x == "back":
            break
        else:
            input(f"\n{" " * 6}I'm not allowed to go there!")
    G.curMenu = 0
    initDisplay()

def initAct():
    while True:
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"\n{" "* 5}< ! ? ) >> ")
        if x == "sleep" and BE.curLoc == [1, 0] and BE.canSleep is True:
            cls()
            BE.mvGTime(None)
            G.printAnim("You went to sleep...", "\n\n\n")
            wait(2)
            cls()
            initDisplay()
        elif x == "ask" and BE.curLoc == [0, 1]:
            BE.curTask = BE.taskList["list"][BE.curRNG]
            BE.heardTask = True
            for x in G.fTaskDialogue():
                cls()
                G.fLocDisplay()
                G.printAnim(x, "\n\n")
                wait(1)
            wait(1)
        elif x == "check":
            cls()
            print(G.fcheckSprite())
            print(G.fcheckActs())
            input(f"\n{" " * 6}Press Enter to continue...")
        elif x == "back":
            break
        else:
            input(f"\n{" " * 6}I'm not allowed to do that!")
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
        x = input(f"\n{" "}For how long? ( 'Back' to exit ) > ")
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
        cls()
        G.fLocDisplay()
        print(G.displayStat())
        G.actScroll()
        x = input(f"{" " * 5}< ! ) >> ").lower()
        if x == "move":
            G.curMenu = 1
            initMove()
        elif x == "act" or x == "acts":
            G.curMenu = 2
            initAct()
        elif x == "task":
            if G.checkAct("do") is True:
                cls()
                wait(1)
                G.printAnim("A few hours later...", "\n\n\n")
                BE.hPlayer("hp", BE.taskList[BE.curTask]["Drain"][0])
                BE.hPlayer("stamina", BE.taskList[BE.curTask]["Drain"][1])
                wait(2)
                cls()
                initDisplay()
            else:
                input(f"\n{" " * 9}I can't do that here.")
        elif x == "wait":
            G.curMenu = 3
            initWait()
        elif x == "menu":
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
    heads = [" o ", "<+>"]
    x = 0
    while True:
        stats = [BE.newbieStats, BE.expertStats]
        names = ["Newbie", "Expert"]
        cls()
        if x < 0:
            x = 1
        elif x > 1:
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
        elif y == "back":
            break
        else:
            input(f"\n{" " * 6}{y} is not a valid Command!")
    initMenu()

def initSettings() -> None:
    while True:
        cls()
        print(G.logo)
        G.menuScroll(G.settingMenu)
        x = input(f"\n{" " * 6}< ? ) >> ").lower()
        if x == "keybind":
            cls()
            print(f"\n\n\n{" " * 8}Keybinds will come soon!")
            wait(2)
        elif x == "save":
            BE.saveG()
            input(f"\n{" " * 5}Game saved successfully!")
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
    print("\n\n" + G.logo)
    wait(2)
    input(f"\n\n{" " * 6}Press Enter to continue... ")
    G.curMenu = 0
    initMenu()

if __name__ == "__main__":
    initGame()