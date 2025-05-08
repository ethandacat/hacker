import time
import sys
import random

score = 0
score = 0

# Global functions
def slow(t, end=True):
  write(t, end, 0.2)


def fast(t, end=True):
  write(t, end, 0.02)


def write(t, end=True, inte=0.04):
  end = bool(end)
  t = "\033[32m".join(t.split("[!green]"))
  t = "\033[34m".join(t.split("[!blue]"))
  t = "\033[31m".join(t.split("[!red]"))
  t = "\033[0m".join(t.split("[!]"))
  for i in t:
    print(i, end='', flush=True)
    time.sleep(inte)
  if end:
    print("")


def die():
  global score
  enter()
  clear()
  write("You [!red]died[!].")
  enter()
  clear()
  write(
      """[!blue]....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
...........###########################################################################-.............
...........############################%####%##########%######################%#######=.............
...........:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..............
....................................................................................................
....................................................................................................
....................................................................................................
...........%%%-...+#%%......%%%%*......+%%%%%#+...:%%%-..-%%%*.:%%%%%#%#%-.:%%%#%%%%-...............
...........#%%-...+##%.....:%###%.....#%%%###%%%..:##%-.:%###..:#%%######-.:%#%##%%%%#..............
...........##%-...+#%%.....*##+%#=...:%%%-...#%%-.:%##-.%%##...:#%%=.......:%%%...:%%%:.............
...........##%-...+##%.....###:%##...:%%%:...=++:.:###-%###:....###=.......:###....###:.............
...........##%*+++###%....-#%*.#%#:..:%%%:........:#####%%:....:###*====:..:%##...-##%:.............
...........####%####%%....##%-.=##+..:%#%:........:#######+....:########+..:%#%%%###%:..............
...........#%%-...+##%....%##..:#%#..:%##:........:%%##:%#%:...:%##=.......:%#####%%:...............
...........%#%-...+%#%...+####%#%#%-.:##%:...###-.:%##-.=%##...:###=.......:%%#..+%##...............
...........%%%-...+#%%...##%+:-:*#%#.:%%%=..:%%%-.:%%%-..#%%#..:###=.......:#%%...%#%-..............
...........##%-...+##%..:%%#....-##%:.*#########..:###-..:%##=.:#%#%%##%#*.:%%#...-%##..............
...........+++:...-*+*..=+++.....**+-...=####+:...:*++:...-***..+*****+*+=.:*++....+**-.............
....................................................................................................
....................................................................................................
....................................................................................................
...........%%%#%%%%%%##%##%%#%##%%#%%:.......=##%%#*:......:%%####%#%%##%%###%###%#%#%=.............
...........##%#######%######%#######%:....-%#########%*....:%##############%##########=.............
.........................................+########%####%............................................
.........................................#####.....:####*...........................................
........................................:%###+......#####...........................................
...................................................:%%#%*...........................................
..................................................:%%##%............................................
.................................................=%%###.............................................
................................................#%####..............................................
..............................................:%%%##*...............................................
.............................................#%%##%:................................................
...........................................-%%%###..................................................
..........................................#####%-...................................................
........................................=%%%###::::::::::...........................................
........................................#%##%%#%%%%%###%#...........................................
........................................###############%#...........................................
....................................................................................................
............................................by.ethan................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
[!]

[!red]YOU DIED[!]
Score: """ + str(score), 0, 0)
  sys.exit()


def rand(n):
  return random.randint(1, n) == 1


ori = input

def num(n):
  p = ori()
  try:
    if int(p)>n or int(p)<0:
      raise ValueError
    return int(p)
  except Exception:
    write(
      "Joe Biden and the Federal Business-Interruption Agency are now investigating your computer of human activity."
    )
    write("You get arrested for being a human.")
    write("You are sentenced to 50 years in prison.")
    slow("Stupid.")
    die()

