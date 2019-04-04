# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 08:13:48 2018

@author: Kevin
"""
"""Pokemon game created by Kevin Castillo. The game is designed for both usrs who
know pokemon and for users who don't. Its purpose is for entertainment for the user.
The game goes through five stages: 
    stage 1 - answering a question and choosing your starter pokemon
    stage 2 - capturing a wild pokemon
    stage 3 - gym battle
    stage 4 - encountering mewtwo
    stage 5 - battling in the pokemon tournament
User can only win by making it through all stages. Nested conditionals and loops are used.
Known bugs: None
"""

import random
def start():
    global name
    global pronoun
    global possesive
    global rival
    print("What's your name?", end= " ")
    name=input().capitalize()
    print("Give me the name of someone you don't like", end = "  ")
    rival = input().capitalize()
    print("What's your gender? (male/female)", end = "  ")
    gender=input().lower()
    if gender == 'male':
        pronoun='he'
    else:
        pronoun='she' 

    if gender == 'male':
        possesive='his'
    else:
        possesive='her'
    
    print(f"Welcome {name}! Welcome to the world of Pokemon where a journey of excitement "+
          "awaits you! During this game, you might be able to become a Pokemon Master! If you're " +
          "already a fan of the series, I hope you enjoy the game. If you don't like " +
          "Pokemon or have never heard of it, maybe this game can help!")
    input('<Press Enter to Continue>')
    
    pre_adventure()

def pre_adventure():
    print(f"So what do you say {name}, are you ready to become a Pokemon Trainer? (yes/no)")
    choice_1=input().lower()
    
    if 'yes' in choice_1:
        print("Awesome! Let's get started")
        stage_1()
    elif 'no' in choice_1: 
        print("Sorry to hear that, in that case this is how far you're adventure comes")
        fail()
    else :
        print("Sorry, I only understand 'yes' or 'no', please try again")
        input('<Press any key to continue>\n')
        pre_adventure()


def stage_1():
    global first_pokemon
    global pok_type1  
    print(f"Narrator:'{name} wakes up late to the alarm clock on the day {pronoun} "+
          f"is supposed to choose {possesive} Pokemon. {name} runs out the door and heads to"+
          " Professor Chase's lab")
    input("<Press Enter to Continue>")
    print(f"Professor Chase:'I see you are late as usual {name}. Fortunately for you, "+
          "all the Pokemon are still available. However, before you can choose one, "+
          "I want to test your Pokemon knowledge with this question.")
    input("<Press Enter to Continue>")
    print(    
"""Which of the following is a Pokemon?
a) unicorn
b) dogmon
c) mewone
d) mewtwo
""")    
    choice_2 = input()
    starter_pokemon = {'Bulbasaur':'grass','Charmander':'fire','Squirtle':'water'}
    if 'd' in choice_2:
        print("You know your stuff!Let's go ahead and get your Pokemon!")
        input('<Press Enter to Continue>')
        print("You now can choose from these great Pokemon: Bulbasaur, Charmander, and Squirtle")
        print("Which one do you want or do you want me to pick for you at random?")
        choice_3 = input().capitalize()
        while choice_3 != 'Random' and choice_3 != 'Bulbasaur' and choice_3 != 'Charmander' and choice_3 != 'Squirtle':
            print("I didn't understand, check your spelling and try again")
            print("Which one do you want or do you want me to pick for you at random?")
            choice_3 = input().capitalize()
        if choice_3 == 'Random':
            first_pokemon=random.choice(list(starter_pokemon.keys()))
            pok_type1=starter_pokemon[first_pokemon]
            print(f"Your pokemon was chosen for you. You are now the proud owner of {first_pokemon}!")
            print(f"{first_pokemon} is a {pok_type1} Pokemon.")
        elif choice_3 == 'Bulbasaur' or 'Charmander' or 'Squirtle':
            first_pokemon=choice_3
            pok_type1=starter_pokemon[first_pokemon]
            print(f"Great, you are now the proud owner of {first_pokemon} which is a "+
              f"{pok_type1} type.")
        
        stage_2()    
    elif choice_2 == 'a' or choice_2 == 'b' or choice_2 == 'c': 
        print("You can't own a Pokemon if you don't know that!")
        fail()
    else:
        print("Sorry, I don't understand that input, please try again")
        input('<Press any key to continue>\n')  
        stage_1()
      
    
def stage_2():
    global second_pokemon
    global pok_type2
    input('<Press Enter to Continue>')
    print(f"Narrator: {name} and {first_pokemon} embark on their Pokemon journey together. "+
          f"As with any typical rookie trainer, {first_pokemon} does not get along with {name} " +
          "right away. However, they have their first adventure when a wild pokemon appears!")
    random_pokemon = {'Pikachu':'electric', 'Vulpix':'fire','Psyduck':'water','Tangela':'grass'}
    wild_pokemon = random.choice(list(random_pokemon.keys()))
    input("<Press Enter to Continue>")
    print(f" A wild {wild_pokemon} appeared, fight it and catch it to advance!")
    captured = False
    turns = 3        
    while captured == False and turns > 0:
        print("Do you want to throw a berry, a pokeball or attack?")
        move = input().lower()
        while move != 'berry' and move != 'attack' and 'pokeball' not in move:
            print("I didn't understand your output, try again.")
            print("Do you want to throw a berry, a pokeball or attack?")
            move = input().lower()
        if move == 'berry':
            prob_list = [False, True, True]
            captured = random.choice(prob_list)
            if captured == True:
                turns = 0
                print(f"Great! {wild_pokemon} likes you and is ready to be captured. "+
                      "Throw a pokeball and it's yours!")
                print("Throw pokeball?(yes/no)")
                ball = input().lower()
                while ball != 'yes' and ball != 'no':
                    print("Invalid entry, try again.")
                    print("Throw pokeball?(yes/no)")
                    ball = input().lower()
                if ball == 'yes':
                    second_pokemon = wild_pokemon
                    print(f"Awesome! You now own {first_pokemon} and {second_pokemon}!")
                elif ball == 'no':
                    print("Oh no! {wild_pokemon} escaped! You can't move forward unless you caught it! Sorry!")
                    
            else:
                print("Aw no! The berry didn't work this time. Try it again or another move")
                turns -= 1
        elif move == 'attack':
            prob_list = [True, False]
            captured = random.choice(prob_list)
            if captured == True:
                turns = 0
                print(f"Great! {wild_pokemon} is weakened and is ready to be captured. "+
                      "Throw a pokeball and it's yours!")
                print("Throw pokeball?(yes/no)")
                ball = input().lower()
                while ball != 'yes' and ball != 'no':
                    print("Invalid entry, try again.")
                    print("Throw pokeball?(yes/no)")
                    ball = input().lower()
                if ball == 'yes':
                    second_pokemon=wild_pokemon
                    print(f"Awesome! You now own {first_pokemon} and {second_pokemon}!")
                elif ball == 'no':
                    print("Oh no! {wild_pokemon} escaped! You can't move forward unless you caught it! Sorry!")
                
            else:
                print("Aw no! Your attack didn't work this time. Try it again or another move")
                turns -= 1
        elif 'pokeball' in move:
            prob_list = [False, False, True, True, False]
            captured = random.choice(prob_list)
            if captured == True:
                turns = 0
                second_pokemon = wild_pokemon
                print(f"Awesome! {wild_pokemon} was captured! You now own {first_pokemon} and {second_pokemon}!")
            else:
                print("Aw no! The pokeball didn't work this time. Try it again or another move")
                turns -= 1
        
    
    if turns == 0 and captured == True:
        pok_type2 = random_pokemon[wild_pokemon]
        pre_stage_3()
    else:
        print("Sorry since you couldn't capture {wild_pokemon}, you can't move on and try again")
        stage_2()      
        
def pre_stage_3():
    print(f"Narrator: '{second_pokemon} joins {name} and {first_pokemon} on {name}'s Pokemon Adventure! "+
          f"Now that {name} has two Pokemon, {pronoun} feels confident and is ready to fight a gym leader.'")
    input("<Press Enter to Continue>")
    print(f"Gym leader: 'Welcome pipsqueak! My name is Misty! I'm the gym leader for Cerulean City where you currently are. "+
          "If you want a badge to make it to the Pokemon tournament, you have to beat me. Lucky for you, I have only one Pokemon.")
    input("<Press Enter to Continue>")
    print("Are you ready to battle?(yes/no)")
    choice_2= input()
    if choice_2 == "yes":
        print("Misty: 'Then straight to it. I choose Starmie!'")
        stage_3()
    elif choice_2 == "no":
        print("Misty:'I knew you couldn't handle it. Come back when and if you're ready'")
    else:
        print("Sorry, I only understand 'yes' or 'no', please try again")
        pre_stage_3()
    
def stage_3():
    global your_pokemon
    global pok_choice
    your_pokemon = {first_pokemon:pok_type1,second_pokemon:pok_type2}
    input("Press Enter to Continue>")
    print("Who do you choose? Remember, Pokemon type is important")
    pok_choice=input().capitalize()
    if pok_choice != first_pokemon and pok_choice!= second_pokemon:
        print("You either don't own that pokemon or misspelled, Try again.")
        stage_3()
    choice_type = your_pokemon[pok_choice]
    print(f"You chose {pok_choice}, a {choice_type} type! Time to battle!" )
    star_health = 100
    pok_choice_health = 125
    if pok_type1 == 'fire' and pok_type2 == 'fire':
        print("Since both your pokemon are fire type, you get a special boost!")
        star_attack = 20
        pok_choice_attack = 21
    elif choice_type == 'fire':
        star_attack = 30
        pok_choice_attack = 10
    elif choice_type == "grass" or choice_type == "electric":
        star_attack = 10
        pok_choice_attack = 30
    else:
        star_attack = 20
        pok_choice_attack = 20
    while star_health > 0 and pok_choice_health > 0 :
        star_health -= pok_choice_attack
        pok_choice_health -= star_attack
        if star_health < 0:
            star_health = 0
        if pok_choice_health < 0:
            pok_choice_health = 0
        print(f"{pok_choice}'s health is {pok_choice_health} and Starmie's health is {star_health}.")
        input("<Press enter to continue>")
    if star_health <= 0:
        print(f"Misty:'No! Your {pok_choice} defeated my Starmie! Not fair! Here's your stupid badge. Hmph!")
        stage_4()
    else:
        print("You lose the battle! Should have chosen your Pokemon better. Try again.")
        stage_3()
        
def stage_4():        
    input("<Press Enter to Continue>")
    print(f"Narrator:'{name}'s journey continues after {pronoun} defeats Misty with {pok_choice} to earn "+
          f"{possesive} badge. {name} is estatic and decides to enter the Pokemon tournament. "+
          f"However, another wild pokemon appears and this is no ordinary Pokemon.")
    input("<Press Enter to Continue>")
    print(f"Unidentified Pokemon:' I know your name {name}, I know everything. Do you know who I am?")
    input("<Press Enter to Continue>")
    print("You must correctly identify this Pokemon or it will defeat you and end your journey, if you want a hint, type 'hint'")
    answer = input().capitalize()
    if answer == 'Hint':
        print("This is your only hint. I am the pokemon before the 151st Pokemon, the strongest pokemon of them all.")
        answer = input().capitalize()
    if answer == 'Mewtwo':
        print("That is correct. If you know who I am, then maybe you are the one. "+
              "Can you help me understand how Pokemon came to exist?")
        input("<Press Enter to Continue>")
        print("""How do you reply to Mewtwo?
              a) I have no idea
              b) don't answer and attack
              c) I don't care""")
        answer_2 = input().lower()
        if 'a' in answer_2:
            print("Mewtwo:'Maybe you are not the one then. However, I'll tell you what I think. I think Pokemon started with me. "+
                  "I believe I am a Pokemon god. I have realized all Pokemon are imperfections and should destroy them to create them again.'")
            input("<Press Enter to Continue>")
            print("""What do you say to Mewtwo's crazy theory?
                  a) attack
                  b) I agree with you
                  c) Pokemon may be imperfect but I like my Pokemon, all Pokemon trainers do""")
            answer_3 = input().lower()
            while answer_3 != 'a' and answer_3 != 'b' and answer_3 != 'c':
                print("Didn't understand your input, try again.")
                print("""What do you say to Mewtwo's crazy theory?
                  a) attack
                  b) I agree with you
                  c) Pokemon may be imperfect but I like my Pokemon, all Pokemon trainers do""")
                answer_3 = input().lower()
                
            if 'c' in answer_3:
                print("Mewtwo:'Pokemon trainers? I've never had a Pokemon trainer. "+
                    "Maybe I should experience having one before making a final decision. "+
                    f"Tell you what {name}), I will join you on your journey for one battle and then I will see what I do.")
                input("<Press Enter to Continue>")
                print(f"Narrator:'Incredible!{name} was able to convince Mewtwo from ending the Pokemon world "+
                      f"and Mewtwo decided to join {name} on {possesive} Pokemon adventure.")
                your_pokemon['Mewtwo']='Psychic'
                stage_5()
            elif 'a' in answer_3:
                print("Mewtwo:'You dare attack me?! For that, I'm turning your Pokemon to stone and ending the Pokemon world!")
                fail()
            elif 'b' in answer_3:
                print("Mewtwo:'I'm glad. Then you won't mind me by starting with deleting your Pokemon from this world.")
                fail()
            else:
                print("Didn't understand your input, try again.")
                stage_4()
        elif 'b' in answer_2:
            print("Mewtwo:'You dare attack me?! For that, I'm turning your Pokemon to stone and ending the Pokemon world!")
            fail()
        elif 'c' in answer_2:
            print("Mewtwo:'You don't care?! Then you won't care if I turn your Pokemon to stone and ending the Pokemon world!")
            fail()
        else:
            print("Didn't understand your input, try again.")
            stage_4()
    else:
        print("Unidentified Pokemon:'If you can't tell who I am, then I don't care for you'")
        stage_5()
        
