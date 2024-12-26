import os
import random
import sys
from time import sleep

from replit import db

# Coloured text definitions
red = '\x1b[0;31m\x1b[1m'
bold = '\x1b[1m'
purple = '\x1b[38;2;130;0;250m\x1b[1m'
darkgrey = '\x1b[38;2;100;100;100m\x1b[1m'
green = '\x1b[0;32m\x1b[1m'
yellow = '\x1b[0;33m\x1b[1m'
blue = '\x1b[0;34m\x1b[1m'
cyan = '\x1b[0;36m\x1b[1m'
white = '\x1b[0;37m\x1b[1m'
orange = '\x1b[38;2;255;140;0m\x1b[1m'
pink = '\x1b[38;2;255;182;193m\x1b[1m'
aquamarine = '\x1b[38;2;127;255;212m'
pastel_purple = '\x1b[38;2;177;162;202m'
pastel_yellow = '\x1b[38;2;255;255;102m'
reset = '\x1b[0m'

# Player name from environment
playername = os.environ.get("REPL_OWNER", "default_player")
"""

| Not very important |


"""


# Typing animation functions
def write(words):
    for char in words:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()


def write2(words):
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


def write3(words):
    for char in words:
        sleep(0.010)
        sys.stdout.write(char)
        sys.stdout.flush()


def clear():
    os.system('clear')


def clear2(time=3.5):
    sleep(time)
    os.system('clear')


def get_ternimal_size():
    size = os.get_terminal_size()
    return size.columns


"""


PLAYER STUFF 


"""


# player stats n stuff
class Game:

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.money = 100
        self.xp = 0
        self.level = 1
        self.inventory = []
        self.max_xp = 10

    def level_up(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.max_health += 50
            # self.health = self.max_health
            self.xp = 0
            self.max_xp += 20

            print(
                f"{playername}, congratulations! You leveled up to Level {self.level}."
            )

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.max_xp:
            self.level_up()

    def is_alive(self):
        return self.health > 0

    def attack_enemies(self):
        return random.randint(1, 30)

    def take_damage(self, damage):
        self.health -= damage



player = Game()
"""



Saving data!!



"""


def load_inventory(playername):
    if playername in db:
        data = db[playername]
        print(f"Loading data for {playername}: {data}")
        sleep(0.1)
        clear()# Debugging print
        player.money = data.get("money", 100)
        player.inventory = data.get("inventory", [])
        player.xp = data.get("xp", 0)
        player.level = data.get("level", 1)
        player.health = data.get("health", 100)
        player.max_health = data.get("max_health", 100)
        player.max_xp = data.get("max_xp", 10)
    else:
        print(f"No data found for {playername}")  # Debugging print


def save_inventory(playername):
    db[playername] = {
        "money": player.money,
        "inventory": player.inventory,
        "xp": player.xp,
        "level": player.level,
        "health": player.health,
        "max_health": player.max_health,
        "max_xp": player.max_xp
    }
    print(f"Saved data for {playername}: {db[playername]}")  # Debugging print


load_inventory(playername)


def open_inventory():
    clear()
    print(f"\n{playername}'s stats:")
    print(f"""\n
    Health: {player.health}/{player.max_health}
    Money:  {player.money}
    XP:     {player.xp}/{player.max_xp}
    Level:  {player.level}
    """)
    if player.inventory:
        write(f"{playername}'s Inventory:\n")
        item_counts = {}


        for item in player.inventory:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

        for item, count in item_counts.items():
            if count > 1:
                write(f" - {item} ({count})\n")
            else:
                write(f" - {item}\n")
    else:
        write2(f"{playername} has no items in their inventory.\n")
    input(f"{blue}Press Enter to continue.{reset}")
    clear()


"""


SHKAI(ELEMENT) STUFF



"""


zanpakuto = {
    "fire":{
        "moveset":{
            "flame slice" : {
                "damage": 20, 
            },
            "Incinerate": {
                "damage": random.randint(10,25)
            },
            "Inferno Cleave" : {
                "damage": random.randint(5,35)
            },

        },
    },

    
    "Ice":{
        "moveset":{ 
            "Glacial Strike" : {
                "damage": random.randint(1,40)
            },
            
            "Frozen Blast" :{
                "damage": 20
                
            },
            "Frostbite" : {
                "damage": random.randint(1,40)
                
            },
            

        },
    },

    "Speed":{
        "moveset":{
            "Getsuga Tensho" : {
                "damage": random.randint(10,50)
            },
            "Flashstep Assault":{
                "damage": random.randint(5,25)
            },
            "Tempest Strike":{
                "damage": random.randint(10,20)
                
            }

      },  
    },
}


#cutsceens
cutscene1 = """
=================================================
║                                               ║
║                                               ║
║ My spirit stands firm and calls out my name   ║
║                                               ║
=================================================
"""


cutscene2 = """
=============================================
║                                           ║
║                                           ║
║        | You hold me within |             ║                  
║                                           ║
=============================================
"""

cutscean3 = """
=============================================
║                                           ║
║         Shikai has been unlocked!         ║
║                                           ║
=============================================
"""



"""
ENEMIES/NPCS



"""


# Enemy classes
class Hollow:

    def __init__(self):
        self.name = "Hollow"
        self.health = 70
        self.attack = 9

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self):
        write2("The hollow attacks you!")
        return random.randint(1, self.attack)