def input(c=False):
  global score
  score += 1
  ff = ori().lower()
  if (ff in "yes/y/1/ye/ye./yes./ya/ya./11/111/1111".split("/")):
    return True
  elif (
      ff in
      "no/n/0/2/no./noo/nooo/noooo/nooooo/noooooo/nooooooo/noooooooo/nooooooooo/noooooooooo/nooooooooooo"
      .split("/")):
    return False
  else:
    for i in "abcdefghijklmnopqrstuvwxyz":
      if i in ff:
        write(
            "Joe Biden and the Federal Business-Interruption Agency are now investigating your computer of human activity."
        )
        write("You get arrested for being a human.")
        write("You are sentenced to 50 years in prison.")
        slow("Stupid.")
        die()
    #empty
    if c:
      write("Again?")
      slow("Stupid.")
      die()
    write(
        """

          @@@@@@        
        @@@@@@%*@@@     
        @%%@@*@*#@@@    
        @@%@*+++*@@@    
        @@@@**@+@@@     
        @@@@@@*%@@@     
    @@%@@@@@@@@%##*@@@@ 
  @@@@@@@@@@@@@@@@@@@*@ 
 @@%@@@@@@@@@@@@@@@@%%@@
 @@@@@@@@@@@@@@@@@@@%*@@
 @@%@@@@@@@@@@@@@%@@##@@
@@@@@@@@@@@@@@@@@@@@%%@ 
 @@@@@@@@@@@@@@@@@@@@@@ 
  @@@@@@@@@@@@@@@@@@@   
     @@@@@@@@@@@@@@@@   

""", 1, 0)
    write("???:")
    write(
        "It seems like you pressed [!blue]ENTER[!] by accident. Please try again."
    )
    write(
        "[!blue]please... otherwise the costco police force will be on you![!]"
    )
    print("\033[0m")
    return input(True)
    

def enter():
  fast("Press [!blue][ENTER][!] to continue.")
  ori()


def clear():
  print("\033[H\033[J", end='')

# Intro
clear()
write(
    """


[!blue]....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
...........###########################################################################-.............
...........############################%####%##########%######################%#######=.............
...........:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..............
....................................................................................................
....................................................................................................
....................................................................................................
...........%%%-...+#%%......%%%%*......+%%%%%#+...:%%%-..-%%%*.:%%%%%#%#%-.:%%%#%%%%-...............
...........#%%-...+##%.....:%###%.....#%%%###%%%..:##%-.:%###..:#%%######-.:%#%##%%%%#..............
...........##%-...+#%%.....*##+%#=...:%%%-...#%%-.:%##-.%%##...:#%%=.......:%%%...:%%%:.............
...........##%-...+##%.....###:%##...:%%%:...=++:.:###-%###:....###=.......:###....###:.............
...........##%*+++###%....-#%*.#%#:..:%%%:........:#####%%:....:###*====:..:%##...-##%:.............
...........####%####%%....##%-.=##+..:%#%:........:#######+....:########+..:%#%%%###%:..............
...........#%%-...+##%....%##..:#%#..:%##:........:%%##:%#%:...:%##=.......:%#####%%:...............
...........%#%-...+%#%...+####%#%#%-.:##%:...###-.:%##-.=%##...:###=.......:%%#..+%##...............
...........%%%-...+#%%...##%+:-:*#%#.:%%%=..:%%%-.:%%%-..#%%#..:###=.......:#%%...%#%-..............
...........##%-...+##%..:%%#....-##%:.*#########..:###-..:%##=.:#%#%%##%#*.:%%#...-%##..............
...........+++:...-*+*..=+++.....**+-...=####+:...:*++:...-***..+*****+*+=.:*++....+**-.............
....................................................................................................
....................................................................................................
....................................................................................................
...........%%%#%%%%%%##%##%%#%##%%#%%:.......=##%%#*:......:%%####%#%%##%%###%###%#%#%=.............
...........##%#######%######%#######%:....-%#########%*....:%##############%##########=.............
.........................................+########%####%............................................
.........................................#####.....:####*...........................................
........................................:%###+......#####...........................................
...................................................:%%#%*...........................................
..................................................:%%##%............................................
.................................................=%%###.............................................
................................................#%####..............................................
..............................................:%%%##*...............................................
.............................................#%%##%:................................................
...........................................-%%%###..................................................
..........................................#####%-...................................................
........................................=%%%###::::::::::...........................................
........................................#%##%%#%%%%%###%#...........................................
........................................###############%#...........................................
....................................................................................................
............................................by.ethan................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
[!]


""", 0, 0.0004)
enter()
clear()

