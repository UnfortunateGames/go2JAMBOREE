from cmds.__cmds__ import wait, rRN, cls
import gui.__animations__ as A
import backend.__backend__ as BE

# - VALUES -

curHead: str = A.cHead
curBody: str = A.cBody

curMenu: int = 0

# - update animation values -
# This is implemented because of python avoiding circular import

def updAVal() -> None:
    A.cHead = curHead
    A.cBody = curHead

# - MAIN MENUS -

logo = """
       |.~~~go-2~~~~~~~~~~~~~~~.|
    .   --. _ . . _  _  _  __ __   .
    ."= , ||-||v||-'| ||-'|- |-  =".
     "= '_'| || ||_''_'| )'__'__ ="
"""

def menuScroll(menu=str) -> None:
    print(f"\n{logo}\n{" " * 9}Made by ElectricSplash\n")
    print(f"{" " * 6}_0_{" " * 22}_0_")
    print(f"{" " * 6}| |{"~" * 22}| |")
    print(menu)
    print(f"{" " * 6}|_|{"~" * 22}|_|")
    print(f"{" " * 6} 0{" " * 24}0")

mainMenu: str = """
           Main Menu:

            > (  Continue  )
            > (  New Game  )
            > (  Settings  )
            > ( Characters )
            > (  Credits   )

          X< 'Exit' to leave
"""

settingMenu: str = """
           Settings:

            > ( KeyBinds )
            > ( Load KBs )
            > (   Load   )
            > (   Save   )
          
          < 'Back' to Main Menu
"""

creditMenu: str = """
           Credits:
            
            Creator-[E-Splash]

               ts all i got.
"""

def fKeyCh() -> str:
    menus = ["""
           KeyBinds:
            ( Move KBs )
            > [ Left  ] 
            > [  Up   ]
            > [ Right ]
            > [ Down  ]


          < 'Exit' to Menu
""",
        """
           KeyBinds:
            ( Acts KBs )
            > [  Act  ]
            > [  Ask  ]
            > [ Check ]
            > [ Sleep ]
            > [  Get  ]

          < 'Exit' to Menu
""",
        """
           KeyBinds:
            ( Misc KBs )
            > [  Bag  ]
            > [ Tasks ]
            > [ Back  ]
            > [ Menu  ]

           < 'L'  |  'R' >
          < 'Exit' to Menu
"""
    ]
    return menus[curMenu]

def fCharMenu(x) -> str:
    charlist = [BE.newbieStats, BE.expertStats, BE.sustainerStats, BE.fallenStats]
    char = charlist[x]
    charHead = char["head"]
    charBody = char["body"]
    charPrice = char["price"]
    desc = char["desc"]
    if BE.charUnlock[x] is False:
        equip = f"{charPrice} Badges > Get"
    elif BE.charUnlock[x] is True:
        equip = "Unlocked! > Equip"
    else:
        equip = "Error!"
    Sprite = f"""
     _0_                        _0_
     | |~~~~~~~~~~~~~~~~~~~~~~~~| |

           Choose a Charcter:
           < Left  ][ Right >
          -> "{desc}"
           {charHead} Health  : {char["max"][0]}
           {charBody}Stamina : {char["max"][1]}
           / \  {equip}
          << 'Back' to Main Menu
    
    |_|~~~~~~~~~~~~~~~~~~~~~~~~~|_|
     0                           0
"""
    print(Sprite)

# - LOCATIONS -

NcheckSprite: str = """
*  *     *      *      *     *     *   *
  *    *     *   ,----,    *     *    *
    *          .' ' .  '.    *      *
 *     *      *| ; ().  |*     *      *
   *     *     '. :   >.'   *     *  *
     *       *   '----'   *       *   *
  *     *        *          *       *
"""

DcheckSprite: str = """
::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::;----;:::::::::::::::::
::::::::::::::::'      '::::::::::::::::
:::::::::::::::| < () > |:::::::::::::::
::::::::::::::::.      .::::::::::::::::
::::::::::::::::::----::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
"""

nightSky: str = """
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
 . .        .      .       .     .    ."""

daySky: str = """
:::::::::::::::::::::::::::::::::::'  ':
:::::::::::::::::::::::::::::::::::.  .:
':':':':':':':':':':':':':':':':':':':':"""

FESpr: str = """
/ \_//\_________________________________
/ .//  \ ---   . "     '     "     '  " 
 / \/  \   __ .  .    '   "     "      
 "|" |||  |  "    '    "     '    "    "
"""