def stage_5():
    
    global tour_choice
    print("Narrator:'After a long Pokemon journey of capturing a Pokemon, "+
          "battling a gym leader and encountering arguably the strongest Pokemon in the universe, "+
          f"{name} is approaching the end of {possesive} Pokemon journey." )
    input("<Press Enter to Continue>")
    print("You have made it this far, congratulations but you're not a Pokemon master yet. "+
          f"You must now battle one more time and it is against your rival {rival}! "+
          "However, this battle won't be about type but strategy and your interaction with the unidentified pokemon.")
    input("<Press Enter to Continue>")
    print(f"{rival}:'Can't believe you actually made it here {name}. Must be pure luck. "+
          "Don't worry though, I'll beat you and you'll be done.")
    input("<Press Enter to Continue>")
    print("Are you ready for the last battle?(yes/no)")
    choice= input()
    if choice == "no":
        print(f"{rival}:'I knew you couldn't handle it. Come back when and if you're ready'")
        stage_5()
    elif choice != 'yes':
        print("Sorry, I only understand 'yes' or 'no', please try again")
        stage_5()
    
    print(f"{rival}:'Get ready to lose! I choose Mankey!")
    input("<Press Enter to Continue>")
    print("Who do you choose? This will be about strategy and luck.")
    tour_choice = input().capitalize()
    if tour_choice != first_pokemon and tour_choice != second_pokemon and tour_choice != 'Mewtwo':
        print("You either don't own that pokemon or misspelled, Try again.")
        stage_5()
    
    print(f"You chose {tour_choice}! Time to battle!")
    tour_health = 150
    mankey_health = 130
    tour_attack = 20
    mankey_attack = 15
    while tour_health > 0 and mankey_health > 0:
        x = random.randint(0,2)
        if x == 0:
            mankey_health -= tour_attack
            tour_health -= mankey_attack
        elif x == 1:
            mankey_health -= tour_attack * 1.3
            tour_health -=mankey_attack
        else: 
            mankey_health -= tour_attack
            tour_health -=mankey_attack *1.5
        if mankey_health < 0:
            mankey_health = 0
        if tour_health < 0:
            tour_health = 0
        print(f"{tour_choice}'s health is {tour_health} and Mankey's health is {mankey_health}.")
        input("<Press enter to continue>")
    if mankey_health == 0:
        print("You defeated Mankey!")
        print(f"{rival}:'Not a problem, Mankey is my weak pokemon. Get ready for this.'")
        battle_2()
    elif tour_health == 0:
        print(f"{rival}:'Ha! I knew you weren't a true Pokemon trainer.")
        fail()
    
    
         
               