write(
    "Inspired by the game [!green]Hacker - A Story Game[BETA][!] by [!blue]LiquidPixel101[!] and [!green]TeamCoderz Productions[!]."
)
write("Go play the game here:")
write(
    "https[!]:[!]//replit.com[!]/[!]@LiquidPixel101/Hacker-A-Story-Game-BETA[!]#main.py"
)
slow("...")
write(
    "Well, feel free to [!green]start[!] the game when you are [!blue]ready[!]."
)
enter()
clear()

write(
    "[!red]WARNING[!]: [!blue]Typos[!] will result in [!red]death[!] by the [!blue]Federal Business-Interruption Agency[!] and the [!green]Costco Police Force[!]."
)
enter()
clear()

# JobI
write("After your ", 0)
slow("[!green]courtroom hearing[!]", 0)
write(
    ", [!]you have been [!green]released[!] from [!blue]all charges[!].[!][!][!]"
)
write("You can now [!green]go home[!].")
write(
    "Just as you were [!blue]about to leave[!], you see a [!blue]job opportunity[!] for a [!green]hacker[!] on your [!blue]phone[!]."
)
write(
    "You [!green]pick up[!] your [!blue]phone[!] to [!red]examine[!] the [!blue]job opportunity[!]."
)
write("Do you [!green]accept[!] the [!blue]job opportunity[!]?")
#accept
if not input():
  clear()
  write("You [!green]decide[!] to [!blue]go home[!].")
  write("You [!green]go home[!] and [!blue]live out[!] your [!green]life[!].")
  write("You run out of [!blue]money[!] and [!green]die[!].")
  slow("Stupid.")
  die()

write("So you accept the job.")
enter()
clear()

write("You have to go to the [!blue]job interview[!].")
write("They tell you to arrive at [!green]1:13 AM[!] flat.")
write("Do you take a [!blue]taxi[!]?")
if input():
  clear()
  write("You take a [!blue]taxi[!].")
  write("The taxi driver works at the [!green]Costco Police Force[!].")
  write(
      "You get [!red]incorrectly arrested[!] for [!blue]escaping from jail[!]."
  )
  die()
clear()
write("You walk to the [!blue]job interview[!].")
write("You arrive at [!green]1:14 AM[!].")
write("You enter the office.")
enter()
clear()

employer = """


       %%@@             
     %%+::-*%           
     %=++:*##           
     =-::--:=           
      -+#..-            
       **===            
     #%:+++=            
   %%%%%%+=:%%%%%       
*%%%%%%%%%%-%%%%%%      
%%%@%%%%%%%%=%%%@@%-    
*%%%%%%@%%%%@%%%%@@-=   
 %%@@@@@@@@%@%%@@@+-@%  
 %%%@@@@@@@@@@@@@+-%%%%%
  %@@@-=-------%%@%%@@@@
  #%@@=**----*%%%%%@@@@ 
   +@@@@%@@@@@@@@@@%    
    %@@@@@@@@@@@@@@     
    @@@@@@@@@@@@@@@@    
   =%@@@@@@@@@@@@@@@    
   %%@@@@@@@@@@@@@@@%   




"""
write(employer, 0, 0)
write("Employer:", 1, 0)
write(
    "Hi! I am [!blue]John[!]. I will be your [!green]boss[!] here at the [!red]Cats' Resistance[!]."
)
write(
    "Before we [!green]start[!], I need to know some things [!blue]about you[!]."
)
write("Should we [!green]start[!]?")
if not input():
  write("Oh, okay.")
  write("Should we [!green]start?[!]")
  if not input():
    write("Well, I guess you [!green]don't want[!] to [!blue]work[!] here.")
    enter()
    clear()
    write(
        "You [!green]go home[!] and [!blue]live out[!] your [!green]life[!].")
    write("But you are [!red]broke[!] and [!green]die[!].")
    slow("Stupid.")
    die()

#interview
write("We will start the [!blue]interview[!].")
enter()
clear()

write(employer, 0, 0)
write("Employer:", 1, 0)
write("What is your [!green]name[!]?")
name = ori()
write("Nice to meet you, [!blue]" + name + "[!].")

# Task 1
write("\nYour first task is to hack into the [!blue]Costco Police Force[!].")
enter()
clear()

computer = """
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Windows        |  |  |     |         |      |
     |  |  Powershell     |  |  |/----|`---=    |      |
     |  |  C:\\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \\,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'

"""