class Quincy:

    def __init__(self):
        self.name = "Quincy"
        self.health = 85
        self.attack = 12

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self):
        write2("The quincy shoots you with their bow!")
        return random.randint(1, self.attack)


#new element boss
class ShikaiBoss:

    def __init__(self):
        self.name = "Shikai Boss"
        self.health = 200
        self.attack = 40

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_player(self):
        write("Your zanpakto unleashes a powerful attack!")
        return random.randint(12, self.attack)


"""



ARCADE + SHOP



"""

arcade_items = {
    "common": ["Soul Ticket", "Soul Candy"],
    "rare": ["Urahara's Fan", "Lesser Bankai Manual"],
    "epic": ["Kenpachi's Eyepatch", "Partial Visord"],
    "legendary": ["Lesser Hogyoku", "Yhawach's Blood"],
    "mythical": ["Hogyoku", "Oken"],
    "exotic": ["Oken robes", "Soul king's right arm"],
    "unfathomable":
    ["Soul King’s Fragments", "Yhawach's Shrift", "Muramasa manual"],
    "play_cost":
    2000,
}
arcade_sell = {
    "common": 250,
    "rare": 2300,
    "epic": 4500,
    "legendary": 9000,
    "mythical": 12500,
    "exotic": 15000,
    "unfathomable": 20000,
}
arcade_rarities = {
    "common": 67,
    "rare": 20,
    "epic": 10.99999999999999,
    "legendary": 1,
    "mythical": 0.5,
    "exotic": 0.025,
    "unfathomable": 0.01,
}
arcade_image = """                                       
  =@+====================================+%@ .#####
  =@**************************************#@ ..*#.
  -+::..................................::-#   -=   
 .. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ :   *%  
  . .@@          %@   -++-   #@   -++-   @@ .@: -+    
  .  @@          @@          @@          @@  @#*##%=  
  .  @@  ####### @@  %###### @@  %###### @@  %====%=  
  .  @@  #   ##  @@  #=..##  @@  #*..##. @@  %====#-  
  .  @@     ##.  @@  ...##.. @@  ...##.. @@  %==++%= 
  .  @@    %#..  @@  ..%#..  @@  ..##... @@  @#%@@@+ 
  .  @@  ......  @@  ......  @@  ......  @@ .@-      
  . .@@   ....   %@   ....   #@   ....   @@ .    
  .. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ =                
   =@****:#@%%%%%%%%%%%%%%%%%%%%%%%%@%-****#@  
   -#==== @@@@@@@@@@@@@@@@@@@@@@@@@@@@.-====@ 
   -#==== @@@######################@@@ -====@ 
   -#====: #@@@@@@@@@@@@@@@@@@@@@@@@# .=====@  
   =%=====:   ....................   :-====*@ 
"""
colors = [
    purple, orange, green, aquamarine, red, pink, pastel_purple, pastel_yellow,
    blue
]

urahara_shop_image = """
 _____________________________|_______________
 /           _    ___________     _________  /|
|  _______   |  /           \   |         |/ |
| |       |  | |             |  |  ______ |  |
| |       |  | |   ____      |  | |      ||  |
| |       |  | |  |    |     |  | |      ||  |
| |       |  | |  |____|     |  | |______||  |
| |       |  | |             |  |          |  |
| |_______|  | |             |  |          |  |
|___________|/  \_____________/   |__________ |
|                                         |   |
|  _________ Urahara's Shop _________   |    |
|  |_______________________________|   |    |
|  |              |                |   |    |
|  |              |                |   |    |
|  |              |                |   |    |
|__|_______________________________|___|____|
"""

