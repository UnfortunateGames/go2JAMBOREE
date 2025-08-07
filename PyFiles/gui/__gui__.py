from cmds.__cmds__ import wait, rRN, cls
import backend.__backend__ as BE

# Might go insane over creating sprites

# Probably...

logo = """
       "====go-2================"
    .  |--. _ . . _  _  _  __ __|  .
    ."=|, ||-||v||-'| ||-'|- |- |=".
     "=|'_'| || ||_''_'| )'__'__|="
"""

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

def canCollect() -> int:
    if BE.curLoc == [0, 0]:
        return 1
    elif BE.curLoc == [2, 1]:
        return 2
    elif BE.curLoc == [1, 1]:
        if BE.IsThereAnimal is True:
            return 3
    return 0

def factionActs() -> str:
    return f"""
     What do I do? :
       ( Sleep )==============[ {"!" if BE.curLoc == [1, 0] and BE.canSleep is True else " "} ]
       ( Check )==============[ ! ]
       (  Ask  )==============[ {"!" if BE.curLoc == [0, 1] else " "} ]
       (  Get  )==============[ {"!" if canCollect() > 0 else " "} ]

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

gameOver: str = """
           GAME OVER!!

            > ( Menu / Back )

            > [  Continue?  ]
"""

mainMenu: str = """
           Main Menu:

            > (  Continue  )
            > (  New Game  )
            > (  Settings  )
            > ( Characters )
            > (  Credits   )

          X< 'Exit' to leave
"""

creditMenu: str = """
           Credits:
            
            Creator-[E-Splash]

               ts all i got.
"""

settingMenu: str = """
           Settings:

            > ( KeyBinds )
            > ( Load KBs )
            > (   Save   )
          
          < 'Back' to Main Menu
"""

def fKeyCh() -> str:
    if BE.curMenu == 0:
        return  """
           KeyBinds:
            ( Move KBs )
            > [ Left  ] 
            > [  Up   ]
            > [ Right ]
            > [ Down  ]


          < 'Exit' to Menu
"""
    elif BE.curMenu == 1:
        return """
           KeyBinds:
            ( Acts KBs )
            > [  Act  ]
            > [  Ask  ]
            > [ Check ]
            > [ Sleep ]
            > [  Get  ]

          < 'Exit' to Menu
"""
    elif BE.curMenu == 2:
        return """
           KeyBinds:
            ( Misc KBs )
            > [  Bag  ]
            > [ Tasks ]
            > [ Back  ]
            > [ Menu  ]

           < 'L'  |  'R' >
          < 'Exit' to Menu
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
"     '      "      "      '   .-."    "
  '      "      '    "  "  __ /;-/ '  "
 " " '    "   '      "     '-'--''   "  
"""

Pl1Spr: str = """
________________________________________
.  ____'....'"      "      '   .-."    "
 '( ;_'_'..'     '    "  "  __ /;-/ '  "
 " ||  | |    '      "     '-'--''   "  
"""

Cl1Spr: str = """
____________ . . . . . . . . . . . . . .
   '   "  |/-..--''--..--''--..--''--..-
  '  "   |/'..''..''..''..''..''..''..''
