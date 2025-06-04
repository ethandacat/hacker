#VERSION 3.0.0
#WARNING: DO NOT LOOK AT THIS OR RISK SPOILERS.
import datetime
import os
import sys
import time
import random

today = datetime.date.today()

def color(color):
  if (color=="d"):#default (black)
    print("\033[0m")
  elif (color=="r"):#red
    print("\033[31m")
  elif color=="g":#green
    print("\033[32m")
  elif color=="y":#yellow
    print("\033[33m")
  elif color=="b":#blue
    print("\033[34m")
  elif color=="p":#purple
    print("\033[35m")
  elif color=="c":#cyan
    print("\033[36m")
  elif color=="w":#white
    print("\033[37m")
def enter():
  print("\033[0m"+"Press "+"\033[34m"+"[Enter] "+"\033[0m"+"to continue ->")
  input()
  clear()
  clear()

def clear():
  print("\033[H\033[J", end='')

def write(words):
  for char in words:
    time.sleep(0.03)
    sys.stdout.write(char)
    sys.stdout.flush()
  print()


def fastwrite(words):
  for char in words:
    time.sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
  print()


def slowwrite(words):
  for char in words:
    time.sleep(0.25)
    sys.stdout.write(char)
    sys.stdout.flush()
  print()

def intput(prompt):
  print(prompt,end="")
  user=input()
  i=0
  while user=="":
    if (i>=5):
      i=0
      clear()
    fastwrite("Oops! It seems like you pressed [Enter]"+"\033[34m"+" accidentally"+"\033[0m"+".\nPlease retype your response.\n")
    print(prompt,end="")
    i+=1
    user=input()
  return user
def yes(user):  #If the user says yes
  if user.lower() in ("1", "one", "yes.", "ye.", "yes", "ye", "yeah", "yeah.",
                      "y", "sure", "sure.", "lol", "heinkan", "heinkan.",
                      "beinkan", "beinkan.", "yea", "yea.", "beinkan!",
                      "heinkan!", "thisiswrong", "ya", "ya.", "yep", "yep.",
                      "ok","duh","duh!","of course!","of course","definetly","definetly."):
    return True
  return False


def no(user):  #if the user says no
  if user.lower() in ("2", "two", "no.", "no", "nope", "nope.", "n", "nah",
                      "nah.", "nah, bro!", "bro", "bruh", "no, why would i?",
                      "nah bro", "nah, bro", "thisiswrong"):
    return True
  return False

print("\033[0m")
def die(user):  #check if incorrect keyword
  if not no(user) and not yes(user):
    write("You didnt enter the correct keyword.")
    write("\nThe Costco Police Force arrests you.\n")
    write("Incorrect keyword is punishable by death.\n")
    death=["executed by lethal injection.","burned at stake.", "shot.", "beheaded.", "boiled alive.", "crucified.", "cut apart by chainsaws.", "hanged.", "whipped to death.", "hit to death.", "electrocuted.", "gassed.", "crushed by an elephant deliberately.", "drowned to death deliberately.", "thrown off a cliff.","stabbed to death.","left in a locked room forever with no food/water.","thrown into a crusher that crushes your whole body into powder.","buried alive.","mauled by a bear.", "eaten by a cougar.", "dead"]
    #22 ways to die lol
    print("\033[31m")
    write("You are "+death[random.randint(0,21)])
    endtime = time.time()
    os._exit(0)
def die1(user):  #check if incorrect keyword
  if not no(user) and not yes(user):
    write("You didnt enter the correct keyword.")
    write("\nThe Costco Police Force arrests you.\n")
    write("Incorrect keyword is punishable by death.\n")
    death=["executed by lethal injection.","burned at stake.", "shot.", "beheaded.", "boiled alive.", "crucified.", "cut apart by chainsaws.", "hanged.", "whipped to death.", "hit to death.", "electrocuted.", "gassed.", "crushed by an elephant deliberately.", "drowned to death deliberately.", "thrown off a cliff.","stabbed to death.","left in a locked room forever with no food/water.","thrown into a crusher that crushes your whole body into powder.","buried alive.","mauled by a bear.", "eaten by a cougar."]
    #21 ways to die lol
    print("\033[31m")
    write("You are "+death[random.randint(0,20)])
    print("\033[0m")
    afire()
  

