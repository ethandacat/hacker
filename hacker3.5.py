# HACKER 3.5: The Mystery Dust Conspiracy by ethandacat
# P.S. Hacker 4 coming probably soon!
# ty all

import time
import random
import sys
import os

score = 0

def slow(t, end=True):
    write(t, end, 0.2)

def fast(t, end=True):
    write(t, end, 0.02)

def write(t, end=True, inte=0.04):
    end = bool(end)
    t = "\033[32m".join(t.split("[!green]"))
    t = "\033[34m".join(t.split("[!blue]"))
    t = "\033[31m".join(t.split("[!red]"))
    t = "\033[35m".join(t.split("[!purple]"))
    t = "\033[33m".join(t.split("[!yellow]"))
    t = "\033[36m".join(t.split("[!cyan]"))
    t = "\033[0m".join(t.split("[!]"))
    for i in t:
        print(i, end='', flush=True)
        time.sleep(inte)
    if end:
        print("")

def die():
    global score
    enter()
    write("You [!red]died[!].")
    enter()
    write(
        """
[!red]
 __  __     ______     ______     __  __     ______     ______       
/\\ \\_\\ \\   /\\  __ \\   /\\  ___\\   /\\ \\/ /    /\\  ___\\   /\\  == \\      
\\ \\  __ \\  \\ \\  __ \\  \\ \\ \\____  \\ \\  _"-.  \\ \\  __\\   \\ \\  __<      
 \\ \\_\\ \\_\\  \\ \\_\\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\    
  \\/_/\\/_/   \\/_/\\/_/   \\/_____/   \\/_/\\/_/   \\/_____/   \\/_/ /_/    
                                                            3.5
                                                            
                                                          YOU DIED
[!]

    """
    ,inte=0.001)
    sys.exit()

def enter():
    write("Press [!green]Enter[!] to continue...")
    input()
    clear()

def clear():
    print("\033[H\033[J", end='')

def get_input():
    return input().lower().strip()

def num(max_num, min_num=1):
    while True:
        try:
            choice = int(input(f"Choose ({min_num}-{max_num}): "))
            if min_num <= choice <= max_num:
                return choice
            else:
                write(f"[!red]Invalid choice! Please choose between {min_num} and {max_num}.[!]")
        except ValueError:
            write("[!red]Please enter a valid number![!]")

# Title Screen
clear()
write("""


[!blue] __  __     ______     ______     __  __     ______     ______       
/\\ \\_\\ \\   /\\  __ \\   /\\  ___\\   /\\ \\/ /    /\\  ___\\   /\\  == \\      
\\ \\  __ \\  \\ \\  __ \\  \\ \\ \\____  \\ \\  _"-.  \\ \\  __\\   \\ \\  __<      
 \\ \\_\\ \\_\\  \\ \\_\\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\    
  \\/_/\\/_/   \\/_/\\/_/   \\/_____/   \\/_/\\/_/   \\/_____/   \\/_/ /_/    
                                                        3.5[!]

[!purple]The Mystery Dust Conspiracy[!]

""",inte=0.001)
enter()

write("Check out [!blue]Hacker 1, 2, and 3[!] by me and [!green]Hacker- a Story Game[!] by LiquidPixel101.")
enter()

# Main Story Begins
write("[!red]WARNING[!]: [!blue]Wrong choices[!] will result in [!red]death[!] by the [!green]Costco Police Force[!], [!purple]Mystery Dust Entities[!], or other [!cyan]interdimensional forces[!].")
enter()

# Chapter 1: The Aftermath of Mystery Dust
write("After the [!purple]Great Mystery Dust Incident[!] of Hacker 3, reality has become... [!cyan]complicated[!].")
write("You wake up in what [!red]appears[!] to be your bedroom, but something is [!blue]fundamentally wrong[!].")
write("Your [!green]ceiling[!] is [!purple]purple[!] and covered in [!yellow]glittering equations[!].")
write("The [!blue]equations[!] are [!red]moving[!] and [!green]rearranging themselves[!] into new patterns.")
write("Your [!cyan]alarm clock[!] is [!purple]floating[!] and displaying [!red]impossible times[!] like '25:73 o'clock'.")
write("Outside your window, you see [!blue]normal people[!] going about their day, but they're all [!green]slightly transparent[!].")
write("Some of them are [!red]walking backwards[!] while [!purple]talking forwards[!].")
write("Your [!yellow]coffee mug[!] from yesterday is still [!cyan]phasing in and out of existence[!].")
write("Every few seconds it [!red]flickers[!] between [!blue]solid[!], [!green]holographic[!], and [!purple]made of pure mathematics[!].")
enter()

