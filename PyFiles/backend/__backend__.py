from cmds.__cmds__ import rRN

# This is the BACKEND of the game.
# (yeah no shit...)

# I'm just hoping you use most of this to
# interact with stats and not dump all
# stat management in __main__

taskList: dict = {
    "list": ["CT", "PM", "DE", "SC"],
    "CT": {
        "name": "Chop Trees.",
        "LocOpt": [0, 0],
        "Drain": [0, -6],
        "ActOption": "collect"
    },
    "PM": {
        "name": "Praise Me.",
        "LocOpt": [0, 1],
        "Drain": [0, -4],
        "ActOption": "praise",
    },
    "DE": {
        "name": "Don't Eat.",
        "LocOpt": [0, 1],
        "Drain": [-3, -5],
        "ActOption": None
    },
    "SC": {
        "name": "Sacrifice.",
        "LocOpt": [0, 1],
        "Drain": [-6, -2],
        "ActOption": "sacrifice"
    }
}

locList: dict = {
    "list": {
        0: ["FE", "Ca", "Sp", "Cl0"],
        1: ["Al", "SL", "Pl", "Cl1"]
    },
    "FE": {
        "name": "The Forest Entrance.",
        "specialAct": True,
        "specialFunc": 1,
    },
    "Ca": {
        "name": "The Campsite.",
        "specialAct": "Sleep",
        "specialFunc": 2,
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
        "specialAct": "Ask",
        "specialFunc": 3,
    },
    "SL": {
        "name": "A Small Lake.",
        "specialAct": None,
        "specialFunc": None,
    },
    "Pl": {
        "name": "Just plains.",
        "specialAct": None,
        "specialFunc": None,
    },
    "Cl1": {
        "name": "More Cliffs",
        "specialAct": None,
        "specialFunc": None,
    }
}

newbieStats: dict = {
    "max": [10, 15],
    "drain": [0, -2]
}

expertStats: dict = {
    "max": [20, 25],
    "drain": [0, -3]
}

curStats: list = [10, 15]

curMaxStats: list = [10, 15]
curDrainStats: list = [0, -2]

curChar: str = "Newbie"
curLoc: list = [2, 0]
curRNG: int = 0
curTask: dict = None

GTime: int = 0
curTime: int = 0
WTime: str = "Day"
Weth: str = None

canSleep: bool = False
heardTask: bool = False
doneTask: bool = False
canWait: bool = True

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
        # The Weth variable will be unused until v0.5.0
        return 0

def mvGTime(amount=1) -> None:
    global GTime, WTime, curTask, doneTask, heardTask
    if amount is None:
        initVar()
        GTime = 6
        WTime = "Day"
        updTVal()
        curTask = taskList[taskList["list"][rRN(0, len(taskList["list"]))]]
        hPlayer()
        return
    GTime += amount
    updTVal()
    x = updTVal()
    if x == 0:
        hPlayer("hp", curDrainStats[0])
        hPlayer("stamina", curDrainStats[1])

def specialLocAct() -> any:
    locCheck = locList[locList["list"][curLoc[1]][curLoc[0]]]
    if locCheck["specialAct"] is True:
        return locCheck["specialFunc"]
    elif locCheck["specialAct"] is str:
        return [locCheck["specialAct"], locCheck["specialFunc"]]

def initVar(onlyPlayer=False) -> None:
    global curStats, curMaxStats, curDrainStats, curRNG, GTime, doneTask, heardTask, canSleep, canWait
    if curChar == "Newbie":
        char = newbieStats
    elif curChar == "Expert":
        char = expertStats
    for x in range(0, 1):
        curMaxStats[x] = char["max"][x]
        curDrainStats[x] = char["drain"][x]
        curStats[x] = curMaxStats[x]
    if onlyPlayer:
        return
    canSleep = doneTask = heardTask = False
    canWait = True
    curRNG = rRN(0, 3)
    GTime = 0
    updTVal()

def saveG():
    try:
        with open('backend/saveFile/__save__.txt', 'w') as F:
            F.write(f"{curChar}\n")
            F.write(f"{curStats}\n")
            F.write(f"{curLoc}\n")
            F.write(f"{curRNG}\n")
            F.write(f"{curTask}\n")
            F.write(f"{doneTask}\n")
        return True
    except PermissionError:
        print("Unable to save game... Current game will not load after you exit.")
        return False
    except FileNotFoundError:
        print("File does not exist, creating new save file and retrying...")
        open('backend/saveFile/__save__.txt')
        saveG()
    except Exception as e:
        raise e

def loadG():
    global curChar, curStats, curLoc, curRNG, curTask, doneTask, heardTask
    heardTask = False
    try:
        with open('backend/saveFile/__save__.txt', 'r') as F:
            L = F.readlines()
            curChar = str(L[0])
            initVar(True)
            curStats = eval(L[1])
            curLoc = eval(L[2])
            curRNG = int(L[3])
            curTask = str(L[4])
            doneTask = bool(L[5])
        return True
    except PermissionError:
        print("Unable to load game...")
        return False
    except FileNotFoundError:
        print("File does not exist, start a new game.")
        return False
    except Exception as e:
        raise e