#playsound('song.mp3')
print("\033[31m")
print("**FULLSCREEN RECOMMENDED**")
print("\033[32m")
print('''  __ __            __                                      
  / // /___ _ ____ / /__ ___  ____                          
 / _  // _ `// __//  '_// -_)/ __/                          
/_//_/ \\_,_/ \\__//_/\\_\\ \\__//_/                             
   ___     ____ __                     _____                
  / _ |   / __// /_ ___   ____ __ __  / ___/___ _ __ _  ___ 
 / __ |  _\\ \\ / __// _ \\ / __// // / / (_ // _ `//  ' \\/ -_)
/_/ |_| /___/ \\__/ \\___//_/   \\_, /  \\___/ \\_,_//_/_/_/\\__/ 
                             /___/                          ''')
print("\n" * 5)
enter()
#the above is just a debug statement
if True:
  print("\033[31m")
  fastwrite("WARNING: THIS WHOLE THING IS CREATED FOR A JOKE. SO YEAH.")
  print("\033[0m")
  enter()
  write("A TeamCoderz Production by "+"\033[32m"+"LiquidPixel101"+"\033[0m"+"...")
  time.sleep(2)
  clear()
  print("\033[32m")
  print('''                                        
                  /&&# 
                  
             .(&@@@@@@@@@%/   
             
       *@@&@@&###%%@@&%#((#&@@@@#.   
       
       .@@@@%&%.     ,,. *&%&@@@(   
       
      #@&#%%  #@@@@,@@@@@@* *&*/@@   
      
     (@&%&*.@@@/         &@%  @(*&@.  
   */@@%&# #@@@/         &@/   &,(@%(,  
   %@@@&@(   ,/.         &@@@. &#%@@@*  
     #@%#&  *@@/         &@@@.(#.%@*   
     
     .@@((@* (@@@@@@,%@@@@@* #/.#@/  
     
       #@%/@@( .#@@&      .&@%,@@,  
       
       #@@@@(**(%&%##%%&#*,,%@@@@*  
       
         ,  /&@@&%#&@%%%@@@#,  .  
         
                  ,@@&          
                  
                                        ''')
  print("\033[0m")
  time.sleep(1)
  clear()
  clear()
  write(
      "Inspired by Alpharumeric, TheFAA, Zygrade, and ColoredHue's Fly an Airplane! repl."
  )
  print("\n" * 5)
  write("Don't worry, the credits should show up only once.")
  print("The next time you run this project, this should NOT appear, as long as you don't press the 'stop' button in the middle of the game, as if you die the code will automatically stop.")
  #write("Speaking of dying (you will die both in real life and in the game of course but there's another thing)...")
  #print("The IS a checkpoint very far in-game. You'd be lucky if yo don't rage quit before you reach that checkpoint, but I'm telling you, THERE WILL BE A CHECKPOINT.")
  
  enter()
else:
  print("\033[0m")
  enter()
print("\033[31m")
write("Warning: Spelling errors will make you lose.\n")
print("\033[0m")
write("Before we start, what is your name?")
username=input(end="")
startime = time.time()
endtime = time.time()
startime=time.time()
user = intput("You are hired to be a"+"\033[32m"+" hacker"+"\033[0m"+". Do you accept?\n")
if no(user):
  endtime = time.time()
  write("You ran out of money and died.")
  time.sleep(1)
  print("\033[31m")
  slowwrite("Stupid.")
  endtime = time.time()
  os._exit(0)
die(user)
user = intput(
    "You will go to a "+"\033[34m"+"job interview"+"\033[0m"+". Would you like to take a "+"\033[33m"+"taxi?\n"+"\033[0m")
