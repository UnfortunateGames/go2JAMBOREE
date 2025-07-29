from cmds.__cmds__ import rRN
import gui.__gui__ as G 

# D.R.Y. won't be happy with this...

def PLanimalChance() -> bool:
    if rRN(0, 10) <= 6:
        return False
    elif rRN(0, 10) > 6:
        return True

taskList: dict = {
    "list": ["CT", "PM", "DE", "SC"],
    "CT": {
        "name": "Chop Trees.",
        "dialogues": ["Chop chop for the wood...", "Few barks of wood later"],
        "LocOpt": [0, 0],
        "Drain": [0, -6],
    },
    "PM": {
        "name": "Praise Me.",
        "dialogues": ["Hallelujah! Rejoice!", "Praise, praise, for our existance!"],
        "LocOpt": [0, 1],
        "Drain": [0, -4],
    },
    "DE": {
        "name": "Don't Eat.",
        "dialogues": ["Resist gluttony, must resist...", "The food looks more tasty"],
        "LocOpt": [0, 1],
        "Drain": [-3, -5],
    },
    "SC": {
        "name": "Sacrifice.",
        "dialogue": ["Sacrifice, to all the sins.", "You feel forgiven..."],
        "LocOpt": [0, 1],
        "Drain": [-6, -2],
    }
}

locList: dict = {
    "list": {
        0: ["FE", "Ca", "Sp", "Cl0"],
        1: ["Al", "SL", "Pl", "Cl1"]
    },
    "FE": {
        "name": "The Forest Entrance.",
        "specialAct": None,
        "specialFunc": None,
    },
    "Ca": {
        "name": "The Campsite.",
        "specialAct": None,
        "specialFunc": None,
    },
    "Sp": {
        "name": "My Spawn.",
        "specialAct": None,
        "specialFunc": None,
    },
    "Cl0": {
        "name": "A Cliff.",
        "specialAct": None,
        "specialFunc": None,
    },
    "Al": {
        "name": "His Altar.",
        "specialAct": None,
        "specialFunc": None,
    },
    "SL": {
        "name": "A Small Lake.",
        "specialAct": "collect",
        "specialFunc": 1,
    },
    "Pl": {
        "name": "Just plains.",
        "specialAct": "kill",
        "specialFunc": PLanimalChance(),
    },
    "Cl1": {
        "name": "More Cliffs",
        "specialAct": None,
        "specialFunc": None,
    }
}

def eat(food) -> None:
    if food == "meat":
        hPlayer("hunger", 4)

itemList: dict = {
    "list": ["Map", "Meat"],
    "Meat": {
        "desc": "Yum...",
        "sprite": None,
        "specialFunc": eat("meat")
    },
    "Apple": {}
}

newbieStats: dict = {
    "head": " o ",
    "body": "/|\ ",
    "desc": "My first creation.",
    "price": 0,
    "max": [10, 15, 10],
    "drain": [0, -1, -2]
}

expertStats: dict = {
    "head": "<+>",
    "body": "/|\ ",
    "desc": "Long forgotten.",
    "price": 15,
    "max": [20, 25, 15],
    "drain": [0, -3, -2]
}

sustainerStats: dict = {
    "head": "{@}",
    "body": "/U\ ",
    "desc": "Gluttony.",
    "price": 20,
    "max": [20, 12, 20],
    "drain": [-2, -1, -2]
}

fallenStats: dict = {
    "head": "(*)",
    "body": '"|"',
    "desc": "My angel, I'm sorry.",
    "price": 30,
    "max": [15, 1, 1],
    "drain": [-2, 0, 0]
}

charUnlock: list = [True, False, False, False]

curStats: list = [10, 15, 10]

curMaxStats: list = [10, 15, 10]
curDrainStats: list = [0, -2, -1]

curChar: str = "Newbie"
curHead: str = " o "
curBody: str = "/|\ "
curBadges: int = 0

curLoc: list = [2, 0]
curRNG: int = 0
curTask: str = None
inventory: dict = {
    "Meat": 0,
    "Apples": 0,
    "Map": 1
}

GTime: int = 0
curTime: int = 0
WTime: str = "Day"
Weth: str = None