CaSpr: str = """
______.----.____________________________
  "  / [] /|\ '   " '  "  . ___ . ______
 "  /____/_|_\ "   '   " _ . _____ . ___
    "   '     "    '     "    '   "  ' '
"""

SpSpr: str = """
________________________________________
_____ . __   " .-------.   '      "    "
__________ .  ( <=====> )   "      '  "
 " " '    "   ''-------'     "   '   "  
"""

Cl0Spr: str = """
____________ . . . . . . . . . . . . . .
 " "   '  /'::::::::::::::::::::::::::::
    "   '|;~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
"   ' " /; ~    ~      ~     ~     ~
"""

AlSpr: str = """
^./ \___________________________________
   '  "|  '  .___. "  '    "    '   "   
 "  '  '  '- .|~|.   "      "      '  "
  '   " '--  '---' ""   '  "   "  '  "  
"""

SLSpr: str = """
________________________________________
"     ' __.._.________.--.___     "    "
  '    /   ~      ~     ~   ~ \    '  "
 " " .'  ~     ~       ~   ~   '.    "  
"""

Pl0Spr: str = """
________________________________________
"     '      "      "      '    .-."     
  '      "      '    "  "   __ /;-/ '  "
 " " '    "   '      "     '-'--''   "  
"""

Pl1Spr: str = """
________________________________________
.  ____'....'"      "      '    .-."     
 '( ;_'_'..'     '    "  "  __ /;-/ '  "
 " | | | |    '      "     '-'--''   "  
"""

Pl2Spr: str = """
________________________________________
   ._..,.--.,"      "      '    .-."    "
 "(_____'..'     '    "  "  __ /;-/ '  "
 " |'|'| |    '      "     '-'--''   "  
"""

Pl3Spr: str = """
________________________________________
   ____|.--.|"      "      '    .-."     
 ,(_____'::'     '    "  "  __ /;-/ '  "
 " |'|'|'|    '      "     '-'--''   "  
"""

Cl1Spr: str = """
____________ . . . . . . . . . . . . . .
   '   "  |/-..--''--..--''--..--''--..-
  '  "   |/'..''..''..''..''..''..''..''
"  '  " //-..--''--..--''--..--''--..--'
"""

locSprites: dict = {
    0: [FESpr, CaSpr, SpSpr, Cl0Spr],
    1: [AlSpr, SLSpr, [Pl0Spr, Pl1Spr, Pl2Spr, Pl3Spr], Cl1Spr]
}

# - IF RETURN -

def checkAct(n=str) -> str:
    if n == "l" and BE.curLoc[0] != 0:
        return True
    elif n == "u" and BE.curLoc[1] != 0:
        return True
    elif n == "r" and BE.curLoc[0] != 3:
        return True
    elif n == "d" and BE.curLoc[1] != 1:
        return True
    elif n == "do":
        if BE.curLoc == [0, 1] or BE.checkTask() is True:
            return True
        elif BE.curLoc == [0, 0] or BE.curTask == "CT":
            return True
    elif n == "collect":
        if BE.curLoc == [0, 0] or BE.curLoc == [2, 1]:
            return True
    return False
  
def canCollect() -> int:
    if BE.curLoc == [0, 0]:
        return 1
    elif BE.curLoc == [2, 1]:
        return 2
    elif BE.curLoc == [1, 1] and BE.IsThereAnimal is True:
        if BE.curAnimal["name"] == "Cow":
            return 3
        elif BE.curAnimal["name"] == "Sheep":
            return 4
        elif BE.curAnimal["name"] == "Goat":
            return 5
    return 0

# - IN GAME MENUS -

def actScroll(auto=True, sprite=str) -> None:
    menus = [fmainActs(), fmoveActs(), factionActs(), fInventoryMenu()]
    print(f"_0_{" " * 34}_0_")
    print(f"| |{"~" * 34}| |")
    if auto is True:
        print(menus[curMenu])
    else:
        print(sprite)
    print(f"|_|{"~" * 34}|_|")
    print(f" 0{" " * 36}0")