if no(user):
  endtime = time.time()
  write("You walk to the "+"\033[34m"+"job interview"+"\033[0m"+".\n")
  write(
      "You arrive late and the interviewer "+"\033[31m"+"rejects you"+"\033[0m"+". You run out of money. A couple of days later, you die"
  )
  enter()
  slowwrite("HINT:")
  write(
      "Use common sense at the beginning of the game, but furthur in-game, it's random; don't use common sense."
  )
  enter()
  endtime = time.time()
  os._exit(0)
die(user)
write("You have arrived on time.")
enter()
write("You get "+"\033[32m"+"hired"+"\033[0m"+". You will work from home.\n")
write("The next day, at home, you start "+"\033[24m"+"working."+"\033[0m"+"\n")
endtime = time.time()
startime=time.time()
user = intput(
    "Suddenly, you recieve an "+"\033[31m"+"email"+"\033[0m"+". Your most "+"\033[32m"+"wished"+"\033[0m"+" item is on "+"\033[32m"+"sale"+"\033[0m"+" for only this "+"\033[31m"+"hour"+"\033[0m"+"! Do you want stay at home?"
)
if yes(user):  #Stay home=die
  write("1 day later...")
  endtime = time.time()
  startime=time.time()
  user = intput(
      "You just need that item "+"\033[31m"+"badly"+"\033[0m"+". Do you want to "+"\033[34m"+"work?"+"\033[0m"+" Enter '"+"\033[32m"+"y"+"\033[0m"+"' for work, '"+"\033[31m"+"n"+"\033[0m"+"' for shopping\n"
  )
  die(user)
  if no(user):#if no, you die
    endtime = time.time()
    write("You go to the "+"\033[34m"+"shopping mall"+"\033[0m"+". You buy your "+"\033[32m"+"item"+"\033[0m"+".\n")
    write("You recieve a "+"\033[31m"+"message"+"\033[0m"+" on your "+"\033[34m"+"phone"+"\033[0m"+", from you "+"\033[31m"+"boss"+"\033[0m"+".\n")

    write("'"+"\033[31m"+"WHY AREN'T YOU WORKING? I PUNISH YOU TO EXTRA WORK TOMORROW!"+"\033[0m"+"\n'")
    enter()
    write("1 day later...\n")
    write("The extra work "+"\033[31m"+"tired"+"\033[0m"+" you out. Your boss "+"\033[31m"+"fires"+"\033[0m"+" you.\n")
    write(""+"\033[31m"+"You soon run out of money and food. You die. The end."+"\033[0m"+"\n")
    time.sleep(2)
    os._exit(0)
  if yes(user):  #If yes, you also die
    write("You work, despite that you "+"\033[31m"+"badly"+"\033[0m"+" wanted that item.\n")
    write("By "+"\033[33m"+"afternoon"+"\033[0m"+", you are still "+"\033[34m"+"working"+"\033[0m"+", but "+"\033[31m"+"anxiety"+"\033[0m"+" has taken you.\n")
    endtime = time.time()
    startime=time.time()
    user = intput(
        "Do you want to "+"\033[31m"+"force"+"\033[0m"+" yourself to keep working? Enter '"+"\033[32m"+"y"+"\033[0m"+"' for work, '"+"\033[31m"+"n"+"\033[0m"+"' for slump back and sleep\n"
    )
    die(user)
    if yes(user):  #if u work u die
      endtime = time.time()
      write(
          "You "+"\033[31m"+"force"+"\033[0m"+" yourself to "+"\033[34m"+"work"+"\033[0m"+". Before you end work, you get too "+"\033[31m"+"anxious and die"+"\033[0m"+". The end."
      )
      
      os._exit(0)
    elif no(user):  #if u dont work u also die
      endtime = time.time()
      write(""+"\033[31m"+"You slump over and sleep."+"\033[0m"+"\n")
      write(
          "When you "+"\033[33m"+"wake up"+"\033[0m"+", it's already the "+"\033[33m"+"next day"+"\033[0m"+". Your "+"\033[31m"+"boss"+"\033[0m"+" sent you a "+"\033[31m"+"message"+"\033[0m"+" on your phone."
      )
      print(""+"\033[31m"+"")
      write("WHY AREN'T YOU WORKING??\n")
      write("YOU ARE FIRED!\n")
      write(""+"\033[0m"+"Later, you run out of money and food and you "+"\033[31m"+"die"+"\033[0m"+". The end.")
      os._exit(0)