"  '  " //-..--''--..--''--..--''--..--'
"""

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

curHead: str = " o "
curBody: str = "/|\ "

head = list(curHead)
body = list(curBody)

def fCTAnim() -> str:
    return [
            f"""
{" " * 16} /\
{" " * 16}/  (>{curHead}
{" " * 16}/  \|{curBody}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16} /\ (>
{" " * 16}/  \/{curHead}
{" " * 16}/  \ \{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16} /\  --v
{" " * 16}/  \ /{head[1] + head[2]}
{" " * 16}/  \  {body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}   ,--.
{" " * 16}/ .\ {curHead}
{" " * 16}/ ^--/{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""

{" " * 16}/(>\ {curHead}
{" " * 16}/  '.-{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""

{" " * 16}/  (>{curHead}
{" " * 16}/  \|{curBody}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}    (>
{" " * 16}/  \/{curHead}
{" " * 16}/  \ \{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}     --v
{" " * 16}/  \ /{head[1] + head[2]}
{" " * 16}/  \  {body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}   ,--.
{" " * 16}  .  {curHead}
{" " * 16}/ ^--/{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""

{" " * 16} (>  {curHead}
{" " * 16}/  '.-{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""

{" " * 16}   (>{curHead}
{" " * 16}/  \|{curBody}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}    (>
{" " * 16}    /{curHead}
{" " * 16}/  \ \{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}     --v
{" " * 16}     /{head[1] + head[2]}
{" " * 16}/  \  {body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}   ,--.
{" " * 16}  .  {curHead}
{" " * 16}  ^--/{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""

{" " * 16} (>  {curHead}
{" " * 16}   '.-{body[1] + body[2]}
{" " * 16} ||  / \ 
""",
            f"""
{" " * 16}   (>{curHead}
{" " * 16}    |{curBody}
{" " * 16} ||  / \ 
"""
    ]

def fPMAnim() -> str:
    return [
    f"""
{" " * 16}
{" " * 16}{curHead} .___.
{" " * 16}{curBody}.|~|.
{" " * 16}/ \ '---'
""",
    f"""
{" " * 16}
{" " * 16}{curHead} .___.
{" " * 16}/,, .|~|.
{" " * 16} >> '---'
""",
    f"""
{" " * 16}
{" " * 16}{curHead} .___.
{" " * 16}/:  .|~|.
{" " * 16}>>  '---'
""",
    f"""
{" " * 16}
{" " * 16}    .___.
{" " * 16},{head[1]}: .|~|.
{" " * 16}>>  '---'
""",
    f"""
{" " * 16}     _ 
{" " * 16}    .___.
{" " * 16},{head[1]}" .|~|.
{" " * 16}>>  '---'
""",
    f"""
{" " * 16}     " .
{" " * 16}    |___'
{" " * 16},{head[1]}" .|~|.
{" " * 16}>>  '---'
""",
    f"""
{" " * 16}    | _''
{" " * 16}    '___|
{" " * 16},{head[1]}" .|~|.
{" " * 16}>>  '---'
""",
    f"""
{" " * 16}    ' " |
{" " * 16}    '___'
{" " * 16},{head[1]}" .|~|.
{" " * 16}>>  '---'
""",
    f"""
{" " * 16}    |   |
{" " * 16}    |___|
{" " * 16},{head[1]}" .|~|.
{" " * 16}>>  '---'
""",
    f"""
{" " * 16}    |   |
{" " * 16}    |___|
{" " * 16},{head[1]}. .|~|.
{" " * 16}> / '---'
""",
    f"""
{" " * 16}    |   |
{" " * 16} {curHead}|___|
{" " * 16}\/. .|~|.
{" " * 16}/ > '---'
""",
    f"""
{" " * 16}    |   |
{" " * 15}{curHead}  |___|
{" " * 16}<\> .|~|.
{" " * 16}/ \ '---'
""",
    f"""
{" " * 16}    |   |
{" " * 15}{curHead}  |___|
{" " * 16}<\> .|~|.
{" " * 16}/ \ '---'
""",
    f"""
{" " * 16}    |   |
{" " * 16}{curHead} |___|
{" " * 16}<{body[1]}> .|~|.
{" " * 16}/ \ '---'
""",
    f"""
{" " * 16}    |   |
{" " * 16}{curHead} |___|
{" " * 16}{curBody}.|~|.
{" " * 16}/ \ '---'
""",
    f"""
{" " * 16}    |   |
{" " * 16}{curHead} |___|
{" " * 16}{curBody}.|~|.
{" " * 16}/ \ '---'
""",
    ]

def fDEAnim() -> str:
    return [
    """ 
Hello World!
"""
    ]

def fSCAnim() -> str:
    return [
    """
Hello World!
"""
    ]

def fBTAnim() -> str:
    return [
    """
Hello World!
"""
    ]

locSprites: dict = {
    0: [FESpr, CaSpr, SpSpr, Cl0Spr],
    1: [AlSpr, SLSpr, [Pl0Spr, Pl1Spr], Cl1Spr]
}

curMenu: int = 0

def fcheckSprite() -> str:
    if BE.WTime == "Day":
        return DcheckSprite
    elif BE.WTime == "Night":
        return NcheckSprite

def fLocDisplay(returnSprite=False) -> None or str:
    sky = daySky if BE.WTime == "Day" else nightSky
    loc = locSprites[BE.curLoc[1]][BE.curLoc[0]]
    if BE.curLoc == [2, 1]:
        if BE.IsThereAnimal is True:
            loc = loc[1]
        elif BE.IsThereAnimal is False:
            loc = loc[0]
    Sprite = sky + loc
    if returnSprite is True:
        return Sprite
    print(Sprite)

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

def fInventoryMenu() -> str:
    return f"""
     Inventory:

       [ Meat  ]===============[ {BE.inventory["meat"]} ]
       [ Apple ]===============[ {BE.inventory["fruit"]} ]
       [ Water ]===============[ {BE.inventory["water"]} ]

    << 'Back' to main menu
"""

def fTaskDialogue() -> list:
    if BE.doneTask is True:
        return ["You have done your work.", "There is nothing else I can ask.", "Go ahead.", "Explore my creation."]
    elif BE.heardTask is False:
        return ["You came back.", f"Your task is {BE.taskList[BE.curTask]["name"]}", "Carry on."]
    return ["Did you forget?", f"I ordered you to {BE.taskList[BE.curTask]["name"]}"]

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

def displayStat() -> str:
    HPamnt = int(BE.curStats[0] // (BE.curMaxStats[0] / 10))
    noBar = "-" * (10 - HPamnt)
    hpgap = ""
    staminagap = ""
    if BE.GTime < 10:
        gtime = f" {BE.GTime}"
    else:
        gtime = BE.GTime
    if BE.WTime == "Day":
        wtime = "day  "
    elif BE.WTime == "Night":
        wtime = "night"
    if BE.doneTask is True:
        task = "is "
    elif BE.doneTask is False:
        task = "not"
    if BE.curStats[0] < 10:
        hpgap = " "
    if BE.curStats[1] < 10:
        staminagap = " "
    return f""".'.{curHead}.| Health  : {hpgap}{BE.curStats[0]} | Time: {gtime}      '.
|::{curBody}| Stamina : {staminagap}{BE.curStats[1]} | It is {wtime}    |
'.==HP==[{"#"*HPamnt}{noBar}]==| Task {task} Done .'"""

def actScroll() -> None:
    menus = [fmainActs(), fmoveActs(), factionActs(), fInventoryMenu()]
    print(f"_0_{" " * 34}_0_")
    print(f"| |{"~" * 34}| |")
    print(menus[curMenu])
    print(f"|_|{"~" * 34}|_|")
    print(f" 0{" " * 36}0")

def menuScroll(menu=str) -> None:
    print(f"\n{logo}\n{" " * 9}Made by ElectricSplash\n")
    print(f"{" " * 6}_0_{" " * 22}_0_")
    print(f"{" " * 6}| |{"~" * 22}| |")
    print(menu)
    print(f"{" " * 6}|_|{"~" * 22}|_|")
    print(f"{" " * 6} 0{" " * 24}0")

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

def taskAnim() -> None:
    if BE.curTask == "CT":
        anim = fCTAnim()
    elif BE.curTask == "PM":
        anim = fPMAnim()
    elif BE.curTask == "DE":
        anim = fCTAnim()
    elif BE.curTask == "SC":
        anim = fCTAnim()
    elif BE.curTask == "BT":
        anim = fCTAnim()
    for x in range(0, 16):
        cls()
        print(x)
        print(f"\n\n{" " * 11}_0_{" " * 11}_0_")
        print(f"{" " * 11}| |{"~" * 11}| |\n")
        print(anim[x])
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