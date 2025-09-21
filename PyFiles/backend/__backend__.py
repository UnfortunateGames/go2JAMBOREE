from cmds.__cmds__ import rRN
import gui.__gui__ as G

# - LISTS -

taskList: dict = {
    "list": ["CT", "PM", "DE", "SC", "BT", "CB"],
    "CT": {
        "name": "Chop Trees.",
        "dialogues": ["Chop chop for the wood...", "Few barks of wood later..."],
        "guide": ["Go to the forest entrance.", "There's some trees there."],
        "prize": 2,
        "LocOpt": [0, 0],
        "Drain": [0, -6, -3],
    },
    "PM": {
        "name": "Praise Me.",
        "dialogues": ["Hallelujah! Rejoice!", "Praise, praise, for our existance!"],
        "guide": ["Praise my altar.", "Praise it!"],
        "prize": 1,
        "LocOpt": [0, 1],
        "Drain": [0, -4, -2],
    },
    "DE": {
        "name": "Don't Eat.",
        "dialogues": ["Resist gluttony, must resist...", "The food looks more tasty..."],
        "guide": ["Come to the plains...", "...and resist gluttony."],
        "prize": 3,
        "LocOpt": [2, 1],
        "Drain": [-2, -4, -6],
    },
    "SC": {
        "name": "Sacrifice.",
        "dialogues": ["Sacrifice, to all the sins.", "You feel forgiven..."],
        "guide": ["Go to the upper cliff.", "You must sacrifice to me."],
        "prize": 4,
        "LocOpt": [3, 0],
        "Drain": [-6, -2, -4],
    },
    "BT": {
        "name": "Baptism.",
        "dialogues": ["Your sins were forgotten.", "Evil Nostalgia."],
        "guide": ["Baptise yourself..", "Come to my lake."],
        "prize": 1,
        "LocOpt": [1, 1],
        "Drain": [0, -4, -2]
    },
    "CB": {
        "name": "Celebrate.",
        "dialogues": ["Thank him for our sake!", "Oh we thank you!"],
        "guide": ["We rejoice!", "Celebrate at your camp."],
        "prize": 1,
        "LocOpt": [1, 0],
        "Drain": [0, -6, -2]
    }
    # Holy Water Creation task
    # Admire God's Creation Task
}

# ? Should probably rework this by v0.3.0

locList: dict = {
    "list": {
        0: ["FE", "Ca", "Sp", "Cl0"],
        1: ["Al", "SL", "Pl", "Cl1"]
    },
    "FE": "The Forest Entrance.",
    "Ca": "The Campsite.",
    "Sp": "My Spawn.",
    "Cl0": "A Cliff.",
    "Al": "His Altar.",
    "SL": "A Small Lake.",
    "Pl": "Just plains.",
    "Cl1": "More Cliffs"
}

itemList: dict = {
    "meat": {
        "desc": "Yum...",
        "sprite": None,
        "heal": [0, 2, 6]
    },
    "apple": {
        "desc": "Eat healthy!",
        "sprite": None,
        "heal": [2, 1, 3]
    },
    "water": {
        "desc": "Thirsty...",
        "sprite": None,
        "heal": [1, 5, 0]
    }
}

weaponList: dict = {
    "CA": {
        "name": "Crude Axe",
        "craftable": True,
        "materials": {
            "wood": 12,
            "horns": 0,
            "Wool": 0,
            "Leather": 0
        },
        "moveSet": {
            "list": ["Hack", "Slash", "Shove"],
            "Hack": [3, 0],
            "Slash": [12, 2],
            "Shove": [28, 4]
        },
    },
    "NA": {
        "name": "Normal Axe",
        "craftable": True,
        "materials": {
            "wood": 8,
            "horns": 0,
            "Wool": 0,
            "Leather": 4
        },
        "moveSet": {
            "list": ["Whack", "Slash", "Throw"],
            "Whack": [5, 0],
            "Slash": [12, 1],
            "Throw": [26, 2]
        },
    },
    "PA": {
        "name": "Pickaxe",
        "craftable": True,
        "materials": {
            "wood": 6,
            "horns": 2,
            "Wool": 0,
            "Leather": 4
        },
        "moveSet": {
            "list": ["Pick", "Crack", "Slash"],
            "Pick": [6, 0],
            "Crack": [22, 2],
            "Slash": [35, 3]
        },
    },
    "GB": {
        "name": "God's Blade",
        "craftable": False,
        "goal": 10,
        "moveSet": {
            "list": ["Chop", "Cut", "Cleave"],
            "Chop": [6, 0],
            "Cut": [15, 1],
            "Cleave": [65, 4]
        },
    }
}