if user == "no, why would i?" or user == "no why would i?" or user == "no, why would i" or user == "No, why would I?" or user == "No, why would i?" or user == "No why would i" or user == "no why would i":
  write("Ermm...Because you don't wanna be fired??")
  print()
  print()
  time.sleep(1)
  write("lol, why are you waiting here")
  time.sleep(1)
  write("oh yeah, the game. sorry, I forgot about it.")
  time.sleep(3)
  write("Wait why are you here?")
  time.sleep(2)
  write(
      "Oh, the game! I forgot about it. Sorry! Continuing on with the game...")
else:
  die(user)
#this means that not yes and not not no so not not = yes so yeah
#ye good go to the shopping mall
write(
    "You leave a "+"\033[34m"+"message"+"\033[0m"+" to your "+"\033[31m"+"boss"+"\033[0m"+" that your not going to work for a while.\n"
)

write("You go to the shopping mall.")
enter()
write("The next day, you "+"\033[32m"+"still work"+"\033[0m"+".\n")
write("Apparently, your boss had "+"\033[32m"+"sympathy"+"\033[0m"+" for you and also "+"\033[32m"+"liked"+"\033[0m"+" that item.\n")
write(
    "Also, your boss "+"\033[32m"+"complimented"+"\033[0m"+" you about your "+"\033[34m"+"integrity"+"\033[0m"+" and gave you a raise."
)
enter()
write("The next day...")
time.sleep(1)
clear()
write("You are required to go to a meeting at work.\n")
endtime = time.time()
startime=time.time()
user = intput("DO YOU WANT TO GO??")
if no(user):
  endtime = time.time()
  startime=time.time()
  user = intput("Please state your reason:\n")
  write("That's ridiculous!\n")
  endtime = time.time()
  startime=time.time()
  letter = intput(
      "Please write an apology letter to your boss - It should be at least 100 words long.\n"
  )
  if (len(letter.split()) < 100):
    write("Your letter is less than 100 words.\n")
    enter()
    endtime = time.time()
    startime=time.time()
    letter = intput("Please rewrite your letter:\n")
    if (len(letter.split()) < 100):
      write("Your letter is still less than 100 words.\n")
      write("Meanwhile, your boss fires you.")
      enter()
      write(
          "A few days later, you run out of money and food. You die. The end.")
      endtime = time.time()
      os._exit(0)
    else:
      write("Letter sent  ✓")
      enter()
      write("You wait.....")
      clear()
      write("And wait...")
      clear()
      slowwrite("And wait...")
      enter()
      write("100 years later, you still wait...\n")
      write("Actually, you die. The end.")
      endtime = time.time()
      os._exit(0)
  else:
    write("Letter sent  ✓")
    enter()
    write("Your boss rejects your letter and fires you")
    write("You get so mad and sad that you suicide. The end.")
    endtime = time.time()
    os._exit(0)
die(user)
write("So you go.\n")
enter()
write("At the meeting, you meet your colleague.")
write(
    "You felt a waft of wind and see your colleague: Ethan the Evil! You are scared and call Arnold the Awesome to help."
)
enter()
if True:

  write(
      "BTW, Arnold the Awesome is some random tardigrade and Ethan the Evil is just a weird red sphere that can morph into different shapes. Arnold once defeated Ethan but Ethan the Evil just came back anyways.\n"
  )
  enter()
write(
    "Arnold to the rescue! Arnold the Tardigrade (a.k.a Arnold the Awesome) comes.\n"
)
write(
    "You watch, as they fight. Then, you see Arnold do a powerful bump on Ethan. You say 'Critical Hit!' in front of them."
)
enter()
write(
    "Ethan gets mad (Isn't he very mad already?!), and comes for you! Do you dodge or attack?"
)
endtime = time.time()
startime=time.time()
user = intput(" \nEnter 1 for attack, 2 for dodge!\n")
clear()
if yes(user):  #Ethan kills u
  write(
      "You try to attack, but Ethan is very skilled and can fly (He's technically god but not god) and he kills you. The end."
  )
  time.sleep(2)
  endtime = time.time()
  os._exit(0)