write("Suddenly, your [!green]computer[!] boots up by itself.")
write("The screen displays a [!blue]familiar message[!]:")
slow("'[!purple]CONGRATULATIONS, HACKER. YOU HAVE SUCCESSFULLY BROKEN REALITY.[!]'")
write("'[!cyan]THE MYSTERY DUST HAS INFECTED THE QUANTUM SUBSTRATE OF EXISTENCE.[!]'")
write("'[!red]IVAN ZONG AND THE RESISTANCE NEED YOUR HELP.[!]'")
write("'[!yellow]THE FBI HAS DISCOVERED THE DUST AND IS TRYING TO WEAPONIZE IT.[!]'")
write("'[!green]ARNOLD THE AWESOME HAS ESCAPED FROM PRISON USING MYSTERY DUST POWERS.[!]'")
write("'[!blue]REALITY IS NOW 47% DUST, 23% MYSTERY, AND 30% PURE CHAOS.[!]'")
enter()

write("What do you do?")
write("1. [!green]Check the news to see if anyone else notices reality is broken[!]")
write("2. [!blue]Try to contact Ivan Zong through the resistance network[!]")
write("3. [!red]Attempt to reverse the Mystery Dust effects[!]")
write("4. [!purple]Embrace the chaos and become one with the Mystery Dust[!]")

choice = num(4)

if choice == 1:
    clear()
    write("You turn on the [!blue]news[!] to see what's happening in the world.")
    write("The [!green]news anchor[!] appears to be [!red]completely normal[!], which is [!purple]suspicious[!].")
    write("She says: '[!cyan]Good morning! Today's weather is partly cloudy with a chance of existential dread.[!]'")
    write("'[!yellow]In other news, local man claims his sandwich spoke to him in binary code.[!]'")
    write("'[!blue]Scientists are baffled by reports of floating furniture and mathematical ceilings.[!]'")
    write("'[!green]The government denies any involvement in what they call 'Tuesday'.[!]'")
    write("Suddenly, the [!red]news anchor[!] looks directly at you through the screen.")
    write("'[!purple]We know you're watching, hacker. The dust remembers everything.[!]'")
    write("Your [!cyan]TV[!] starts [!yellow]leaking[!] [!purple]glittery dust[!] onto your floor.")
    write("The dust [!red]spells out[!] '[!green]FIND THE SOURCE[!]' before [!blue]evaporating[!].")
    
elif choice == 2:
    clear()
    write("You attempt to [!blue]contact Ivan Zong[!] through the old resistance channels.")
    write("You type the [!green]secret code[!] into your computer: '[!cyan]CatsAreDigital2024[!]'")
    write("The screen [!purple]flickers[!] and shows a [!red]distorted video feed[!].")
    write("Ivan Zong appears, but he's [!yellow]partially made of Mystery Dust[!].")
    write("His [!blue]left arm[!] is [!green]pure mathematics[!] and his [!red]right eye[!] is a [!purple]swirling galaxy[!].")
    slow("'[!cyan]Hacker! Thank the digital gods you're alive![!]'")
    write("'[!yellow]The Mystery Dust has given me incredible powers, but at a cost.[!]'")
    write("'[!red]I can see through dimensions now, but I can't eat solid food anymore.[!]'")
    write("'[!green]Everything tastes like quantum uncertainty and regret.[!]'")
    write("'[!blue]The FBI has built a Mystery Dust weapon. We need to stop them![!]'")
    write("'[!purple]Meet me at the old Costco. The one that exists in seven dimensions simultaneously.[!]'")
    