def displayStat() -> str:
    HPamnt = int(BE.curStats[0] // (BE.curMaxStats[0] / 10))
    noBar = "-" * (10 - HPamnt)
    hggap = "" if BE.curStats[2] >= 10 else " "
    staminagap = "" if BE.curStats[1] >= 10 else " "
    gtime = f" {BE.GTime}" if BE.GTime < 10 else BE.GTime
    task = "is " if BE.doneTask is True else "not" 
    print(f""".'.{curHead}.| Hunger  : {hggap}{BE.curStats[2]} | Time: {gtime}      '.
|::{curBody}| Stamina : {staminagap}{BE.curStats[1]} | It is {BE.WTime}    |
'.==HP==[{"#"*HPamnt}{noBar}]==| Task {task} Done .'""")

def fLocDisplay(returnSprite=False) -> None or str:
    sky = daySky if BE.WTime == "Day" else nightSky
    loc = locSprites[BE.curLoc[1]][BE.curLoc[0]]
    if BE.curLoc == [2, 1]:
        if BE.IsThereAnimal is True:
            animals = {
                "Cow": Pl1Spr,
                "Sheep": Pl2Spr,
                "Goat": Pl3Spr
            }
            loc = animals[BE.curAnimal["name"]]
        elif BE.IsThereAnimal is False:
            loc = loc[0]
    Sprite = sky + loc
    if returnSprite is True:
        return Sprite
    print(Sprite)

def fmainActs() -> str:
    return f"""
     Main Options:
       (  Move  )=============[ ! ]
       (  Acts  )=============[ {"!" if BE.curLoc == [0, 1] or BE.curLoc == [1, 0]else " "} ]
       (  Task  )=============[ {"!" if BE.checkTask() is True else " "} ]
       (  Wait  )=============[ {"!" if BE.canWait is True else " "} ]
          >> [ 'Bag' ] ->
    << 'Menu' to Main Menu
"""

def fmoveActs() -> str:
    return f"""
     Move Where? :
                 [{"!" if BE.curLoc[1] != 0 else " "}]-.
        [{"!" if BE.curLoc[0] != 0 else " "}]-.    ( Up )
         ( Left )  <>  (Right)
                 (Down)   '-[{"!" if BE.curLoc[0] != 3 else " "}]
                 '-[{"!" if BE.curLoc[1] != 1 else " "}]
    < 'Back' to Main Options
"""

def factionActs() -> str:
    return f"""
     What do I do? :
       ( Sleep )==============[ {"!" if BE.curLoc == [1, 0] and BE.canSleep is True else " "} ]
       ( Check )==============[ ! ]
       (  Ask  )==============[ {"!" if BE.curLoc == [0, 1] else " "} ]
       (  Get  )==============[ {"!" if canCollect() > 0 and BE.IsThereAnimal is True else " "} ]

    < 'Back' to Main Options
"""

def fcheckActs() -> str:
    return f"""
     I can do these right now...
         [ ! = Can do | ~ = Can't ]

       ( Task  )==============[ {"!" if BE.doneTask is False else "~"} ]
       ( Sleep )==============[ {"!" if BE.canSleep is True else "~"} ]
       ( Wait  )==============[ {"!" if BE.canWait is True else "~"} ]
"""

def fInventoryMenu() -> str:
    return f"""
     Inventory:

       [ Meat  ]===============[ {BE.curBag["meat"]} ]
       [ Apple ]===============[ {BE.curBag["fruit"]} ]
       [ Water ]===============[ {BE.curBag["water"]} ]

    << 'Back' to main menu
"""

cowSpr: str = """
             .  ____'....'
              '( ;_'_'..'
                | | | |
"""

sheepSpr: str = """
                ._..,.--.,
              "(_____'..'
                |'|'| |
"""

goatSpr: str = """
                ____|....|
              '(_____'::'
                |'|'|'|
"""

animalSprites: list = [cowSpr, sheepSpr, goatSpr]

def fAnimalSprite() -> None:
    sprs = {
        "Cow": cowSpr,
        "Sheep": sheepSpr,
        "Goat": goatSpr
    }
    Sprite = sprs[BE.curAnimal["name"]]
    print(Sprite)

def fBattleMenu(cd1, cd2, cd3, chance) -> str:
    MS = BE.curmoveSet
    L = MS["list"]
    move1L = list(L[0])
    move1 = "".join(move1L) + (" " * (11 - len(move1L)))
    move2L = list(L[1])
    move2 = "".join(move2L) + (" " * (11 - len(move2L)))
    move3L = list(L[2])
    move3 = "".join(move3L) + (" " * (11 - len(move3L)))
    act1 = f"ON COOLDOWN! < {cd1} Turns left"
    if cd1 <= 0:
        act1 = f"> {move1} | {MS[L[0]][0]}{" " if MS[L[0]][0] < 10 else ""} ATK {MS[L[0]][1]}{" " if MS[L[0]][1] < 10 else ""} CD"
    act2 = f"ON COOLDOWN! < {cd2} Turns left"
    if cd2 <= 0:
        act2 = f"> {move2} | {MS[L[1]][0]}{" " if MS[L[1]][0] < 10 else ""} ATK {MS[L[1]][1]}{" " if MS[L[1]][1] < 10 else ""} CD"
    act3 = f"ON COOLDOWN! < {cd3} Turns left"
    if cd3 <= 0:
        act3 = f"> {move3} | {MS[L[2]][0]}{" " if MS[L[2]][0] < 10 else ""} ATK {MS[L[2]][1]}{" " if MS[L[2]][1] < 10 else ""} CD"
    return f"""
     {BE.curmoveSet["name"]} :

       {act1}
       {act2}
       {act3}

    << 'Run' to escape! ( {"  " if chance < 10 else " " if chance < 100 else ""}{chance}% )
"""

# def fanimalStats() -> str:
#     return f"""
# {" " * 10}( Health : {" " if BE.curStats[0]}{BE.curStats[0]} / {BE.curMaxStats[0]} )
# """

def fcheckSprite() -> str:
    if BE.WTime == "Day":
        return DcheckSprite
    elif BE.WTime == "Night":
        return NcheckSprite

gameOver: str = """
           GAME OVER!!

            > ( Menu / Back )

            > [  Continue?  ]
"""

# - ANIMATIONS -

def printAnim(m=str, before="") -> None:
    L = list(m)
    x = 3 / (len(L) * len(L))
    y = x
    b = " " * int((40 - len(L)) / 2)
    print(f"{before}{b}", end="", flush=True)
    for n in L:
        print(n, end="", flush=True)
        wait(y)
        y += x

def Cprint(message=str, spaces=None) -> None:
    if spaces is None:
        spaces = " " * int((40 - len(list(message))) / 2)
    print(spaces + message)

def taskAnim() -> None:
    animList = {
        "CT": A.fCTAnim(),
        "PM": A.fPMAnim(),
        "DE": A.fDEAnim(),
        "SC": A.fSCAnim(),
        "BT": A.fBTAnim(),
        "CB": A.fCBAnim()
    }
    for x in range(0, len(animList[BE.curTask])):
        cls()
        print(x)
        print(f"\n\n{" " * 11}_0_{" " * 11}_0_")
        print(f"{" " * 11}| |{"~" * 11}| |\n")
        print(animList[BE.curTask][x])
        print(f"{" " * 11}|_|{"~" * 11}|_|")
        print(f"{" " * 12}0{" " * 13}0")
        wait(0.2)
    print("\n\n")
    fRandomDialogue("task", "\n\n")
    wait(2)

def moveAnim() -> None:
    anim = ["/ \ ", "/<", "<|"]
    dots = 0
    for x in range(0, 15):
        cls()
        y = x % 3
        z = x % 5
        if z == 0:
            dots += 1
        print(f"\n\n{" " * 11}_0_{" " * 11}_0_")
        print(f"{" " * 11}| |{"~" * 11}| |\n")
        print(f"{" "* 18}{curHead}\n{" " * 18}{curBody}")
        print(" " * 18 + anim[y])
        print(f"{" " * 16}Moving{"." * dots}\n")
        print(f"{" " * 11}|_|{"~" * 11}|_|")
        print(f"{" " * 12}0{" " * 13}0")
        wait(0.15)

# - DIALOGUES -

def fTaskDialogue() -> list:
    if BE.doneTask is True:
        return ["You have done your work.", "There is nothing else I can ask.", "Go ahead.", "Explore my creation."]
    elif BE.heardTask is False:
        return ["You came back.", f"Your task is {BE.taskList[BE.curTask]["name"]}", BE.taskList[BE.curTask["name"]]["guide"][0], BE.taskList[BE.curTask["name"]]["guide"][1], "Carry on."]
    return ["Have you forgetten?", f"I ordered you to {BE.taskList[BE.curTask]["name"]}", BE.taskList[BE.curTask["name"]]["guide"][0], BE.taskList[BE.curTask["name"]]["guide"][1], "Carry on."]

def fRandomDialogue(dialogue, before) -> None:
    if dialogue == "task":
        dial = BE.taskList[BE.curTask]["dialogues"][rRN(0, 1)]
    elif dialogue == "sleep":
        x = ["Oh sweet relief of sleep...", "Tiring day isn't it?"]
        dial = x[rRN(0, 1)]
    elif dialogue == "wait":
        x = ["Hmmmm... Zen...", "The sun's setting..."]
        dial = x[rRN(0, 1)]
    printAnim(dial, before)