#Urahara shop stuff

items_in_shop = {
    "Cloak of reiatsu": 500,
    "Portable Gigai": 2000,
    "Anti Hierro Armour": 3500,
    "Soul Cane": 6000,
    "Hogyoku": 35000,
}


def shop_urahara():
    # print(items_in_shop)  # I will help format the dictionary
    for items in items_in_shop:
        print(f"{items}: {items_in_shop[items]}")
    option = input("What would you like to buy in Uraharas shop? 1-7")
    if option == '1':
        input(
            f"Would you like to purchase the cloak of reiatsu for {items_in_shop['Cloak of reiatsu']} money? Press enter to continue"
        )
        if player.money >= items_in_shop["Cloak of reiatsu"]:
            player.inventory.append("Cloak of reiatsu")
            save_inventory(playername)
            player.money -= items_in_shop["Cloak of reiatsu"]
            write(
                f"You bought the Cloak of reiatsu for {items_in_shop['Cloak of reiatsu']} money"
            )
            sleep(2)
            clear()
        else:
            print("insuffient funds")
            clear()
    if option == '2':
        input(
            f"Would you like to purchase the portable gigai for {items_in_shop['Portable Gigai']} money? Press enter to continue"
        )
        if player.money >= items_in_shop["Portable Gigai"]:
            player.money -= items_in_shop["Portable Gigai"]
            print(
                f"You bought the Portable Gigai for {items_in_shop['Portable Gigai']} for money"
            )
            player.inventory.append("Portable Gigai")
            save_inventory(playername)
            sleep(2)
            clear()
        else:
            print("insuffient funds")
            clear()

    if option == '3':
        input(
            f"Would you like to purchase the anti hierro armour for {items_in_shop['Anti Hierro Armour']} money? Press enter to continue"
        )
        if player.money >= items_in_shop["Anti Hierro Armour"]:
            player.money -= items_in_shop["Anti Hierro Armour"]
            print(
                f"You bought the Anti Hierro Armour for {items_in_shop['Anti Hierro Armour']} for money"
            )
            player.inventory.append("Anti Hierro Armour")
            save_inventory(playername)
            sleep(2)
            clear()
        else:
            print("insuffient funds")
            clear()

    if option == '4':
        input(
            f"Would you like to purchase the soul cane for {items_in_shop['Soul Cane']}"
        )
        if player.money >= items_in_shop["Soul Cane"]:
            player.money -= items_in_shop["Soul Cane"]
            print(
                f"You bought the Soul Cane for {items_in_shop['Soul Cane']} for money"
            )
            player.inventory.append("Soul Cane")
            save_inventory(playername)
            sleep(2)
            clear()
        else:
            print("insuffient funds")
            clear()

    if option == '5':
        input(
            f"Would you like to purchase the hogyoku for {items_in_shop['Hogyoku']}"
        )
        if player.money >= items_in_shop["Hogyoku"]:
            player.money -= items_in_shop["Hogyoku"]
            print(
                f"You bought the Hogyoku for {items_in_shop['Hogyoku' ]} for money"
            )
            player.inventory.append("Hogyoku")
            save_inventory(playername)
            sleep(2)
            clear()
        else:
            print("insuffient funds")
            clear()


def random_color():
    return random.choice(colors)


def arcade_main():
    print(arcade_image)
    sleep(2)
    clear()
    write2(
        "you walk inside the arcade the room is filled with friendly faces\n")
    global money
    write2("Do you want to play? (y/n) ")
    play = input(f"{blue}Enter your choice (y/n):{reset} ")
    if play.lower() == 'y':
        write2("you walk up to the arcade machine \n")
        if player.money >= arcade_items["play_cost"]:
            play_game = random.choices(list(arcade_items.keys())[:-1],
                                       weights=[
                                           arcade_rarities[r]
                                           for r in arcade_rarities
                                           if r != 'cost'
                                       ],
                                       k=1)[0]
            arcade_item = random.choice(arcade_items[play_game])
            player.inventory.append(arcade_item)
            write2(
                f"You rolled and got a{random_color()}{bold} {arcade_item}{reset}!\n"
            )
        else:
            print("Insufficent funds")
    elif play.lower == 'n':
        write2("you walk away from the arcade\n")

    else:
        print(f"{red}invalid option{reset}")