write(computer, 0, 0)
write("\n\n\n")
ori("Python 3.12, windows 10.0.19045.3086\nCopyright (c) Microsoft Corporation. All rights reserved.\n\nC:\\Users\\"
    + name + "\\AppData\\Roaming\\Python\\Python312\\python.exe\n\n")
ori()
ori()
ori()
ori()
slow("...")
enter()
clear()

write(employer, 0, 0)
write("Employer:", 1, 0)
write("Did you finish the [!blue]task[!]?")
if not input():
  write("Maybe you should [!green]do better[!].")
  write("You are a slow [!red]hacker[!].")
  write("You are [!blue]FIRED[!]!")
  enter()
  clear()
  write("You [!green]go home[!] and [!blue]live out[!] your [!green]life[!].")
  write("You run out of [!blue]money[!] and [!green]die[!].")
  die()

write("Good job!")
enter()
clear()

write("[!red]THE NEXT DAY...[!]")
enter()
clear()

# Task 2
write(employer, 0, 0)
write("Employer:", 1, 0)
write("Your next task is to hack into the [!blue]Amazon Webspace[!].")
write("Also, did I mention your [!green]salary[!]?")
write("You will be [!blue]given[!] [!green]$30[!] per [!blue]hour[!].")
enter()
clear()

write(computer, 0, 0)
write("\n\n\n")
ori("Python 3.12, windows 10.0.19045.3086\nCopyright (c) Microsoft Corporation. All rights reserved.\n\nC:\\Users\\"
    + name + "\\AppData\\Roaming\\Python\\Python312\\python.exe\n\n")
ori()
ori()
ori()
write(
    "SmartWrite(c) by the Underground Civilians Union has detected that you have finished writing your [!red]program[!]."
)
write("Would you like to [!green]run[!] it?")
if not input():
  write("Too bad.")
write("Running...")
write("...")
enter()
clear()

write("""
         
   /\\   /\\ /\\    /\\   --->  /----\\  |\\  |
  /--\\  | | |   /--\\    /   |    |  | \\ |
 /    \\ | | |  /    \\  <--- \\----/  |  \\|
                                 Webspace

          =======ENTER THE PORTAL=======
""")
enter()
clear()

write("Hey! Who are [!blue]you[!]?")
write("[!red]What do you do?[!]")
write("1. [!green]Say[!] your [!blue]name[!].")
write("2. [!green]Say[!] you work [!blue]here[!].")

slow("[!][!]")

if not input():
  write("I work here, at [!blue]Amazon Webspace[!]. My name is [!green]" +
        name + "[!].")
  enter()
  clear()
  write(
      "You get put in jail for [!red]lying[!] to the Federal Business-Interruption Agency."
  )
  die()

write("I am [!blue]" + name + "[!].")
enter()
clear()

write("[!red]THE NEXT DAY...[!]")
enter()
clear()

write(employer, 0, 0)
write("Employer:", 1, 0)
write("Did you finish the [!blue]task[!]?")
if not input():
  write("Don't lie, I see you did.")
write("I see your little [!blue]hack[!].")
write("What [!red]damage[!] did you do?")
ori()
write("It's okay, you did well.")
enter()
clear()

write(employer, 0, 0)
write("Employer:",1,0)
write("Well, today you will be [!blue]hacking[!] into the [!green]Alphabet Umbrella[!].")
write("They own [!blue]Google[!] and [!green]Hackers' Defense Union[!]. Be careful of them, unfortunately they aren't stupid dingbats.")
write("Well, off you [!blue]go[!]!")
enter()
clear()

# Section K

write(computer, 0,0)
write("Employer:",1,0)
write("By the way you won't need your computer today!")
write("")
write("Do you want to [!green]take[!] your [!blue]computer[!] with you to the [!red]Alphabet Umbrella[!]?")
k1 = input()
if k1:
  write("You [!green]take[!] your [!blue]computer[!] with you.")
else:
  write("You [!green]leave[!] your [!blue]computer[!].")
enter()
clear()

write("You [!green]arrive[!] at the [!red]Alphabet Umbrella[!].")
write("As you go [!blue]inside[!], you see a [!green]guard[!].")
write("You make a [!green]run[!] for the [!blue]entrance[!].")
write("The [!green]guard[!] [!blue]notices[!] you.")
write("What do you do?")
write("Press 1 to [!green]Run[!].")
write("Press 2 to [!green]Dodge[!].")
write("Press 3 to [!green]Attack[!].")