elif choice == 3:
    clear()
    write("You decide to [!red]reverse[!] the Mystery Dust effects.")
    write("You open your [!green]computer[!] and start typing [!blue]anti-dust code[!].")
    write("```")
    write("[!cyan]if (mysteryDust == true) {[!]")
    write("[!cyan]    mysteryDust = false;[!]")
    write("[!cyan]    reality.restore();[!]")
    write("[!cyan]}[!]")
    write("```")
    write("As soon as you hit [!yellow]Enter[!], your computer [!red]screams[!].")
    write("Not metaphorically. It [!purple]literally screams[!] like a [!blue]digital banshee[!].")
    write("The [!green]Mystery Dust[!] in your room [!red]becomes angry[!] and starts [!cyan]swirling violently[!].")
    write("It forms [!purple]tiny dust tornadoes[!] that [!yellow]spell out curse words[!] in [!blue]ancient languages[!].")
    write("Your [!red]ceiling equations[!] start [!green]solving themselves[!] and the answers are all [!purple]'NO'[!].")
    write("The dust [!cyan]whispers[!]: '[!red]You cannot undo what has been dusted![!]'")
    write("Your [!blue]computer[!] [!yellow]explodes[!] into [!purple]mathematical fragments[!].")
    write("The [!green]Costco Police Force[!] arrives and arrests you for [!red]attempted reality vandalism[!].")
    die()
    
elif choice == 4:
    clear()
    write("You decide to [!purple]embrace[!] the [!cyan]Mystery Dust[!] and become one with the chaos.")
    write("You [!green]open your arms[!] and [!blue]breathe deeply[!].")
    write("The [!yellow]glittery dust[!] in your room [!red]swirls around you[!] like a [!purple]magical tornado[!].")
    write("You feel your [!cyan]consciousness[!] [!green]expanding[!] across [!blue]multiple dimensions[!].")
    write("Suddenly, you can [!red]see[!] the [!yellow]true nature[!] of reality.")
    write("Everything is [!purple]connected[!] by [!cyan]threads of Mystery Dust[!].")
    write("You see [!green]Ivan Zong[!] in his [!blue]seven-dimensional Costco[!].")
    write("You see [!red]Arnold the Awesome[!] [!yellow]surfing[!] on [!purple]waves of pure mathematics[!].")
    write("You see the [!cyan]FBI[!] building their [!red]Mystery Dust weapon[!] in a [!green]secret facility[!].")
    write("But most importantly, you see the [!blue]source[!] of all the Mystery Dust.")
    write("It's a [!purple]giant interdimensional cat[!] that's [!yellow]sneezing[!] [!cyan]cosmic dust[!] into reality.")
    write("The cat [!red]notices[!] you looking and [!green]winks[!].")
    slow("'[!blue]Meow. Finally, someone who gets it.[!]'")

enter()

# Chapter 2: The Interdimensional Cat
write("The [!purple]giant interdimensional cat[!] speaks to you through [!cyan]dust telepathy[!].")
write("'[!green]I am Whiskers the Infinite, Guardian of the Mystery Dust Realm.[!]'")
write("'[!blue]I've been sneezing cosmic dust into your reality for eons.[!]'")
write("'[!red]It's not my fault! I'm allergic to linear time![!]'")
write("'[!yellow]The FBI wants to use my dust to control reality itself.[!]'")
write("'[!purple]But the dust cannot be controlled, only embraced.[!]'")
write("'[!cyan]You must choose, young hacker. Will you help me stop the FBI?[!]'")
enter()

write("Whiskers shows you [!green]three possible paths[!] through the [!blue]dust dimensions[!]:")
write("1. [!red]Infiltrate the FBI facility and destroy their Mystery Dust weapon[!]")
write("2. [!yellow]Rally the resistance and launch a full-scale assault[!]")
write("3. [!purple]Try to negotiate with the FBI and explain the true nature of Mystery Dust[!]")
write("4. [!cyan]Ask Whiskers to just stop sneezing[!]")

choice = num(4)