die(user)
write(
    "Ethan tries to attack you, but you dodge! 'Miss!' you shout. Ethan gets more angry (He can get infinetly angry) and comes for you! Do you dodge or attack?"
)
endtime = time.time()
startime=time.time()
user = intput("\nEnter 1 for attack, 2 for dodge!\n")
if no(user):
  write("Ethan knew you were going to dodge and kills you! The end.")
  time.sleep(2)
  endtime = time.time()
  os._exit(0)
die(user)
write("You try to attack, but Ethan is very skilled. You miss.")
enter()
write("Suddenly, Arnold uses his bump powers and bumps Ethan the Evil!\n")
write("Ethan the Evil falls.")
enter()
write("Startled, your boss calls 911.")
write("Police soon come, and arrests Arnold and charges him of murder.")
enter()
write(
    "Arnold the Awesome is going to be in jail, and you need to help him!!\n")
write("You need a car! You see a car nearby.")
endtime = time.time()
startime=time.time()
user = intput("Do you want to go to that car?")
if no(user):
  write("You stand in this place for the rest of your life, the end.")
  write("lol do you want to continue")
  input()

  write("whatever ur gonna die.")
  time.sleep(2)
  endtime = time.time()
  os._exit(0)
die(user)
write("You go to that car.")

write("Now what do you do?")
endtime = time.time()
startime=time.time()
user = intput("Enter 1 to break into the car\nEnter 2 to stand there\n")
if yes(user):
  write("You break into the car.")
  write("But then you see a comfortable looking pair of gloves beside you.")
  endtime = time.time()
  startime=time.time()
  user = intput("Do you want to wear it?")
  die(user)
  if yes(user):
    write("You wear the gloves:)")
  if no(user):
    write("You don't wear the gloves :(")
  write("You want to drive the car.")
  write(
      "Uh oh! You don't have the key to start the engine up and the alarm starts beeping!"
  )
  write(
      "The police come and you are sent to jail for the rest of your life. the end."
  )
  time.sleep(2)
  endtime = time.time()
  os._exit(0)
die(user)
write("You stand in this place.")
enter()
write("You wait...")
clear()
write("And wait...")
clear()
write("Until...")
enter()
write("You hear a 'Cling!' sound. It's the car key! ")
endtime = time.time()
startime=time.time()
user = intput("Do you want to steal the car?")
if no(user):
  write("The car's owner sees you with the car key and calls the police!")
  write(
      "The police come and you stay in jail for the rest of your life. You're a failure. The end."
  )
die(user)
write("You get into the car.")
write(
    "You see a comfortable looking pair of gloves with a weird metal thing on it beside you."
)
endtime = time.time()
startime=time.time()
user = intput("Do you want to wear it?")
die(user)
if yes(user):
  write("You wear the gloves.")
  gloves = 1
else:
  gloves = 0
enter()
write(
    "Anyways, you drive away and see a police car with Arnold the Awesome inside!"
)
endtime = time.time()
startime=time.time()
user = intput("Do you want to chase the police car?\n")
if no(user):
  write("Stoopid you couldn't do anything now.")
  write("A car crashes into you and you die.")
  time.sleep(2)
  endtime = time.time()
  os._exit(0)
if not no(user) and not yes(user):
  write("Congrats you found the Easter Egg!!!")
  easteregg = 1
  enter()
  write("idk, but it MIGHT be some use in the near future...")
  print("Actually trust me it's not, i tried but i gave up on this")
  write("but anyways continuing on with da game:")