# dodge, attack, run (no comp)
# dodge, run, attack(no comp)
# dodge, run, dodge, attack (comp)
k2 = num(3)
if k2==3:
  write("You [!green]attack[!] the [!green]guard[!].")
  write("You get [!red]swarmed[!] by the [!blue]Federal Business-Interruption Agency[!] and the [!green]Costco Police Force[!].")
  die()
elif k2==2:
  write("You [!green]dodge[!] the [!red]guard's[!] attack.")
  write("What do you do next?")
  write("Press 1 to [!green]Run[!].")
  write("Press 2 to [!green]Dodge[!].")
  write("Press 3 to [!green]Attack[!].")
  k3 = num(3)
  if k3==3:
    write("You [!green]attack[!] the [!green]guard[!].")
    write("More guards are [!red]closing[!] on you!")
    write("What do you do next?")
    write("Press 1 to [!green]Run[!].")
    write("Press 2 to [!green]Dodge[!].")
    write("Press 3 to [!green]Attack[!].")
    k4 = num(3)
    if k4==3:
      write("You [!green]attack[!] the [!green]guards[!].")
      write("You get [!red]swarmed[!] by the [!blue]guards[!].")
      write("You get sent to [!red]jail[!].")
      slow("Stupid.")
      die()
    elif k4==2:
      write("You attempt to [!green]dodge[!] the [!green]guards[!].")
      write("You get [!red]swarmed[!] by the [!blue]guards[!].")
      write("You get sent to [!red]jail[!].")
      die()
    if k1:
      write("You [!green]run[!] with your [!blue]computer[!].")
      write("Your computer [!blue]slows[!] you [!red]down[!] and you get [!green]caught[!].")
      die()
    write("You [!green]run[!].")
  elif k3==2:
    write("The guards [!red]expect[!] that you would [!green]dodge[!].")
    write("They [!green]catch[!] you.")
    die()
  elif k3==1:
    if k1:
      write("You [!green]run[!] with your [!blue]computer[!].")
      write("Your computer [!blue]slows[!] you [!red]down[!] and the guards [!green]close in[!].")
      write("What do you do?")
      write("Press 1 to [!green]Run[!].")
      write("Press 2 to [!green]Dodge[!].")
      write("Press 3 to [!green]Attack[!].")
      k5 = num(3)
      if k5==1:
        write("You try to run.")
        write("However, the [!blue]guards[!] are expecting this.")
        write("You get [!red]caught[!].")
        die()
      elif k5==2:
        write("You [!green]dodge[!].")
        write("One guard [!blue]misses[!]!")
        write("You send a message to your [!blue]boss[!].")
        write("Backup [!red]is on the way[!].")
        enter()
        clear()
        write("Backup [!blue]arrives[!].")
        write("This [!green]gives[!] you the opportunity to [!blue]escape[!].")
      else:
        write("You [!green]attack[!] the [!green]guards[!].")
        write("You catch them off guard.")
        write("They get [!blue]pushed back[!].")
        write("However, more guards are [!red]closing in[!].")
        write("You get [!red]caught[!].")
        die()
    write("You [!green]run[!].")
    write("However, the [!red]guards[!] are [!blue]catching[!] up!")
    write("What do you do?")
    write("Press 1 to [!green]Run[!].")
    write("Press 2 to [!green]Dodge[!].")
    write("Press 3 to [!green]Attack[!].")
    k5 = num(3)
    if k5==1:
      write("You try to run.")
      write("However, the [!blue]guards[!] are expecting this.")
      write("You get [!red]caught[!].")
      die()
    elif k5==2:
      write("You [!green]dodge[!].")
      write("One guard [!blue]misses[!]!")
      write("You get excited.")
      write("However, the other guards [!red]catch[!] you.")
      die()
    write("You [!green]attack[!] the [!green]guards[!].")
    write("You catch them off guard.")
    write("They get [!blue]pushed back[!].")
    write("You run.")
elif k2==1:
  write("You [!green]run[!].")
  write("You make it back to [!blue]work[!].")
  write("Your [!red]boss[!] is [!green]mad[!].")
  write("You get [!red]fired[!].")
  die()

enter()
clear()


write(employer, 0, 0)
write("Employer:", 1, 0)
write("Welcome back, [!blue]" + name + "[!].")
write("What did you do?")
ori()
write("Oh, that's [!red]cool[!]!")
write("Well, you should get some rest. See you tommorrow!")
enter()
clear()