if choice == 1:
    clear()
    write("You choose to [!red]infiltrate[!] the FBI facility.")
    write("Whiskers [!purple]nods approvingly[!] and [!cyan]sneezes[!] you into a [!green]dust portal[!].")
    write("You emerge in a [!blue]high-tech facility[!] filled with [!yellow]scientists in hazmat suits[!].")
    write("They're [!red]studying[!] [!purple]Mystery Dust[!] in [!cyan]containment chambers[!].")
    write("You see a [!green]massive weapon[!] that looks like a [!blue]dust-powered laser cannon[!].")
    write("A [!yellow]scientist[!] notices you and shouts: '[!red]INTRUDER! ACTIVATE THE DUST DEFENSES![!]'")
    write("Suddenly, [!purple]weaponized Mystery Dust[!] starts [!cyan]attacking[!] you.")
    write("But since you're [!green]one with the dust[!], it [!blue]recognizes[!] you as [!yellow]family[!].")
    write("The [!red]attack dust[!] [!purple]hugs[!] you instead of [!cyan]disintegrating[!] you.")
    write("The scientists are [!green]confused[!] and [!blue]slightly jealous[!].")
    
elif choice == 2:
    clear()
    write("You decide to [!yellow]rally the resistance[!] for a [!red]full-scale assault[!].")
    write("Whiskers [!purple]teleports[!] you to the [!cyan]seven-dimensional Costco[!].")
    write("You find [!green]Ivan Zong[!] and [!blue]Arnold the Awesome[!] planning their next move.")
    write("Arnold is now [!red]50% Mystery Dust[!] and can [!yellow]phase through walls[!].")
    write("Ivan has [!purple]mathematical superpowers[!] and can [!cyan]calculate the probability of anything[!].")
    write("'[!green]Hacker![!]' Arnold shouts. '[!blue]Perfect timing! We're about to storm the FBI facility![!]'")
    write("'[!red]I've calculated a 73.6% chance of success,[!]' Ivan adds, '[!yellow]and a 26.4% chance of everyone turning into dust bunnies.[!]'")
    write("'[!purple]Those are pretty good odds![!]' Arnold says cheerfully.")
    write("You join their [!cyan]resistance army[!] of [!green]dust-powered rebels[!].")
    
elif choice == 3:
    clear()
    write("You choose to [!purple]negotiate[!] with the FBI.")
    write("Whiskers [!cyan]sighs[!] and says, '[!green]Diplomacy? How boringly three-dimensional.[!]'")
    write("But he [!blue]teleports[!] you to the [!red]FBI headquarters[!] anyway.")
    write("You walk into the [!yellow]main lobby[!] and approach the [!purple]receptionist[!].")
    write("'[!cyan]Hi, I'd like to speak to whoever is in charge of the Mystery Dust project.[!]'")
    write("The receptionist [!green]stares[!] at you for a moment, then [!blue]presses a big red button[!].")
    write("[!red]Alarms[!] start [!yellow]blaring[!] and [!purple]FBI agents[!] surround you.")
    write("'[!cyan]MYSTERY DUST ENTITY DETECTED![!]' they shout.")
    write("'[!green]INITIATE CONTAINMENT PROTOCOL![!]'")
    write("They [!blue]spray[!] you with [!red]anti-dust spray[!], but it just makes you [!purple]sparkle more[!].")
    write("'[!yellow]Wait![!]' you shout. '[!cyan]I just want to talk![!]'")
    write("The agents [!green]pause[!], [!blue]confused[!] by your [!red]reasonable request[!].")
    
elif choice == 4:
    clear()
    write("You ask Whiskers to [!cyan]just stop sneezing[!].")
    write("Whiskers [!purple]looks at you[!] with [!green]infinite sadness[!].")
    write("'[!blue]Oh, sweet summer hacker,[!]' he says, '[!red]you don't understand.[!]'")
    write("'[!yellow]I am not sneezing by choice. I am allergic to the fundamental nature of reality.[!]'")
    write("'[!purple]Every time someone makes a logical decision, I sneeze.[!]'")
    write("'[!cyan]Every time someone follows the laws of physics, I sneeze.[!]'")
    write("'[!green]Every time someone says 'that's impossible,' I sneeze.[!]'")
    write("'[!red]Your reality is so aggressively sensible that I cannot stop sneezing![!]'")
    write("As if to [!blue]prove his point[!], Whiskers [!yellow]sneezes[!] again.")
    write("This time, the [!purple]Mystery Dust[!] [!cyan]transforms[!] your [!green]shoes[!] into [!red]tiny helicopters[!].")
    write("They [!blue]start flying around[!] your feet, [!yellow]making helicopter noises[!].")
    write("'[!purple]See?[!]' Whiskers says. '[!cyan]This is my life now.[!]'")

