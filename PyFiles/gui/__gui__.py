from cmds.__cmds__ import wait
import backend.__backend__ as BE

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
        if BE.curLoc == [0, 1] or BE.curLoc != [1, 0]:
            return True
    return False

def fmainActs() -> str:
    return f"""
     Main Options:
       (  Move  )=============[ ! ]
       (  Acts  )=============[ {"!" if BE.curLoc == [0, 1] or BE.curLoc == [1, 0]else " "} ]
       (  Task  )=============[ {"!" if BE.checkTask is True else " "} ]
       (  Wait  )=============[ {"!" if BE.canWait is True else " "} ]
    
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

           ( KeyBinds )[SOON]
           > (  Save  )
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
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
 . .        .      .       .     .    .
/ \_//\_________________________________
/ .//  \ ---   . "     '     "     '  " 
 / \/  \   __ .  .    '   "     "      
 "|" |||  |  "    '    "     '    "    "
"""

CaSpr: str = """
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
   .        .      .       .     .    .
______.----.____________________________
  "  / [] /|\ '   " '  "  . ___ . ______
 "  /____/_|_\ "   '   " _ . _____ . ___
    "   '     "    '     "    '   "  ' '
"""

SpSpr: str = """
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
   .        .      .       .     .    .
________________________________________
_____ . __   " .-------.   '      "    "
__________ .  ( <=====> )   "      '  "
 " " '    "   ''-------'     "   '   "  
"""

Cl0Spr: str = """
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
   .        .      .       .     .    .
____________ . . . . . . . . . . . . . .
 " "   '  /'::::::::::::::::::::::::::::
    "   '|;~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
"   ' " /; ~    ~      ~     ~     ~
"""

AlSpr: str = """
  .   .       .        . .    .   .';o'.
.     .        .      .    .      '.',.'
  .     .    .      .       .     .    .
^./ \___________________________________
   '  "|  '  .___. "  '    "    '   "   
 "  '  '  '- .|~|.   "      "      '  "
  '   " '--  '---' ""   '  "   "  '  "  
"""

SLSpr: str = """
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
   .        .      .       .     .    .
________________________________________
"     ' __.._.________.--.___     "    "
  '    /   ~      ~     ~   ~ \    '  "
 " " .'  ~     ~       ~   ~   '.    "  
"""

PlSpr: str = """
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
   .        .      .       .     .    .
________________________________________
"     '      "      "      '      "    "
  '      "      '    "      "      '  "
 " " '    "   '      "       "   '   "  
"""

Cl1Spr: str = """
  .   .       .        . .    .   .';o'.
.       .        .      .    .    '.',.'
   .        .      .       .     .    .
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

locSprites: dict = {
    0: [FESpr, CaSpr, SpSpr, Cl0Spr],
    1: [AlSpr, SLSpr, PlSpr, Cl1Spr]
}

curMenu: int = 0

def fLocDisplay() ->  str:
    return locSprites[BE.curLoc[1]][BE.curLoc[0]]

def fCharMenu(x, y) -> str:
    charlist = [BE.newbieStats["max"], BE.expertStats["max"]]
    char = charlist[x]
    Stats = [0, 1]
    Stats[0] = char[0]
    Stats[1] = char[1]
    return f"""
          < Left    |    Right >
           Health: {y}
            > {Stats[0]}   /|\  Stamina:
                   / \  > {Stats[1]}
        < 'Back' to Main Menu
"""

def fTaskDialogue() -> list:
    if BE.doneTask is True:
        return ["You have done your work.", "There is nothing else I can ask.", "Go ahead.", "Explore my creation"]
    elif BE.heardTask is False:
        return ["You came back.", f"Your task is {BE.taskList[BE.curTask]["name"]}.", "Carry on."]
    return ["Did you forget?", f"I ordered you to {BE.taskList[BE.curTask]["name"]}"]

def printAnim(m=str, before=str) -> None:
    L = list(m)
    x = 3.5 / (len(L) * len(L))
    y = x
    b = " " * int((40 - len(L)) / 2)
    print(before + b, end="", flush=True)
    for n in L:
        print(n, end="", flush=True)
        wait(y)
        y += x

def displayStat() -> str:
    HPamnt = int(BE.curStats[0] // (BE.curMaxStats[0] / 10))
    noBar = "-" * (10 - HPamnt)
    hpgap = ""
    staminagap = ""
    if BE.curStats[0] < 10:
        hpgap = " "
    if BE.curStats[1] < 10:
        staminagap = " "
    return f""".'..o..| Health  : {hpgap}{BE.curStats[0]} |..//_Electric..'.
|::/|\:| Stamina : {staminagap}{BE.curStats[1]} |:/_ /-Splash-:::|
'.==HP==[{"#"*HPamnt}{noBar}]==|==//===========.'"""

def actScroll() -> None:
    menus = [fmainActs(), fmoveActs(), factionActs()]
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