write("[!red]THE NEXT DAY...[!]")
enter()
clear()

# Task 3
write(employer, 0, 0)
write("Employer:", 1, 0)
write("Your final task is to go with [!blue]Jacob[!] here and hack into the [!red]Meganet[!]. It will be hard. However, Jacob is a [!green]experienced[!] hacker and mission specialist.")
write("Good luck!")
enter()
clear()

jacob = """

         %                  
       @%#%%@%%             
      @@@%%%#%%@%           
      @@@@@*#:*%%           
       @@%+#:-=%@           
       @@#=+..:%@           
       %@%%=:-@@@#          
       @%@##--+%@#          
    %%@@@@---:%*##**        
  #%#@#%%@@@@@@*#****#      
  %%@@*%%@##%####*#*#*      
 @@#*@#%#@##%#####%*+#      
 @@%@@#%#@##%#%@######=     
 %@@%@%%%%%%%#%@%#%####     
 %%%@@%%%%%#%%#-@#@%##*     
 #%%@@%@%%%%%%%%@%@@@##     

"""

write(jacob, 0, 0)
write("Jacob:", 1, 0)
write("Hey, [!blue]" + name + "[!]! I am [!green]Jacob[!].")
write("I am the [!blue]mission specialist[!].")
write("Let's [!green]start[!].")
enter()
clear()

write(computer, 0,0)
write("Python 3.12, windows 10.0.19045.3086\nCopyright (c) Microsoft Corporation. All rights reserved.\n\nC:\\Users\\Jacob\\AppData\\Roaming\\Python\\Python312\\python.exe\n\n")
for i in """
import time
import sys
import hacktool
import meganet

meganet.enter(time = time.time, pass=hacktool.psi("595933".fcr))
sys.ctrl("de")
hacktool.jp(meganet, sys)
hacktool.ret = meganet
meganet.enter(hacktool.getretspec())
""":
  print(i, end='', flush=True)
  time.sleep(random.uniform(0.0001, 0.0005))

time.sleep(3)
write("SmartWrite(c) by the Underground Civilians Union has detected that you have finished writing your [!red]program[!].")
write("Would you like to [!green]run[!] it?")
slow("yes")
enter()
clear()

fast("""

univ3rsal univ3rsal univ3rsal univ3rsal univ3rsal univ3rsal 
megan3t megan3t megan3t megan3t megan3t megan3t megan3t 
join join join join join join join join join join join join 

by Opot Sarcophsis and the Federal Business-Interruption Agency.

""")
enter()
clear()

# Section N(10 moves)
write("You and Jacob enter the [!red]Meganet[!].")
write("A guard [!red]spots[!] you!")
write("What do you do?")
write("Press 1 to [!green]Run[!].")
write("Press 2 to [!green]Dodge[!].")
write("Press 3 to [!green]Attack[!].")
n1 = num(3)
if n1==3:
  write("Jacob doesn't quite [!green]agree[!] with your [!red]decision[!].")
  write("You get [!red]overpowered[!] by the guards.")
  write("You get [!red]caught[!].")
  die()
elif n1==2:
  write("You dodge the [!green]attack[!], but [!blue]Jacob[!] doesn't.")
  write("Jacob gets [!red]caught[!] and sent away.")
  write("What do you do?")
  write("Press 1 to [!green]Run[!].")
  write("Press 2 to [!green]Dodge[!].")
  write("Press 3 to [!green]Attack[!].")
  n2 = num(3)
  if n2==3:
    write("You [!green]attack[!] the [!green]guards[!].")
    write("They don't [!green]expect[!] this and you are able to gain the upper hand for a little.")
    write("However, more guards are [!red]closing in[!].")
    write("What do you do?")
    write("Press 1 to [!green]Run[!].")
    write("Press 2 to [!green]Dodge[!].")
    write("Press 3 to [!green]Attack[!].")
    n3 = num(3)
    if n3==3:
      write("You [!green]attack[!] the [!green]guards[!].")
      write("They don't [!green]expect[!] this and you are able to gain the upper hand for a little.")
      write("However, [!red]you get caught[!].")
      die()
    elif n3==2:
      write("You [!green]dodge[!] the [!green]guards[!].")
      write("You get [!red]swarmed[!] and [!blue]caught[!].")
      die()
    else:
      write("You [!green]run[!].")
      write("The [!red]guards[!] are catching up.")
  elif n2==2:
    write("You [!green]dodge[!] the [!green]guards[!].")
    write("You get [!red]swarmed[!] and [!blue]caught[!].")
    die()
  else:
    write("You [!green]run[!].")
    write("The [!red]guards[!] are catching up.")
    write("What do you do?")
    write("Press 1 to [!green]Run[!].")
    write("Press 2 to [!green]Dodge[!].")
    write("Press 3 to [!green]Attack[!].")
    n3 = num(3)
    if n3==3:
      write("You [!green]attack[!] the [!green]guards[!].")
      write("However, this time they are more [!red]prepared[!].")
      write("You get [!red]caught[!].")
      die()
    elif n3==2:
      write("You [!green]dodge[!] the [!green]guards[!].")
      write("However, you are [!red]swarmed[!] and [!blue]caught[!].")
      die()
    else:
      write("You run.")
      write("However, the [!red]guards[!] are [!blue]catching up[!].")