enter()

# Chapter 3: The Final Confrontation
write("Regardless of your [!green]previous choice[!], all paths [!blue]converge[!] at the [!red]FBI facility[!].")
write("You find yourself [!purple]standing[!] before the [!cyan]Mystery Dust Weapon[!].")
write("It's a [!yellow]massive device[!] that looks like a [!green]cross[!] between a [!blue]particle accelerator[!] and a [!red]disco ball[!].")
write("The [!purple]FBI Director[!] emerges from the shadows.")
write("'[!cyan]So, you're the hacker who broke reality,[!]' she says.")
write("'[!green]I'm Director Sarah Dustbane, and I've been hunting Mystery Dust entities for years.[!]'")
write("'[!blue]This weapon will allow us to control the dust and restore order to the universe![!]'")
write("'[!red]No more floating furniture! No more mathematical ceilings! No more talking sandwiches![!]'")
write("'[!yellow]Just pure, boring, predictable reality![!]'")
enter()

write("Suddenly, [!purple]Ivan Zong[!] and [!green]Arnold the Awesome[!] burst through the wall!")
write("'[!blue]Not so fast, Dustbane![!]' Arnold shouts, [!red]surfing[!] on a [!cyan]wave of pure mathematics[!].")
write("'[!yellow]The Mystery Dust is not meant to be controlled![!]' Ivan adds, [!purple]calculating[!] the [!green]trajectory[!] of his [!blue]dust-powered laser eyes[!].")
write("Director Dustbane [!red]laughs[!] and [!cyan]activates[!] the weapon.")
write("'[!green]Too late! The Mystery Dust Neutralizer is charging up![!]'")
write("The weapon [!blue]hums[!] with [!purple]ominous energy[!] and starts [!yellow]sucking in[!] all the [!cyan]Mystery Dust[!] in the area.")
write("You feel your [!red]dust powers[!] being [!green]drained away[!].")
enter()

write("What do you do in this [!red]final moment[!]?")
write("1. [!green]Try to overload the weapon with too much Mystery Dust[!]")
write("2. [!blue]Call upon Whiskers the Infinite for help[!]")
write("3. [!purple]Attempt to reason with Director Dustbane[!]")
write("4. [!yellow]Embrace the chaos and let whatever happens happen[!]")

choice = num(4)

if choice == 1:
    clear()
    write("You [!green]concentrate[!] all your [!purple]Mystery Dust energy[!] and [!red]channel[!] it into the weapon.")
    write("'[!blue]If you want dust,[!]' you shout, '[!cyan]I'll give you ALL THE DUST![!]'")
    write("You [!yellow]overload[!] the weapon with [!purple]pure concentrated mystery[!].")
    write("The machine [!red]starts sparking[!] and [!green]making concerning noises[!].")
    write("'[!blue]ERROR: TOO MUCH MYSTERY DETECTED,[!]' the computer announces.")
    write("'[!cyan]MYSTERY LEVELS EXCEEDING MAXIMUM DUSTINESS.[!]'")
    write("'[!yellow]INITIATING EMERGENCY SPARKLE PROTOCOL.[!]'")
    write("The weapon [!purple]explodes[!] in a [!green]shower of glitter[!] and [!blue]mathematical equations[!].")
    write("Director Dustbane is [!red]covered[!] in [!cyan]Mystery Dust[!] and starts [!yellow]floating[!].")
    write("'[!purple]This is not what I wanted![!]' she cries as she [!green]phases through the ceiling[!].")
    
elif choice == 2:
    clear()
    write("You [!blue]call out[!] to [!purple]Whiskers the Infinite[!].")
    write("'[!green]Whiskers! We need your help![!]'")
    write("Suddenly, a [!cyan]massive interdimensional sneeze[!] echoes through the facility.")
    write("Whiskers [!yellow]materializes[!] in the room, [!red]the size of a small building[!].")
    write("'[!purple]Did someone say they needed help with dust control?[!]' he asks.")
    write("Director Dustbane [!green]stares[!] in [!blue]shock[!]. '[!red]A giant cosmic cat?![!]'")
    write("'[!cyan]That's MISTER Giant Cosmic Cat to you,[!]' Whiskers replies [!yellow]indignantly[!].")
    write("He [!purple]sneezes[!] directly at the weapon, [!green]transforming[!] it into a [!blue]giant ball of yarn[!].")
    write("'[!red]There,[!]' he says. '[!cyan]Much better. Now it's useful.[!]'")
    write("Director Dustbane [!yellow]faints[!] from [!purple]existential overload[!].")
    