def battle_2():
    pok_list = list(your_pokemon.keys())
    pok_set = set(pok_list)
    print(f"{rival}:'I now choose Tauros!'")
    input("<Press Enter to continue>")
    print("You must now choose a different Pokemon. Who do you choose?")
    tour_2 = input().capitalize()
    if tour_2 == tour_choice:
        print(f"Your already chose {tour_2}, try again!")
        battle_2()
    pok_list = pok_list.remove(tour_choice)
    if tour_2 in pok_set:
        print(f"You chose {tour_2}!")
    else:
        print("You either don't own that pokemon or misspelled, Try again.")
        battle_2()
    if 'Mewtwo' in pok_set:
        if tour_2 == 'Mewtwo':
            tour2_health = 200
            tauros_health = 150
            tour_2_attack = 50
            tauros_attack = 30
        else:
            tour2_health = 150
            tauros_health = 150
            tour_2_attack = 35
            tauros_attack = 30
    else:
        tour2_health = 150
        tauros_health = 150
        tour_2_attack = 35
        tauros_attack = 30
    
    while tour2_health > 0 and tauros_health > 0:
        x = random.randint(0,2)
        if x == 0:
            tauros_health -= tour_2_attack
            tour2_health -= tauros_attack
        elif x == 1:
            tauros_health -= tour_2_attack * 1.5
            tour2_health -=tauros_attack
        else: 
            tauros_health -= tour_2_attack
            tour2_health -=tauros_attack *1.4
        if tauros_health < 0:
            tauros_health = 0
        if tour2_health < 0:
            tour2_health = 0
        print(f"{tour_2}'s health is {tour2_health} and Tauro's health is {tauros_health}.")
        input("<Press enter to continue>")
    if tauros_health == 0:
        print("You defeated Taurus!")
        print(f"{rival}:'This can't be happening! Ugh!'")
        end()
    elif tour2_health == 0:
        print(f"{rival}:'Ha! I knew you weren't a true Pokemon trainer.")
        fail()
def end():
    input("<Press Enter to Continue>")
    print(f"Narrator:'{name}'s Pokemon journey has now has come to an end after winning the Pokemon tournament.'")
    input("<Press Enter to Continue>")
    print("Or has it?")
    input("<Press Enter to Continue>")                
    print("Congratulations! You're a Pokemon Master!")
    print("""
░█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀ """)
    print("Do you want to try again?")
    replay = input()
    if "yes" in replay:
        start()
    else:
        print("No problem!")
        input('<Press any key to exit>')  
    
def fail():
    print("You're not a Pokemon Master, but you can try again!")
    print("Do you want to try again?")
    replay = input()
    if "yes" in replay:
        start()
    else:
        print("No problem!")
        input('<Press any key to exit>')  

start()       