write("You chase the police car to the police station.")
enter()
write("Do you want to:")
endtime = time.time()
startime=time.time()
user = intput(
    "Enter 1 to go right into the police station and get Arnold out\nEnter 2 to spy on Arnold and the police and see what they do\n"
)
if yes(user):
  write("You go right into the police station.")
  enter()
  write(
      "Suddenly, a woman runs into the police station and says that her car has been stolen."
  )
  write("Then, she points and you and says that you stole the car.")
  print("\n" * 5)
  write("You spent the rest of your life in jail. The end.")
  endtime = time.time()
  os._exit(0)
die(user)
write("You spy on Arnold without being seen.")
write(
    "Suddenly, a woman runs into the police station and says that her car is stolen."
)
write("She points at the car you just stole, and says that that's the car!")
endtime = time.time()
startime=time.time()
user = intput(
    "What do you do?\nEnter 1 to go to the police and confess\nEnter 2 to stay in hiding and hope for the best."
)
if yes(user):
  write(
      "You go confess to the police. Then you go to jail for the rest of your life. The end."
  )
  endtime = time.time()
  os._exit(0)
die(user)
write("You stay in hiding and hope for the best.")
write("You see the police go to the car and try to get in it.")
enter()
write("Since the key is on you, the police couldn't get in, so they break in.")
write("They do a test on the steering wheel.")
if gloves == 0:
  write("They discover your fingerprints on the steering wheel!")
  write("They do a investigation. They search for you.")
  print()
  write("They don't seem to know your name.")
  print()
  print("Wait you don't have a name, lol")
  time.sleep(2)
  write("So they name you Joe Mama.")
  enter()
  write("idk i ran out of ideas so anyhow you die after. the end.")
  endtime = time.time()
  os._exit(0)

write("The police discover nothing.")
write('Then, all of a sudden, the woman shouts:')
print('"MY GLOVES! MY GLOVES! MY $10 GLOVES! THEY ARE GONE! OH NO!!!!"')
time.sleep(1)
write("The police agree and they declare a Earth wide search for the gloves")
enter()
write("Do you:")
endtime = time.time()
startime=time.time()
user = intput("(1) Give up and suicide\n(2) Keep going and go hide somewhere\n")
if no(user):
  write("Oh, no! The police find you.\n")
  write("They sentence you to 10000 years in prison.\n")
  write("You stay in prison for the rest of your life. The end.")
die(user)
write("You give up.")
enter()
write("Just as you were about to suicide, the police find you!\n")
endtime = time.time()
startime=time.time()
user = intput("Do you:\n(1) Quickly hide your gloves\n(2) Don't do anything\n")
if no(user):
  write(
      "The police spot you with the gloves. You spent the rest of your life in jail. The end."
  )
  endtime = time.time()
  os._exit(0)
die(user)
write("You quickly hide your gloves.")
enter()
write("The police ask you what your name is.\nWhat is your name???")
input()
write("Whatever, you say that your name is " + username + ".")
write("They ask you your full birthday. What is it?\n")
input()
write("Whatever, you say you are born on:")
print(str(today.year) + ",", today.strftime("%B"), today.day - 2)
slowwrite("lol.")
enter()
write("The police release you.")
endtime = time.time()
startime=time.time()
user = intput("Where do you want to go now? (by the way, this question is a matter of life or death. You should go to only one of the places you've been before, not telling you which one.)")
if user.lower() not in ["home", "home.", "house", "house."]:
  write("This place doesn't exist.")
  write(
      "You stand here by the police station for the rest of your life. The end."
  )
  fastwrite(
      "MAYBE if you go back home you MIGHT survive, though it's not guaranteed. "
  )
  endtime = time.time()
  os._exit(0)