# - ANIMAL STATS -

cow: dict = {
    "name": "Cow",
    "HP": 50,
    "defense": 2,
    "moveSet": {
        "list": ["Kick", "Rest"],
        "Kick": 5,
        "Rest": 8
    },
    # [meat, leather, wool, horn]
    "prize": [2, 2, 0, 0]
}

sheep: dict = {
    "name": "Sheep",
    "HP": 25,
    "defense": 0,
    "moveSet": {
        "list": ["Bump", "Sleep"],
        "Bump": 2,
        "Sleep": 12
    },
    "prize": [1, 0, 3, 0]
}

goat: dict = {
    "name": "Goat",
    "HP": 15,
    "defense": 6,
    "moveSet": {
        "list": ["Ram", "Preparation"],
        "Ram": 8,
        "Preparation": 2
    },
    "prize": [3, 0, 0, 2]
}

animalList: list = [cow, sheep, goat]

curAnimal: dict = None

# - YOUR STATS -

newbieStats: dict = {
    "head": " o ",
    "body": "/|\ ",
    "desc": "My first creation.",
    "def": 0,
    "moveSet": {
        "name": "Instincts",
        "list": ["Punch", "Kick", "Thrust"],
        "Punch": [2, 0],
        "Kick": [3, 1],
        "Thrust": [12, 4]
    },
    "price": 0,
    "max": [10, 15, 10],
    "drain": [0, -1, -2]
}

expertStats: dict = {
    "head": "<+>",
    "body": "/|\ ",
    "desc": "Long forgotten.",
    "def": 1,
    "moveSet": {
        "name": "Kung Fu",
        "list": ["Fist Hit", "Spin Kick", "Power Fist"],
        "Fist Hit": [3, 0],
        "Spin Kick": [5, 1],
        "Power Fist": [16, 3]
    },
    "price": 15,
    "max": [20, 25, 15],
    "drain": [0, -3, -2]
}

sustainerStats: dict = {
    "head": "{@}",
    "body": "/U\ ",
    "desc": "Gluttony.",
    "def": 3,
    "moveSet": {
        "name": "Sumo",
        "list": ["Crush", "Smash", "Push"],
        "Crush": [3, 0],
        "Smash": [5, 1],
        "Push": [20, 4]
    },
    "price": 20,
    "max": [20, 12, 20],
    "drain": [-2, -1, -2]
}

fallenStats: dict = {
    "head": "(*)",
    "body": '"|" ',
    "desc": "My angel, I'm sorry.",
    "def": 2,
    "moveSet": {
        "name": "Divine Power",
        "list": ["Divine Bolt", "Holy Smite", "God's Will"],
        "Divine Bolt": [2, 0],
        "Holy Smite": [3, 1],
        "God's Will": [12, 4]
    },
    "price": 30,
    "max": [15, 1, 1],
    "drain": [-2, 0, 0]
}

# - IN GAME STATS -

curChar: str = "Newbie"

curmoveSet: any = newbieStats["moveSet"]

# [hp, stamina, hunger]
curStats: list = [10, 15, 10]

curMaxStats: list = [10, 15, 10]
curDrainStats: list = [0, -2, -1]

curDefense: int = 0

curBag: dict = {
    "meat": 0,
    "fruit": 0,
    "water": 0
}

seenLocs: dict = {
    0: [False, False, True, False],
    1: [False, False, False, False]
}

# [Crude Axe, Normal Axe, Pickaxe, God's Blade]
curWeapons: list = [False, False, False, False]
curEquip: str = None 

curBadges: int = 0
# [newbie, expert, sustainer, fallen]
charUnlock: list = [True, False, False, False]

# - GAME VALUES -

curLoc: list = [2, 0]
curRNG: int = 0
curTask: str = None