else:
  write("You [!green]run[!] and [!red]leave[!] Jacob behind.")
  write("When you get back to [!blue]work[!], you get [!red]fired[!].")
  write("You [!green]go home[!] and [!blue]live out[!] your [!green]life[!].")
  write("You run out of [!blue]money[!] and [!green]die[!].")
  slow("Stupid.")
  die()

# N4 & N5 PIN
enter()
clear()
write("A person approaches you, supposedly being hired by your boss, appears and wants to tell you something.")
write("Do you trust this person?")
n4 = input()
if n4:
  write("He [!red]backstabs[!] you and laughs.")
  die()
write("He continues to beg you to [!green]trust[!] him.")
write("Do you trust this person?")
n5 = input()
if n5:
  write("Mysterious Man:",1,0)
  slow("0431",0)
  write(" is the PIN.")
enter()
clear()

# Section N (part 2)
write("While you were [!blue]busy[!] with the [!red]Mysterious Man[!], the [!green]Costco Police Force[!] starts to [!red]close in[!] on you.")
write("What do you do?")
write("Press 1 to [!green]Run[!].")
write("Press 2 to [!green]Dodge[!].")
write("Press 3 to [!green]Attack[!].")
n6 = num(3)
if n6==3:
  write("You [!red]attack[!] the guards.")
  write("They [!blue]expect[!] this and the [!green]Costco Police Force[!] surrounds you.")
  write("They [!red]catch[!] you.")
  die()
elif n6==2:
  write("You [!green]dodge[!] one of the guards attacks.")
  write("What do you do?")
  write("Press 1 to [!green]Run[!].")
  write("Press 2 to [!green]Dodge[!].")
  write("Press 3 to [!green]Attack[!].")
  n7 = num(3)
  if n7==3:
    write("You [!red]attack[!] the guards.")
    write("They [!blue]expect[!] this and the [!green]Costco Police Force[!] surrounds you.")
    write("They [!red]catch[!] you.")
    die()
  elif n7==2:
    write("You [!blue]dodge[!] the guards.")
    write("What do you do next?")
    write("Press 1 to [!green]Run[!].")
    write("Press 2 to [!green]Dodge[!].")
    write("Press 3 to [!green]Attack[!].")
    n8=ori()
    if n8==3:
      write("You [!red]attack[!] the guards.")
      write("However, you quickly get overpowered and [!red]caught[!] by the [!green]Costco Police Force[!].")
      die()
    elif n8==2:
      write("The [!green]guards[!] expect this and they [!red]catch[!] you.")
      die()
  else:
    write("You [!green]run[!].")
    write("When you get back to [!blue]work[!], you get [!red]fired[!].")
    write("You [!green]go home[!] and [!blue]live out[!] your [!green]life[!].")
    write("You run out of [!blue]money[!] and [!green]die[!].")
    slow("Stupid.")
    die()
else:
  write("You [!green]run[!].")
  write("When you get back to [!blue]work[!], you get [!red]fired[!].")
  write("You [!green]go home[!] and [!blue]live out[!] your [!green]life[!].")
  write("You run out of [!blue]money[!] and [!green]die[!].")
  slow("Stupid.")
  die()

# Section N (part 3)
write("You find a [!red]lock[!] on the ground.")
write("Do you want to [!blue]pick it up[!]?")
n9 = input()
if not n9:
  write("You don't pick up the lock.")