write("You go home.")
enter()
write("Oh no! You forgot about Arnold the Awesome!")
endtime = time.time()
startime=time.time()
user = intput("Do you care?\n")
die(user)
if yes(user):
  write("Since you care, do you want to go back to the police station?")
  user = intput()
  die(user)
  if yes(user):
    write("You go back to the police station, and you don't see Arnold!")
    endtime = time.time()
    startime=time.time()
    user = intput(
        "Do you:\n(1) Ask the police for Arnold's whereabouts\n(2) Search for him by yourself"
    )
    die(user)
    if yes(user):
      write(
          "You ask the police for Arnold's whereabouts, but the police ask you why."
      )
      enter()
      write(
          "You tell them about Arnold, but then they reject you and arrest you."
      )
      time.sleep(1)
      write("You stay in jail with Arnold for the rest of your life. The end.")
      endtime = time.time()
      os._exit(0)
    write("You search for Arnold for the rest of your life. The end.")
    time.sleep(2)
    endtime = time.time()
    os._exit(0)
  write("Then you don't truly care about him.")
  write(
      "You feel a waft of wind again and Ethan materializes in front of you!")
  endtime = time.time()
  startime=time.time()
  user = intput("Do you:\n(1) Call 911\n(2) Call Arnold the Awesome\n")
  die(user)
  if yes(user):
    write("You call 911.")
    enter()
    write("Ethan kills you before the Emergency Services come. The end.")
    endtime = time.time()
    os._exit(0)
  write("You call Arnold the Awesome to help.")
  enter()
  write(
      "Since you didn't truly care about Arnold, Arnold doesn't truly care about you."
  )
  write("Arnold doesn't come, and Ethan kills you. The end.")
  endtime = time.time()
  os._exit(0)
write("Whatever, you don't care about Arnold.")
enter()
write("Suddenly, your phone rings.\nDo you:")
endtime = time.time()
startime=time.time()
user = intput(
    "(1) Pick up the phone and see who's calling\n(2) Who cares, ignore the phone\n"
)
die(user)
if no(user):
  write("You don't pick up the phone.")
  enter()
  write("So basically, you just chose the wrong option so you will die.")
  write(
      "Here's what happened after: It was your boss calling and then your fired, so somehow you die after"
  )
  fastwrite("Suicide!")
  endtime = time.time()
  os._exit(0)
write("It's your boss calling!")
endtime = time.time()
startime=time.time()
user = intput("Do you:\n (1) Answer the phone\n (2) Decline the phone\n")
die(user)
if no(user):
  write("You don't answer the phone.")
  enter()
  write("So basically, you just chose the wrong option so you will die.")
  write(
      "Here's what happened after: It was your boss calling and then your fired, so somehow you die after, as expected."
  )
  fastwrite("Suicide!")
  endtime = time.time()
  os._exit(0)
write("Your boss asks that why you called a murderer (Arnold the Awesome) to murder one of his employees in a threatening voice!")
write("Your boss gives you a big, big warning so that if you call Arnold again he is going to fire you!")
endtime = time.time()
startime=time.time()
user=intput("Do you:\n (1) Hang up the phone \n(2) Explain to your boss that Arnold isn't a murderer and that Ethan almost killed you")
die(user)
if no(user):
  write("Your boss disagrees. The next thing that comes out of his mouth is: You're fired!")
  enter()
  print("SIDENOTE: DON'T QUIT NOW, THIS IS THE RIGHT OPTION.")
  
if yes(user):
  write("You hang up the phone.")
  enter()
  write("A few minutes later, you hear an android notification sound from your iPhone for some reason.")
  endtime = time.time()
  startime=time.time()
  user=intput("Do you check it?")
  if yes(user):
    write("It's your boss! Your boss sent you a message!")
    write("Oh no! Your boss says that you're fired!")
    write("You regret so much hanging up the phone that you suicide! The end.")
    endtime = time.time()
    os._exit(0)
  write("You ignore your phone.")
  enter()
  write("It's the next day!")
  write("Do you go to work like usual?")
  user=intput("")
  die(user)
  if (yes(user)):
    write("You go to work like usual. At your office, your boss does the angry face to you.")
    write("You don't know why.")
    enter()
    write("Suddenly, you feel a gust of wind and a sear of pain in your neck!")
    write("ETHAN THE EVIL BEHEADED YOU!")
    write("You die.")
    endtime = time.time()
    os._exit(0)
  enter()
  write("You hear a knock on the door. Do you open it?")
  user=intput("")
  if no(user):
    write("You get a break in!")
    enter()
    write("FBI open up! The FBI, with guns, arrest you. Do you ask why you are arrested?")
    user=intput("")
    die(user)
    if (no(user)):
      write("They take you to jail, where you stay there for the rest of your life, and you don't know why you got arrested.")
      endtime = time.time()
      os._exit(0)
    write("They tell you that you are arrested because you are arrested. ")
    enter()
    write("They force you into jail, where you stay for the rest of your life. The end.")
    endtime = time.time()
    os._exit(0)
  write("You open the door, and you see your boss!")
  write("Your boss tells you that your fired!")
  enter()
  write("You slam the door shut as you are so angry, and your boss goes away after a while.")
  print("SIDENOTE: YOU'VE DONE THE RIGHT OPTION")