canSleep: bool = False
heardTask: bool = False
doneTask: bool = False
canWait: bool = True

deaths: int = 0

def checkTask(n=int) -> bool:
    task = taskList[taskList["list"][curRNG]]
    if n == 1 and curTask != "CT":
        return False
    elif heardTask is False or doneTask is True:
        return False
    elif curLoc == task["LocOpt"]:
        return True
    return False

def hPlayer(stat=None, amount=None) -> None:
    if stat == "hp" or stat is None:
        if amount is None:
            curStats[0] = curMaxStats[0]
        else:
            curStats[0] += amount
    if stat == "stamina" or stat is None:
        if amount is None:
            curStats[1] = curMaxStats[1]
        else:
            curStats[1] += amount
    if stat == "hunger" or stat is None:
        if amount is None:
            curStats[2] = curMaxStats[2]
        else:
            curStats[2] += amount

def checkDeath() -> int:
    if curStats[0] <= 0:
        return 1
    elif curStats[1] <= 0:
        return 2
    return 0

def updTVal() -> any:
    global GTime, WTime, Weth, curTime, canSleep
    curTime = GTime % 3
    if GTime == 0:
        return 0
    elif curTime == 0:
        return 1
    if GTime == 12:
        GTime = 0
        if WTime == "Night":
            WTime = "Day"
            canSleep = False
        elif WTime == "Day":
            WTime = "Night"
            canSleep = True
        # The Weth variable will be unused until v0.4.0
        return 0

def mvGTime(amount=1) -> None:
    global GTime, WTime, curTask, doneTask, heardTask
    if amount is None:
        initVar()
        GTime -= 4
        WTime = "Day"
        updTVal()
        heardTask = doneTask = False
        hPlayer()
        return
    GTime += amount
    updTVal()
    x = updTVal()
    if x == 0:
        hPlayer("hp", curDrainStats[0])
        hPlayer("stamina", curDrainStats[1])

def updCharVal() -> None:
    global curStats, curMaxStats, curDrainStats, curHead, curBody
    if curChar == "Newbie":
        char = newbieStats
    elif curChar == "Expert":
        char = expertStats
    for x in range(0, 2):
        curMaxStats[x] = char["max"][x]
        curDrainStats[x] = char["drain"][x]
        curStats[x] = curMaxStats[x]
    curHead = char["head"]
    curBody = char["body"]

def initVar() -> None:
    global curRNG, curTask, GTime, doneTask, heardTask, canSleep, canWait
    canSleep = doneTask = heardTask = False
    canWait = True
    curRNG = rRN(0, 3)
    curTask = taskList["list"][rRN(0, len(taskList["list"]))]
    GTime = 0
    updTVal()

def saveG() -> None:
    try:
        with open('PyFiles/backend/saveFile/__save__.txt', 'w') as F:
            L = [curChar, curStats, curLoc, curRNG, curTask, doneTask]
            for x in L:
                F.write(f"{x}\n")
        return True
    except PermissionError:
        G.Cprint("Unable to save game...")
        G.Cprint("Current game will not load.")
        return False
    except FileNotFoundError:
        G.Cprint("Save file does not exist.")
        G.Cprint("Recreate the save file in:")
        G.Cprint("( PyFiles/backend/saveFile )")
        return False
    except Exception as e:
        raise e

def loadG() -> None:
    global curChar, curStats, curLoc, curRNG, curTask, doneTask, heardTask
    heardTask = False
    try:
        with open('backend/saveFile/__save__.txt', 'r') as F:
            L = F.readlines()
            if len(L) < 6:
                G.Cprint("Save File seems to be missing values or is empty...", 2)
                input(f"{" " * 5}( Save the game! ) Press enter to abort...")
            curChar = str(L[0])
            initVar(True)
            curStats = eval(L[1])
            curLoc = eval(L[2])
            curRNG = int(L[3])
            curTask = str(L[4])
            doneTask = bool(L[5])
        return True
    except PermissionError:
        G.Cprint("Unable to load game...")
        return False
    except FileNotFoundError:
        G.Cprint("File does not exist, start a new game.")
        return False
    except Exception as e:
        raise e