else:
  write("You pick up the lock.")
write("Meanwhile, the guards have come closer to you.")
write("What do you do?")
write("Press 1 to [!green]Run[!].")
write("Press 2 to [!green]Dodge[!].")
write("Press 3 to [!green]Attack[!].")
time.sleep(1)
slow("Press 4 to commit [!][!][!red]Suicide[!].")
n10 = num(4)
if n10==4:
  write("You give yourself up to them.")
  write("They kill you.")
  enter()
  clear()
  slow("[!red]YOU DIED[!]")
  time.sleep(1)
  write("or did you?")
  slow("...")
  write("Ok I was joking.")
  write("Stall for time.")
  write("OR MAYBE YOU DIDNT DIE???!?!?!?!")
  write("P.S. you did.")
  die()
elif n10==3:
  write("You [!red]attack[!] the guards.")
  write("You manage to [!green]gain[!] some [!blue]space[!].")
  write("You see helicopters [!blue]above[!] you, and you [!red]recgonize[!] that your [!green]boss[!] is on it.")
elif n10==2:
  write("The [!green]guards[!] expect this and they [!red]catch[!] you.")
  die()
else:
  write("You [!green]run[!].")
  write("However, they [!red]expect[!] this and they [!blue]catch[!] you.")
  die()

enter()
clear()

write("You [!green]enter[!] the helicopter.")
enter()
clear()

write(employer, 0,0)
write("Employer: ",1,0)
write("How did you do?")
ori()
write("So anyways time to go back to [!green]HQ[!]!")
enter()
clear()
if n9:
  write("Turns out that lock had a tracker on it.")
  write("Yeah, you're in prison.")
  write("Yaey.")
  slow("NOW DIE.")
  die()

write(employer,0,0)
write("Employer: ",1,0)
write("Okay, so now we need to break into the [!red]ColaVault[!].")
write("or the [!blue]PepsiVault[!].")
write("they're the same thing.")
write("Anyways, we do not know the [!green]PIN[!], so this is going to take a long time.")
write("You there, do you know the [!green]PIN[!]?")
if not n5:
  slow("No..?")
  write("You know what? There's no point trying.")
  write("Time to commit suicide.")
  die()
if not input():
  write("You know what? There's no point trying.")
  write("Time to commit suicide.")
  die()
write("Oh great! What is the [!green]PIN[!]?")
slow("0431")
write("Okay, let's go!")
enter()
clear()

write("Soon, you enter the [!red]ColaVault[!].")
write("You see a computer labeled: [!green]CONFIDENTIAL COMPUTER - DO NOT USE![!]")
write("Do you use this computer?")
if not input():
  write("Too bad.")
if True:
  write("You open the [!blue]computer[!].")
  enter()
  clear()
  write(f"""\n\n\n---  ----   ---\n|__  |___\\   |\n|    |___/  ---\nCONFIDENTIAL DOCUMENTS\n\n/logs/tracker/people/1391033.log\nARNOLD THE AWESOME\nStatus: In Prison\nCrime: Murdered 1391032\nTRACKED - Known to be in contact with {name}.\n\n/logs/tracker/people/1334953.log\n{name.upper()}\nSTATUS: Hunted\nCrime: Treason to Government(via Cat's Resistance)\nBOUNTY - $5,000\n\n/history/main.txt\nThe FBI is a system created by Junes Viafel and Sejal Sumen.\n\n/history/resistance.txt\nThe resistance was started by Ivan Zong and Arnold the Awesome.\n\n/logs/tracker/people/1328483.log\nIVAN ZONG\nStatus: Hunted\nCrime: Treason to Government, 17 murders, 95 injured, illegal gun, IHS Rule 2303.\nBOUNTY - $1,000,000,000\n\n""",1,0)
enter()
clear()

write("[!red]TO BE CONTINUED...[!]")
enter()
clear()

write("""
GAME OVER - You won!

Thank you to LiquidPixel101 for making the original version of the game!
I highly recommend you check it out.

Anyways, IDK if I will release Hacker 3.
So um, enjoy?""")
enter()
clear()
write("Why are you still here?")
enter()
clear()
fast("LEAVE RIGHT NOW UR BOTHERING ME")
enter()
clear()
write("Whatever... your fault.")
die()