print("\033[034m")
write("Hooray!! You've reached a checkpoint!")
print("\033[0m")
def afire():
  global startime
  endtime = time.time()
  startime=time.time()
  enter()
  write("Loading Checkpoint...")
  enter()
  write("It's the next day...")
  enter()
  user= intput("Do you look for a new job?")
  die1(user)
  if no(user):
    write("lol then what do you do?")
    input()
    write("nah. I think you expect what is going to happen. Right?")
    input()
    write("So, anyways, you run out of money and "+"\033[31m"+"die"+"\033[0m"+" lol obviously.")
    write("OH WAIT THERE WAS A CHECKPOINT")
    enter()
    afire()
  write("Just in time, another hacker job offer just came up!")
  user =intput("Do you accept?")
  endtime = time.time()
  startime=time.time()
  die1(user)
  if no(user):
    enter()
    write("The correct answer is basically the answer to the first question, so you know whats gonna happen.")
    write("YOU RUN OUT OF MONEY AND DIE!!!")
    
    afire()
  write("You accept the job offer.")
  enter()
  write("Somebody is loudly banging on your door. ")
  user=intput("Do you open it?")
  die1(user)
  endtime = time.time()
  startime=time.time()
  if no(user):
    write("Outside, you hear them talking loudly. \" POLICE! OPEN THE DOOR!\"")
    write("Then suddenly, with a loud BOOM, they break the door and come in.")
    write("They point their guns at you.")
  if yes(user):
    write("You open the door. It's the police!")
    write("They come in and point their guns at you.")
    enter()
  write("They tell you to put your hands up!")
  user=intput("Do you do that?")
  die1(user)
  endtime = time.time()
  startime=time.time()
  if no(user):
    write("They shoot you and you die. The end.")
    afire()
  write("They put handcuffs on you and bring you to their car.")
  enter()
  write("They tell you that the metal thing on the glove was a tracking device.")
  write("The police search your house while you are locked in the car.")
  enter()
  write("Later that day...")
  enter()
  write("They have interviewed you and put you in a small cell.")
  write("They said that you were to stay there until you court hearing, which for some reason will happen.")
  user=intput("Do you try to escape?")
  die1(user)
  endtime = time.time()
  startime=time.time()
  if yes(user):
    write("You see a small vent in your cell.")
    user=intput("Do you try to climb into it and possibly escape?")
    die1(user)
    if yes(user):
      write("While you climb into the vent, a guard catches you!")
      write("They have very harsh punishments for escaping.")
      death=["executed by lethal injection.","burned at stake.", "shot.", "beheaded.", "boiled alive.", "crucified.", "cut apart by chainsaws.", "hanged.", "whipped to death.", "hit to death.", "electrocuted.", "gassed.", "crushed by an elephant deliberately.", "drowned to death deliberately.", "thrown off a cliff.","stabbed to death.","left in a locked room forever with no food/water.","thrown into a crusher that crushes your whole body into powder.","buried alive.","mauled by a bear.", "eaten by a cougar."]
      print("\033[31m")
      write("You are "+death[random.randint(0,20)])
      print("\033[0m")
      afire()
  write("You stay there for the night.")
  enter()
  
afire()
  
print("TO BE CONTINUED")
print("==============>")
endtime = time.time()
timetaken = round(endtime - startime, 2)
print("You took " + str(timetaken) + " seconds to complete this game.")