elif choice == 3:
    clear()
    write("You [!purple]step forward[!] and [!green]address[!] Director Dustbane.")
    write("'[!blue]Director, you don't understand what you're dealing with.[!]'")
    write("'[!cyan]The Mystery Dust isn't a threat - it's evolution![!]'")
    write("'[!yellow]Reality was getting boring. The dust makes things interesting![!]'")
    write("'[!red]Don't you want to live in a world where your coffee mug might spontaneously become sentient?[!]'")
    write("Director Dustbane [!green]pauses[!], [!blue]considering[!] your words.")
    write("'[!purple]You know what?[!]' she says slowly. '[!cyan]My life HAS been pretty dull lately.[!]'")
    write("'[!yellow]And I did always wonder what it would be like to have a conversation with my furniture.[!]'")
    write("She [!red]turns off[!] the weapon and [!green]smiles[!].")
    write("'[!blue]Maybe a little mystery in life isn't so bad after all.[!]'")
    
elif choice == 4:
    clear()
    write("You [!yellow]shrug[!] and [!purple]embrace[!] the [!cyan]chaos[!].")
    write("'[!green]You know what?[!]' you say. '[!blue]Let's see what happens.[!]'")
    write("You [!red]sit down[!] on the floor and [!yellow]start eating popcorn[!] that [!purple]materializes[!] from nowhere.")
    write("Everyone [!green]stares[!] at you in [!blue]confusion[!].")
    write("'[!cyan]Are you... are you just going to watch?[!]' Director Dustbane asks.")
    write("'[!red]Yep,[!]' you reply, [!yellow]munching[!] on [!purple]interdimensional popcorn[!].")
    write("The [!green]absurdity[!] of the situation causes [!blue]reality[!] to [!cyan]hiccup[!].")
    write("The weapon [!purple]transforms[!] into a [!yellow]popcorn machine[!].")
    write("Everyone [!red]starts laughing[!] and [!green]sharing popcorn[!].")
    write("'[!blue]You know what?[!]' Director Dustbane says. '[!cyan]This is nice.[!]'")

enter()

# Epilogue
write("[!purple]Six months later...[!]")
enter()

write("Reality has [!green]settled[!] into a [!blue]new normal[!].")
write("The [!cyan]Mystery Dust[!] is now [!yellow]part of everyday life[!].")
write("People [!red]commute[!] to work on [!purple]flying carpets[!] made of [!green]crystallized mathematics[!].")
write("The [!blue]weather forecast[!] includes [!cyan]chances of spontaneous poetry[!] and [!yellow]probability storms[!].")
write("Director Dustbane [!purple]retired[!] and now [!green]runs[!] a [!red]interdimensional coffee shop[!].")
write("Her [!blue]specialty[!] is [!cyan]coffee[!] that [!yellow]tastes like your favorite memory[!].")
write("Ivan Zong [!green]became[!] the [!purple]Minister of Impossible Things[!] in the new government.")
write("Arnold the Awesome [!blue]started[!] a [!red]Mystery Dust surfing school[!].")
write("Whiskers the Infinite [!cyan]finally[!] found [!yellow]allergy medication[!] that works on [!purple]cosmic scale[!].")
write("He [!green]only sneezes[!] [!blue]recreationally[!] now.")
enter()

write("As for you, the [!red]legendary hacker[!]...")
write("You [!green]opened[!] a [!blue]small shop[!] that [!purple]sells[!] [!cyan]impossible things[!].")
write("Your [!yellow]bestsellers[!] include:")
write("- [!red]Bottled laughter[!] from [!green]interdimensional comedians[!]")
write("- [!blue]Solid music[!] that you can [!purple]sculpt[!] into [!cyan]furniture[!]")
write("- [!yellow]Time loops[!] for people who want to [!red]relive[!] their [!green]favorite moments[!]")
write("- [!purple]Quantum uncertainty[!] for [!blue]spicing up[!] [!cyan]boring conversations[!]")
enter()