"""


###################
Combat mechainics ig





"""


# Battle system
class Fight:

    @staticmethod
    def start_battle(player, enemy):
        clear()
        print(random_event_scenarios(player, enemy))

        while player.is_alive() and enemy.is_alive():

            print(
                f"\n{playername}'s Health: {player.health} | {enemy.name}'s Health: {enemy.health}"
            )

            write("\nChoose your move:")
            write(f"\n1.{orange} Attack{reset}")
            write(f"\n2.{blue} Defend{reset}")

            move_choice = input("\nEnter your move (1/2): \n")

            if move_choice == '1':
                player_damage = player.attack_enemies()
                enemy_damage = enemy.attack_player()

                if random.random() < 0.9:

                    write(
                        f"\nYou dealt {player_damage} damage to {enemy.name}.\n"
                    )
                    enemy.take_damage(player_damage)

                else:
                    write("\nYou missed the attack!\n")
                    enemy.take_damage(player_damage * 0)

                if random.random() < 0.9:
                    write(
                        f"\n{enemy.name} dealt {enemy_damage} damage to you.\n"
                    )
                    player.take_damage(enemy_damage)

                else:
                    write("\nYour enemy missed the attack!\n")
                    player.take_damage(enemy_damage * 0)

            elif move_choice == '2':
                write("\nYou chose to defend. You parried the attack\n")

                enemy_damage = enemy.attack_player() * 0

                player.take_damage(enemy_damage)

            else:
                enemy_damage = enemy.attack_player()
                write("\nInvalid move. You stumble and take extra damage.\n")
                write(
                    f"\n{enemy.name} dealt {enemy_damage} damage to you.\n\n")
                player.take_damage(enemy_damage)

        if not enemy.is_alive():
            print("\nYou have completed the mission.")
            player.gain_xp(10)
            player.money += 50
            save_inventory(playername)
            print("You gained 50 money.")
        elif not player.is_alive():
            print("\nYou lost the battle and failed to complete the mission.")

class bossFight:
    @staticmethod
    def start_boss_battle(player, enemy):
        return player + enemy


# Random event scenarios
def random_event_scenarios(player, enemy):

    scenarios = [
        f'You explore Soul Society and encounter a {random_color()}{enemy.name}{reset}!',
        f'Kisuke Urahara approaches you and asks for help to defeat the {random_color()}{enemy.name}{reset}.',
        f'You are tasked to defeat and bait {random_color()}{enemy.name}{reset} by Shinji.'
    ]


# Randomly select an enemy
def get_random_enemy():
    return random.choice([Hollow(), Quincy()])


"""




START OF GAME LOOPS 






"""
# Game loop options
options = f"""
||   What would you like to do:   ||

    {random_color()}1. Do a mission {reset}
    {random_color()}2. Heal {reset}
    {random_color()}3. Explore {reset}
    {random_color()}4. Open Inventory\n {reset}

"""

#Stuff for the explore
places = f"""
||   Where would you like to go:   ||
        {random_color()}1. Arcade {reset}
        {random_color()}2. Urahara's shop {reset}
        {random_color()}3. Karakura Highschool {reset}
        {random_color()}4. Kurosaki Clinic\n {reset}
"""


def start_game():
    while player.is_alive():
        write(options)
        choice = input("Enter your choice: ")

        if choice == '1':
            enemy = get_random_enemy()
            Fight.start_battle(player, enemy)
            sleep(2)
            clear()

        elif choice == '2':
            player.health = player.max_health
            write2("You healed yourself back to full health.\n")
            sleep(2)
            clear()

        elif choice == '3':
            write2("You go into the senkaimon to Karakura Town\n")
            write2(places)
            travel = input("Enter your choice: ")

            if travel == '1':
                write2("You visit the Arcade\n")
                arcade_main()

            elif travel == '2':
                print("You visit Urahara's shop it is crouded with people")
                shop_urahara()
            elif travel == '3':
                write("You visit Karakura Highschool\n")
                print("#COMING SOON")
            elif travel == '4':
                write("You visit Kurosaki Clinic\n")
                print("He heals u")
        elif choice == '4':
            open_inventory()

        else:
            write2("Invalid choice. Please choose a valid option.\n")
            sleep(1)
            clear()