GTime: int = 0
curTime: int = 0
WTime: str = "Day"
Weth: str = None

canSleep: bool = False
heardTask: bool = False
doneTask: bool = False
IsThereAnimal: bool = False
canWait: bool = True

deaths: int = 0

# - IF RETURN -

def PLanimalChance() -> bool:
    if rRN(0, 10) <= 6:
        return False
    elif rRN(0, 10) > 6:
        return True

def checkTask(n=int) -> bool:
    task = taskList[curTask]
    if n == 1 and curTask != "CT":
        return False
    elif heardTask is False or doneTask is True:
        return False
    elif curLoc == task["LocOpt"]:
        return True
    return False

def checkDeath() -> int:
    if curStats[0] <= 0:
        return 1
    elif curStats[1] <= 0:
        return 2
    return 0

# - VALUE MANIPULATION -

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

def updTVal() -> any:
    global GTime, WTime, Weth, curTime, canSleep
    curTime = GTime % 3
    if GTime == 0:
        return 0
    elif curTime == 0:
        return 1
    if GTime > 12:
        GTime = 0
        if WTime == "Night":
            WTime = "Day"
            canSleep = False
        elif WTime == "Day":
            WTime = "Night"
            canSleep = True
        # ! The Weth variable will be unused until v0.4.0
        return 0

def mvGTime(amount=1) -> None:
    global GTime, WTime, curTask, doneTask, heardTask
    if amount is None:
        initVar()
        GTime -= 4
        if GTime < 0:
            GTime += 12
        elif GTime > 12:
            GTime -= 12
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
    global curStats, curMaxStats, curDrainStats, curmoveSet, curDefense
    if curChar == "Newbie":
        char = newbieStats
    elif curChar == "Expert":
        char = expertStats
    elif curChar == "Sustainer":
        char = sustainerStats
    elif curChar == "Fallen":
        char = fallenStats
    for x in range(0, 2):
        curMaxStats[x] = char["max"][x]
        curDrainStats[x] = char["drain"][x]
        curStats[x] = curMaxStats[x]
    if curEquip is None:
        curmoveSet = char["moveSet"]
    else:
        curmoveSet = weaponList[curEquip]["moveSet"]
    curDefense = char["def"]
    G.curHead = char["head"]
    G.curBody = char["body"]

def initVar() -> None:
    global curRNG, curTask, GTime, doneTask, heardTask, canSleep, canWait, IsThereAnimal, deaths, curAnimal
    IsThereAnimal = PLanimalChance()
    canSleep = doneTask = heardTask = False
    canWait = True
    for x in range(0, 1):
        for y in range(0, 3):
            seenLocs[x][y] = False
    seenLocs[0][2] = True
    # ! curRNG unused until Weather is implemented
    # curRNG = rRN(0, 3)
    curAnimal = animalList[rRN(0, 2)]
    curTask = taskList["list"][rRN(0, len(taskList["list"]) - 1)]
    deaths = GTime = 0
    updTVal()

# - SAVE FILE -

def saveG() -> None:
    try:
        with open('PyFiles/backend/saveFile/__save__.txt', 'w') as F:
            L = [curChar, curStats, curBag["meat"], curBag["fruit"], curBag["water"], curBadges, charUnlock, curLoc, GTime, WTime, doneTask, deaths]
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
    global curChar, curStats, curBag, curBadges, charUnlock, curLoc, GTime, WTime, doneTask, deaths, heardTask
    try:
        with open('PyFiles/backend/saveFile/__save__.txt', 'r') as F:
            L = F.readlines()
            curChar = str(L[0])
            curStats = eval(L[1])
            curBag["meat"] = int(L[2])
            curBag["fruit"] = int(L[3])
            curBag["water"] = int(L[4])
            curBadges = int(L[5])
            charUnlock = eval(L[6])
            curLoc = eval(L[7])
            GTime = int(L[8])
            WTime = str(L[9])
            doneTask = bool(L[10])
            deaths = int(L[11])
        heardTask = doneTask
        return True
    except PermissionError:
        input("     Unable to load game...")
        return False
    except FileNotFoundError:
        input("     File does not exist, start a new game.")
        return False
    except Exception as e:
        raise e