write("One day, while [!green]organizing[!] your [!blue]inventory[!] of [!purple]crystallized dreams[!], you notice something [!red]strange[!].")
write("A [!cyan]new type[!] of [!yellow]dust[!] is [!green]appearing[!] in your shop.")
write("This dust is [!blue]different[!] - it [!purple]sparkles[!] with [!red]binary code[!] and [!cyan]smells like[!] [!yellow]fresh possibilities[!].")
write("You [!green]examine[!] it closely and realize...")
write("It's [!red]Digital Dust[!] - the [!blue]next evolution[!] of [!purple]Mystery Dust[!].")
write("This dust doesn't just [!cyan]change reality[!] - it [!yellow]programs[!] it.")
enter()

write("Your [!green]computer[!] [!blue]boots up[!] and displays a [!purple]familiar message[!]:")
slow("'[!cyan]CONGRATULATIONS, HACKER. REALITY.EXE HAS BEEN SUCCESSFULLY UPDATED.[!]'")
write("'[!yellow]NEW FEATURES INCLUDE: PROGRAMMABLE PHYSICS, CUSTOMIZABLE LOGIC, AND PREMIUM CHAOS MODES.[!]'")
write("'[!red]WOULD YOU LIKE TO INSTALL THE DIGITAL DUST EXPANSION PACK?[!]'")
write("'[!green]WARNING: MAY CAUSE EXISTENTIAL DEBUGGING AND RECURSIVE REALITY LOOPS.[!]'")
enter()

write("You [!blue]look[!] at the [!purple]Digital Dust[!], then at your [!green]computer[!], then at the [!cyan]impossible world[!] outside your window.")
write("A [!yellow]flying car[!] [!red]honks[!] its [!purple]musical horn[!] as it [!blue]drives[!] past your [!green]floating shop[!].")
write("A [!cyan]customer[!] walks in - they appear to be [!red]made entirely[!] of [!yellow]living equations[!].")
write("'[!purple]Excuse me,[!]' they say, '[!blue]do you sell any dust that can help me solve for X when X is the meaning of life?[!]'")
enter()

write("You [!green]smile[!] and [!blue]reach[!] for the [!purple]Digital Dust[!].")
write("'[!cyan]Actually,[!]' you say, '[!yellow]I think I have exactly what you need.[!]'")
write("'[!red]But first, let me ask you something...[!]'")
write("'[!green]Have you ever wondered what would happen if reality had a programming language?[!]'")
enter()

write("The [!purple]equation customer[!] [!blue]tilts[!] their [!cyan]mathematical head[!].")
write("'[!yellow]That sounds dangerous,[!]' they say.")
write("'[!red]And fascinating,[!]' they add.")
write("'[!green]And probably inevitable,[!]' they conclude.")
enter()

write("You [!blue]nod[!] and [!purple]sprinkle[!] some [!cyan]Digital Dust[!] into the air.")
write("The dust [!yellow]forms[!] [!red]glowing code[!] that [!green]reads[!]:")
write("[!cyan]if (reality == boring) {[!]")
write("[!cyan]    reality = awesome();[!]")
write("[!cyan]    mystery.level = maximum;[!]")
write("[!cyan]    chaos.enable(true);[!]")
write("[!cyan]}[!]")
enter()

write("The [!purple]code[!] [!blue]executes[!], and suddenly your [!green]shop[!] [!red]transforms[!] into a [!cyan]interdimensional programming interface[!].")
write("Your [!yellow]shelves[!] are now [!purple]filled[!] with [!blue]code libraries[!] for [!red]reality modification[!].")
write("The [!green]equation customer[!] [!cyan]gasps[!] in [!yellow]mathematical delight[!].")
write("'[!purple]This is it![!]' they exclaim. '[!blue]This is the future![!]'")
enter()

write("And so begins [!red]the next chapter[!] of your [!green]impossible adventures[!]...")
write("But that, dear [!blue]player[!], is a [!purple]story[!] for [!cyan]another day[!].")
write("Or [!yellow]another dimension[!].")
write("Or [!red]another programming language[!].")
write("The [!green]possibilities[!] are [!blue]literally[!] [!purple]infinite[!].")
enter()