t_size = get_ternimal_size()

ascii_art = f'''{darkgrey}
               ?@        @;,,,,@?              
             +@@:        @*,,,,:%#;            
            %@*#:       ?#:,:,,,;@%:           
           :@::%        :@:,*@#,,:@@           
           @+,:@:      :@:,?@@%,,*@;           
          ?#,,,%:      ?@::#@@@:,,##           
          ##,,,?@      @?,:@@@@S,,##           
          ##,,,,##+;;?@%,,*@@@@@,,##     :+,   
     *    *#,,,,+@@@@@?,,*@@@@@@,,##      S%;,,
   ;S#    @+,:#::::::,,*@@@@@@@,,#;      ?@S,, 
   ?@#     #?,:@@#:::::+@@@@@@@@,;#,      *@S?,
  :@@#     :S,:@@@@@#@@@@@@@@@@?,*?       ?@,S:
  #%##     ;@::@@@@@@@@;;#@@@@@;,*:       #@,?+
  @?S@+    *@::@@@@@#*,,,,:@@@@:,?@.     ;@:,*@
  @*,@S+:;*@%,:@@@S?,,,,,,,:?@@;,;@+    :@#:,:#
  #:,+@@S@@#:,:@@#:,,,,,,,,,,*@#,,;@S?;%##:,,,#
  #;,,,S@@:,,,@@@,,,,,,,,,,,,,*@,,,,S@@#:,,,,+@
  %?,,,,+++++#@@:,,,,,,,,,,,,,,##+,,,,,,,,,,,*#
  :S:,,,@@@@@@@%,,,,,,,,,,,,,,,%@@S%+,,,,,,,:#+
   ?@.,,;@@@@@@?,,*:,,,,,,,+#,,,@@@@@@:,,,,,@S,
    ?#:,,+@@@@@*,,SS,,,,,,,?@,,,@@@@@@;,,,:##+ 
     *S:,,#@@@@;,:@@,,,,,,,?@,,,@@@@S*,,,:S?;  
      ?@,,,@@@#,,:@@,,,,,,:#@+,,@@@@*,,,SS:    
       #S,,@@@#,,:@@:,,,,,:@@#,,@@@S,,+#;      
       S#,,@@@#,,:@@#,,,,,:@@#,,@@@:,,#;       
       :#,,@@@#,,*@@#,,,,,#@@#,.@@@,,%S        
        #,,@@@#,,S@@@;,,,,@@@#,,@@@.,#         
        #,,%@@#,,+@@@*,,,:@@@#,.@@#,,#         
        #;,+@@#,,,?@@*,,,S@@*:,.@@+,,#         
        @;,;@@@;,,,,@*,,,S#;,,,,@@:,+@         
        @;,:@@@S*,,,,,,,,,,,,,,+@@:,*S         
        #:,:@@@@@?,,,,,,,,,,,:S@@@:,*+         
        #;,:@@@@@#,,,,,,,,,,.@@@@@:,*;         
        @*,:#@@@@#,,,,,,,,,,,S@@@*,,*:         
        @?,,:#@@@?,,,,,,,*,,,;@@#:,:S:         
        :@:,,,;@@*,,,?:,,#,,,@@*,,,*@:         
         *@?:,,,?%;,;@:,,##%S%:,,;#S+          
          +##?;,,,+:S@%*?@#*,,,*%S*            
            +#@#:,,,,::+:,,,,*@@*              

{darkgrey}{bold}
  ___             _           _        __ __  _   _     _                 _    
 | _ \ _ _  ___  (_) ___  __ | |_     / // / (_) | |__ | | ___  __ _  __ | |_  
 |  _/| '_|/ _ \ | |/ -_)/ _||  _|   / // /   _  | '_ \| |/ -_)/ _` |/ _|| ' \ 
 |_|  |_|  \___/_/ |\___|\__| \__|  /_//_/   (_) |_.__/|_|\___|\__,_|\__||_||_|
               |__/                                                            

{aquamarine}
made by @aaronduan123
{reset}
'''

for line in ascii_art.splitlines():
    print(line.center(t_size))
sleep(5)
clear()

# Start the game
start_game()