write("[!cyan]THE END[!]")
write("[!yellow]OR IS IT?[!]")
write("[!red]PROBABLY NOT[!]")
write("[!green]NOTHING EVER REALLY ENDS[!]")
write("[!blue]ESPECIALLY NOT IN A REALITY WHERE DUST CAN PROGRAM ITSELF[!]")
write("[!purple]TO BE CONTINUED IN HACKER 5: THE DIGITAL DUST CHRONICLES[!]")
write("[!cyan]COMING SOON TO A DIMENSION NEAR YOU[!]")
write("[!yellow]OR FAR FROM YOU[!]")
write("[!red]DISTANCE IS RELATIVE WHEN REALITY IS PROGRAMMABLE[!]")
enter()

write("Thank you for playing [!purple]HACKER 4: The Mystery Dust Conspiracy[!]!")
write("Created by [!green]ethandacat[!] with [!blue]100% organic Mystery Dust[!] and [!cyan]locally sourced chaos[!].")
write("Special thanks to [!yellow]Whiskers the Infinite[!] for [!red]not sneezing[!] during the [!purple]final boss fight[!].")
write("And to [!green]LiquidPixel101[!] for [!blue]starting this whole magnificent mess[!].")
enter()

write("Now go [!cyan]touch some grass[!].")
write("But [!red]not[!] [!purple]Mystery Grass[!].")
write("That stuff is [!yellow]dangerous[!].")
write("It [!blue]asks too many[!] [!green]philosophical questions[!].")
enter()

write("[!purple]FINAL SCORE: INFINITE MYSTERY POINTS[!]")
write("[!cyan]ACHIEVEMENT UNLOCKED: REALITY HACKER[!]")
write("[!yellow]ACHIEVEMENT UNLOCKED: DUST WHISPERER[!]")
write("[!red]ACHIEVEMENT UNLOCKED: INTERDIMENSIONAL ENTREPRENEUR[!]")
write("[!green]ACHIEVEMENT UNLOCKED: FRIEND OF COSMIC CATS[!]")
write("[!blue]ACHIEVEMENT UNLOCKED: MASTER OF IMPOSSIBLE THINGS[!]")
enter()

write("Goodbye, [!purple]hacker[!].")
write("May your [!cyan]code[!] be [!yellow]bug-free[!] and your [!red]reality[!] be [!green]appropriately mysterious[!].")
write("[!blue]Until we meet again in the digital dust...[!]")

# Secret ending for persistent players
enter()
write("...")
enter()
write("You're still here?")
enter()
write("Really?")
enter()
write("Okay, fine. [!purple]Secret ending unlocked[!].")
enter()

write("As you [!green]close[!] the [!blue]game[!], you notice something [!red]strange[!].")
write("Your [!cyan]real computer screen[!] has a [!yellow]tiny speck[!] of [!purple]glittery dust[!] on it.")
write("You [!blue]reach out[!] to [!green]wipe it off[!], but it [!red]moves[!] away from your finger.")
write("The dust [!purple]spells out[!] a [!cyan]tiny message[!]: '[!yellow]The game never really ends.[!]'")
write("Then it [!green]winks[!] at you and [!blue]disappears[!].")
enter()

write("You [!red]blink[!] and [!purple]shake your head[!].")
write("'[!cyan]That's impossible,[!]' you think.")
write("But somewhere in the [!yellow]distance[!], you hear a [!green]faint[!] [!blue]interdimensional sneeze[!]...")
enter()

write("[!red]NOW[!] it's [!purple]really[!] [!cyan]THE END[!].")
write("[!yellow]We promise[!].")
write("[!green]Maybe[!].")
write("[!blue]Probably not[!].")
slow("I think hacker 4 is coming soon")
fast("ANYWAYS CAN U LEAVE NOW LOLLLOLOLOOOO fhjdkfhskjhfksjdfhhjkjdfjsdljfkljfksdljkl I'M WAITING\nBRUH LEAVE PLSSSSSSSSSSS anyways hacker 4 comming soon lool byeeeeeeeeeeeee")

# Final system exit
sys.exit()
