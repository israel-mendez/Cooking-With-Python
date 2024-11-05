# Israel Méndez Crespo
# Scripting Languages
# COP 2830C Section 31462
# Projects 1.4

# Pókemon in Python
# Scenario project: This project is part of a discussion forum
# that prompts students to create a program deriving from a
# certain scenario. This projects adherence to the prompts can
# be found in the skill_level variables, level_up functions,
# and class attributes.

import os
import winsound
import time
import sys
import random

# About Sound:

# WINSOUND - This method works in Windows, but for other OS you can uncomment
# the import os line below and replace the WINSOUND functions along the code
# with the ones below. These will only play the sound and do not seem to
# to offer additional options but more functionality can be added with pysound

# import os
# os.system("aplay battle.wav&") #Linux
# os.system("afplay battle.wav&") #Mac

# CLEAR - This method will equal a system call to erase the terminal and avoid
# excess of information on the screen as well as ease use of the program

clear = lambda: os.system('cls')


# SLOW_PROMPT, SLOW_DRAW - these are similar functions made to imitate the
# pacing of 16-bit generation mobile game prompts. I would have used just one but
# the time function throws a data type error when passing ints and floats as args

def slow_prompt(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)


def slow_draw(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.000001)


# POKEMON CLASS - this class holds common attributes shared
# by all Pokémon. The attributes are established by the
# scenario specifications. It will also allow ease of use
# when printing values, comparing attributes, defining
# battle functions and code organization.

class Pokemon:
    # DEFAULT CONSTRUCTOR
    def __init__(self, arg_name, arg_type, arg_art, arg_hp, arg_melee, arg_ranged, arg_block,
                 arg_agility, arg_healing, arg_move_list, arg_move_names):
        self.name = arg_name
        self.type = arg_type
        self.art = arg_art
        self.max_hp = arg_hp
        self.hp = arg_hp
        self.melee = arg_melee
        self.ranged = arg_ranged
        self.block = arg_block
        self.agility = arg_agility
        self.healing = arg_healing
        self.move_list = arg_move_list
        self.move_names = arg_move_names
        self.buff = False
        self.buff_type = ""
        self.debuff = False
        self.debuff_type = ""

    # VIEW STATS - This function is simple. It prints out
    # most of the class attributes of a particular object

    def view_stats(self):
        slow_prompt("\nName    : " + self.name)
        slow_prompt("\nType    : " + self.type)
        slow_prompt("\nHP      : " + str(self.max_hp))
        slow_prompt("\nMelee   : " + skill_level[self.melee])
        slow_prompt("\nRanged  : " + skill_level[self.ranged])
        slow_prompt("\nBlock   : " + skill_level[self.block])
        slow_prompt("\nAgility : " + skill_level[self.agility])
        slow_prompt("\nHealing : " + skill_level[self.healing])
        slow_prompt("\nMoves   -")
        # Iterates over move list
        n = 1
        for i in self.move_names:
            slow_prompt(" " + i + " -")
            n += 1
        print("\n")

    # DRAW FUNCTION - this function will call the slow_draw function
    # and pass the art attribute of the pertaining Pokémon object
    # that calls the function through the argument

    def draw(self):
        slow_draw(self.art)

    # MY_MOVE - this function can be called by any Pokémon
    # object. It takes another Pokémon object as argument
    # to calculate and store battle operations

    def my_move(self, opponent):
        slow_prompt("Choose your move: \n")

        # Iterates over Pokémon moves
        n = 1
        for i in self.move_names:
            slow_prompt(str(n) + "- ")
            slow_prompt(i)
            slow_prompt("\n")
            n += 1

        # Validates move choice input
        valid_move_choice = False
        move_choice = input("\nSelect: ")

        while not valid_move_choice:
            if (int(move_choice) > 0) or (int(move_choice) <= 4):
                self.move_list[int(move_choice) - 1](self, opponent)
                valid_move_choice = True
            else:
                move_choice = input("Please select a valid move number : ")
        return opponent

    # BATTLE FUNCTION - This function serves to direct the flow of battle.
    # The function can be called by a Pokemon object and will pass another
    # Pokemon object as an argument. Its calculations will determine which
    # Pokemon object has the next move, prints battle data, outputs battle
    # audio and verifies when the battle is over.

    def battle(self, opponent):
        # Plays battle theme
        winsound.PlaySound("battle", winsound.SND_FILENAME | winsound.SND_ASYNC)
        # Prints opponent on console
        opponent.draw()
        # Battle flow
        buff_counter = 0
        debuff_counter = 0
        slow_prompt(opponent.name + " wants to battle!\n\n")
        while self.hp > 0 and opponent.hp > 0:
            # Validates, counts, and deactivates buffs and debuffs
            if self.buff and buff_counter > 2:
                temp_buff(self, False, self.buff_type)
                buff_counter = 0
            elif self.buff and buff_counter <= 2:
                buff_counter += 1

            if self.debuff and debuff_counter > 2:
                temp_debuff(self, False, self.debuff_type)
                debuff_counter = 0
            elif self.debuff and debuff_counter <= 2:
                debuff_counter += 1

            # Determines turn order
            if self.agility > opponent.agility:
                self.my_move(opponent)
                if self.hp <= 0:
                    slow_prompt("\nThere's always next time!\n")
                    break
                elif opponent.hp <= 0:
                    slow_prompt(opponent.name + " is knocked out!\n")
                    break
                else:
                    slow_prompt(opponent.name + "'s HP fell to " + str(int(opponent.hp)) + "\n")
                    opponent.move_list[random.randrange(len(opponent.move_list)) - 1](opponent, self)
                    if self.hp <= 0:
                        slow_prompt("\nThere's always next time!\n")
                    elif opponent.hp < 0:
                        slow_prompt(opponent.name + " is knocked out!\n")
                        break
                    else:
                        slow_prompt(self.name + "'s HP fell to " + str(int(self.hp)) + "\n")
            else:
                opponent.move_list[random.randrange(len(opponent.move_list)) - 1](opponent, self)
                if self.hp <= 0:
                    slow_prompt("\nThere's always next time!\n")
                    break
                elif opponent.hp <= 0:
                    slow_prompt(opponent.name + " is knocked out!\n")
                    break
                else:
                    slow_prompt(self.name + "'s HP fell to " + str(int(self.hp)) + "\n")
                    self.my_move(opponent)
                    if opponent.hp <= 0:
                        slow_prompt("\n" + opponent.name + " is knocked out!\n")
                    elif self.hp <= 0:
                        slow_prompt("\nThere's always next time!\n")
                    else:
                        slow_prompt(opponent.name + "'s HP fell to " + str(int(opponent.hp)) + "\n")
        if self.hp > 0:
            winsound.PlaySound("victory", winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.level_up(opponent)
            time.sleep(3)
            add_pokemon(opponent)
        else:
            winsound.PlaySound("flute", winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(3)
            winsound.PlaySound("route24", winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.hp = self.max_hp
            input("Press any key to continue ")
            main_menu(self)

    # LEVEL UP: This function will execute after the
    # user has one a battle. The function will evaluate
    # the highest attribute of the Pokémon object that
    # was battled with and award a point to the self
    # Pokémon object that is leveling up.

    # To keep within the constraints of the scenario
    # the function does not allow any attribute value
    # to exceed 8.

    def level_up(self, opponent):
        my_attributes = [self.melee, self.ranged,
                         self.block, self.agility, self.healing]

        enemy_attributes = [opponent.melee, opponent.ranged,
                            opponent.block, opponent.agility, opponent.healing]

        attribute_names = ["Melee", "Ranged",
                           "Block", "Agility", "Healing"]
        max_index = 0
        max_value = 0

        # Looks for maximum attribute value
        for i in range(0, 5):
            current_value = int(enemy_attributes[i])
            if current_value > max_value:
                max_index = i
                max_value = current_value

        # Only levels up if nox on max level
        if my_attributes[max_index] <= 7:
            if max_index == 0:
                pre_value = self.melee
                self.melee += 1
            elif max_index == 1:
                pre_value = self.ranged
                self.ranged += 1
            elif max_index == 2:
                pre_value = self.block
                self.block += 1
            elif max_index == 3:
                pre_value = self.agility
                self.agility += 1
            elif max_index == 4:
                pre_value = self.healing
                self.healing += 1

            self.max_hp += 1
            self.hp = self.max_hp

            # prints level up prompt
            slow_prompt("\n" + self.name + "'s " + attribute_names[max_index] + " attribute has leveled up!\n")
            slow_prompt(skill_level[pre_value] + "  =====>  " + skill_level[pre_value + 1] + "\n\n")


# POKEMON CLASS ENDS

# MOVE FUNCTIONS these will be called when executing a Pokémon move
# The functions take the self instance and the opponent instance that
# is passed by argument and make calculations to determine damage and
# effects. Special messages are printed if needed.

# Attack calculations are derivatives of the Standard RPG Damage Formula
# Standard RPG Damage Formula: attack*(100/(100+defense))

def tackle(self, opponent):
    slow_prompt(self.name + " heavily tackles " + opponent.name + "!\n")
    opponent.hp -= int(self.melee * (100 / (100 + opponent.block)))
    return opponent


def vine_whip(self, opponent):
    slow_prompt(self.name + " WHIPS " + opponent.name + " rapidly!\n")
    if opponent.type == "Rock":
        opponent.hp -= int(self.ranged * (260 / (100 + opponent.block)))
        slow_prompt("It's super effective")
    else:
        opponent.hp -= int(self.ranged * (130 / (100 + opponent.block)))
    return opponent


def leech_seed(self, opponent):
    slow_prompt(self.name + " leeches life from " + opponent.name + "!\n")
    opponent.hp -= int(self.healing * (70 / (100 + opponent.block)))
    self.hp += int(self.healing * (70 / (100 + opponent.block)))
    slow_prompt(self.name + " heals its HP back to " + str(int(self.hp)) + "\n")
    return opponent


def growth(self, opponent):
    slow_prompt(self.name + " Starts amassing energy!\n")
    temp_buff(self, True, "Melee")
    return opponent


def scratch(self, opponent):
    slow_prompt(self.name + " scratches " + opponent.name + "!\n")
    opponent.hp -= int(self.melee * (100 / (100 + opponent.block)))
    return opponent


def ember(self, opponent):
    slow_prompt(self.name + " sets " + opponent.name + "on FIRE!\n")
    if opponent.type == "Grass":
        opponent.hp -= int(self.melee * (260 / (100 + opponent.block)))
        slow_prompt("It's super effective")
    else:
        opponent.hp -= int(self.ranged * (130 / (100 + opponent.block)))
    return opponent


def smoke_screen(self, opponent):
    slow_prompt(self.name + " sets hides in a cloud of smokescreen\n")
    temp_buff(self, True, "Block")
    return opponent


def flamethrower(self, opponent):
    slow_prompt(self.name + " fires a huge plume of flame!\n")
    if opponent.type == "Grass":
        opponent.hp -= int(self.ranged * (280 / (100 + opponent.block)))
        slow_prompt("It's super effective")
    else:
        opponent.hp -= int(self.ranged * (140 / (100 + opponent.block)))
    return opponent


def bite(self, opponent):
    slow_prompt(self.name + " bites " + opponent.name + "!\n")
    opponent.hp -= int(self.melee * (100 / (100 + opponent.block)))
    return opponent


def water_gun(self, opponent):
    slow_prompt(self.name + " BLASTS " + opponent.name + " with a jet of water!\n")
    if opponent.type == "Fire":
        opponent.hp -= int(self.ranged * (270 / (100 + opponent.block)))
        slow_prompt("It's super effective")
    else:
        opponent.hp -= int(self.ranged * (135 / (100 + opponent.block)))
    return opponent


def withdraw(self, opponent):
    slow_prompt(self.name + " withdraws into its shell.\n")
    temp_buff(self, True, "Block")
    return opponent


def skull_bash(self, opponent):
    slow_prompt(self.name + " heavily bashed " + opponent.name + " with its shell!\n")
    opponent.hp -= int(self.ranged + self.melee) * (100 / (100 + opponent.block))
    return opponent


def thunder_shock(self, opponent):
    slow_prompt(self.name + " SHOCKS " + opponent.name + " with electricity!\n")
    opponent.hp -= int(self.ranged) * (100 / (100 + opponent.block))
    return opponent


def quick_attack(self, opponent):
    slow_prompt(self.name + " does a quick attack!\n")
    opponent.hp -= int(self.agility * (85 / (100 + opponent.block)))
    quick_attack2(self, opponent)
    return opponent


def quick_attack2(self, opponent):
    slow_prompt(self.name + " does another quick attack!\n")
    opponent.hp -= int(self.agility * (75 / (100 + opponent.block)))
    return opponent


def thunder(self, opponent):
    slow_prompt(self.name + " blasts " + opponent.name + " with a devastating bolt\n")
    if opponent.type == "Flying" or opponent.type == "Water":
        opponent.hp -= int(self.ranged * (220 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (110 / (100 + opponent.block)))
    return opponent


def iron_tail(self, opponent):
    slow_prompt(self.name + " slaps " + opponent.name + " with its Iron Tail!\n")
    opponent.hp -= int(self.melee * (75 / (100 + opponent.block)))
    return opponent


def sand_attack(self, opponent):
    slow_prompt(self.name + " uses Sand Attack on " + opponent.name + "!\n")
    opponent.hp -= int(self.agility * (50 / (100 + opponent.block)))
    temp_debuff(opponent, True, "Agility")
    return opponent


def swift(self, opponent):
    slow_prompt(self.name + " does a SWIFT attack!\n")
    opponent.hp -= int(self.agility * (150 / (100 + opponent.block)))
    return opponent


def twineedle(self, opponent):
    slow_prompt(self.name + " uses TWINEEDLE!\n")
    opponent.hp -= int((self.agility + self.melee) * (50 / (100 + opponent.block)))
    return opponent


def fury_attack(self, opponent):
    slow_prompt(self.name + " does a furious attack!\n")
    opponent.hp -= int((int(random.randrange(5)) * (50 / (100 + opponent.block))))
    return opponent


def poison_sting(self, opponent):
    slow_prompt(self.name + " stings " + opponent.name + " with a poison barb!\n")
    opponent.hp -= int(self.melee * (55 / (100 + opponent.block)))
    temp_debuff(opponent, True, "Poison")
    return opponent


def gust(self, opponent):
    slow_prompt(self.name + " starts a strong gust!\n")
    opponent.hp -= int((self.agility + self.ranged) * (50 / (100 + opponent.block)))
    return opponent


def wing_attack(self, opponent):
    slow_prompt(self.name + " uses WING ATTACK on " + opponent.name + "\n")
    if opponent.type == "Grass" or opponent.type == "Fighting":
        opponent.hp -= int(self.ranged * (240 / (100 + opponent.block)))
    opponent.hp -= int(self.ranged * (120 / (100 + opponent.block)))
    return opponent


def fly(self, opponent):
    slow_prompt(self.name + " starts a strong gust!\n")
    opponent.hp -= int((self.agility + self.ranged + self.melee) * (30 / (100 + opponent.block)))
    return opponent


def acid(self, opponent):
    slow_prompt(self.name + " Spews ACID on " + opponent.name + "!\n")
    if opponent.type == "Steel":
        opponent.hp -= int(self.ranged * (180 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (90 / (100 + opponent.block)))
    temp_debuff(opponent, True, "Poison")
    return opponent


def wrap(self, opponent):
    slow_prompt(self.name + " wraps " + opponent.name + " on a tight lock!\n")
    opponent.hp -= int(self.melee * (140 / (100 + opponent.block)))
    return opponent


def defense_curl(self, opponent):
    slow_prompt(self.name + " attacks " + opponent.name + " using a DEFENSIVE move!\n")
    if opponent.type == "Electric":
        opponent.hp -= int(self.block * (80 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.block * (80 / (100 + opponent.block)))
    temp_buff(self, True, "Block")
    return opponent


def flare_blitz(self, opponent):
    slow_prompt(self.name + " engulfs " + opponent.name + " in a giant FIRE BLITZ!\n")
    if opponent.type == "Grass" or opponent.type == "Ice":
        opponent.hp -= int(self.melee * (300 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.melee * (150 / (100 + opponent.block)))
    temp_debuff(self, True, "Melee")
    return opponent


def confusion(self, opponent):
    slow_prompt(self.name + " confuses " + opponent.name + " very brutally!\n")
    if opponent.type == "Psychic" or opponent.type == "Fighting":
        opponent.hp -= int((self.melee + opponent.melee) * (200 / (100 + opponent.block)))
    else:
        opponent.hp -= int((self.melee + opponent.melee) * (100 / (100 + opponent.block)))


def psybeam(self, opponent):
    slow_prompt(self.name + " shoots a a powerful PSYBEAM at " + opponent.name + "!\n")
    if opponent.type == "Psychic" or opponent.type == "Fighting":
        opponent.hp -= int(self.ranged * (250 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (150 / (100 + opponent.block)))


def reflect(self, opponent):
    slow_prompt(self.name + " constructs a reflective barrier!\n ")
    temp_buff(self, True, "Block")
    temp_debuff(opponent, True, "Range")
    return opponent


def recover(self, opponent):
    slow_prompt(self.name + " fully recovers its health! ...but something is odd.\n")
    self.hp = self.max_hp
    temp_debuff(self, True, "Block")
    return opponent


def bulk_up(self, opponent):
    slow_prompt(self.name + " is bulking up for this fight and " + opponent.name + "looks worried!\n")
    temp_buff(self, True, "Melee")
    temp_debuff(opponent, True, "Block")
    return opponent


def low_kick(self, opponent):
    slow_prompt(self.name + " low kicks " + opponent.name + " into the ground!\n")
    if opponent.type == "Normal":
        opponent.hp -= int(self.melee * (200 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.melee * (100 / (100 + opponent.block)))
    return opponent


def seismic_toss(self, opponent):
    slow_prompt(self.name + " does a wrestling move!\n")
    if opponent.type == "Normal":
        opponent.hp -= int(self.melee * (300 / (100 + opponent.block)))
    elif opponent.type == "Flying":
        opponent.hp -= int(self.melee * (0 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.melee * (150 / (100 + opponent.block)))


def wide_guard(self, opponent):
    slow_prompt(self.name + " has a strong and vigilant guard!\n")
    temp_buff(self, True, "Block")
    temp_debuff(opponent, True, "Melee")
    return opponent


def razor_leaf(self, opponent):
    slow_prompt(self.name + " shoots sharp leaves at " + opponent.name + "!\n")
    if opponent.type == "Rock" or opponent.type == "Ice":
        opponent.hp -= int(self.ranged * (200 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (100 / (100 + opponent.block)))
    return opponent


def surf(self, opponent):
    slow_prompt(self.name + " brings a huge wave towards " + opponent.name + "!\n")
    if opponent.type == "Fire" or opponent.type == "Ground":
        opponent.hp -= int(self.ranged * (200 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (100 / (100 + opponent.block)))
    return opponent


def explosion(self, opponent):
    slow_prompt(self.name + " cause an extravagant explosion! \n")
    opponent.hp -= int((self.melee + self.block) * (500 / (100 + opponent.block)))
    self.hp = 1
    temp_debuff(self, True, "Agility")
    return opponent


def curse(self, opponent):
    slow_prompt(self.name + " places a curse on " + opponent.name + "!\n")
    opponent.hp = self.hp
    self.hp += int(self.healing * (100 / (100 + self.block)))
    return opponent


def shadow_ball(self, opponent):
    slow_prompt(self.name + " shoots a giant SHADOW BALL at " + opponent.name + "!\n")
    if opponent.type == "Normal":
        opponent.hp -= int(self.ranged * (0 / (100 + opponent.block)))
    elif opponent.type == "Fairy":
        opponent.hp -= int(self.ranged * (200 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (100 / (100 + opponent.block)))

    return opponent


def shadow_ball(self, opponent):
    slow_prompt(self.name + " pulls a ghostly punch!\n")
    if opponent.type == "Normal":
        opponent.hp -= int(self.melee * (0 / (100 + opponent.block)))
    elif opponent.type == "Fairy":
        opponent.hp -= int(self.melee * (200 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.melee * (100 / (100 + opponent.block)))

    return opponent


def ice_beam(self, opponent):
    slow_prompt(self.name + " Casts an ICE BEAM at " + opponent.name + "!\n")
    if opponent.type == "Flying" or opponent.type == "Dragon":
        opponent.hp -= int(self.ranged * (230 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (115 / (100 + opponent.block)))

    return opponent


def slam(self, opponent):
    slow_prompt(self.name + " slams towards " + opponent.name + "!\n")
    if opponent.type == "Fairy" or opponent.type == "Dark":
        opponent.hp -= int(self.melee * (280 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.melee * (140 / (100 + opponent.block)))
    self.hp -= 2

    return opponent


def moon_blast(self, opponent):
    slow_prompt(self.name + " summons a moon blast into " + opponent.name + "!\n")
    if opponent.type == "Dragon" or opponent.type == "Ghost":
        opponent.hp -= int(self.ranged * (260 / (100 + opponent.block)))
    else:
        opponent.hp -= int(self.ranged * (130 / (100 + opponent.block)))

    return opponent


def hyper_beam(self, opponent):
    slow_prompt(self.name + " shoots a powerful beam at " + opponent.name + "!\n")
    opponent.hp -= int((self.ranged + self.melee) * (150 / (100 + opponent.block)))
    self.hp -= 5
    temp_debuff(self, True, "Ranged")

    return opponent


# TEMP BUFF, TEMP DEBUFF - These functions works
# with the battle flow to adjust temporary adjustments
# to Pokemon attributes

def temp_buff(self, status, buff_type):
    self.buff_type = buff_type

    if not self.buff:
        self.buff = True
        if status:
            if buff_type == "Melee":
                self.melee += 1
            if buff_type == "Ranged":
                self.ranged += 1
            if buff_type == "Block":
                self.block += 1
            if buff_type == "Agility":
                self.agility += 1
            if buff_type == "Healing":
                self.healing += 1
        else:
            if buff_type == "Melee":
                self.melee -= 1
            if buff_type == "Ranged":
                self.ranged -= 1
            if buff_type == "Block":
                self.block -= 1
            if buff_type == "Agility":
                self.agility -= 1
            if buff_type == "Healing":
                self.healing -= 1


def temp_debuff(self, status, debuff_type):
    if self.debuff and debuff_type == "Poison":
        self.hp -= 2

    self.debuff_type = debuff_type

    if not self.debuff:
        self.debuff = True
        if status:
            if debuff_type == "Poison":
                self.hp -= 2
            if debuff_type == "Melee":
                self.melee -= 1
            if debuff_type == "Ranged":
                self.ranged -= 1
            if debuff_type == "Block":
                self.block -= 1
            if debuff_type == "Agility":
                self.agility -= 1
            if debuff_type == "Healing":
                self.healing -= 1
        else:
            if debuff_type == "Melee":
                self.melee += 1
            if debuff_type == "Ranged":
                self.ranged += 1
            if debuff_type == "Block":
                self.block += 1
            if debuff_type == "Agility":
                self.agility += 1
            if debuff_type == "Healing":
                self.healing += 1


# ASCII ART SECTION BEGINS

bulbasaur_art = """\n
MMMMMMMMMNNMMMdyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMN++yd//omMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMhhhy+/++///oydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMmooho///+++//////:::::///////++symMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMyosy////::::::////++///////////:::ohNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMhooh//////:::::::::://+++/////////:::sNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMNoooh////////::::::::::::/o//////////::/mMMMMMMMMMMMMMMNmmMMMMMMMMMM
MMMMMMMsooys///////////////:::o++++++++////++++oddhhhhddmNho/:::-oNMMMMMMMM
MMMMMNsoooy+/////////////////o+::::::::/+++/::::::::------:///:::-/NMMMMMMM
MMMMNsoooyo+/////////////////s::::::::::::::::+ssoo+/:::::::::::::-oMMMMMMM
MMMNsoooyso/////////////////o/::::::::::::::::/syyyyyhyso+/:::::::/:mMMMMMM
MMNoooosso+//////////////+ooy:::::::::::::::::::/oyyyyyyyyho::::::::sMMMMMM
MNsooooyoo+////////////+ooooo::::::::::::::::::::::+syyyys+::::::::::/mMMMM
Myoooosoooo//////////+oooosy/::::::::::/::::::::::::::/+/::::hy/:::////dMMM
Nooooosoooo+////////ooooso:o::::::::+shds-/:::/+:::::::::::::sy/:+:s+`:/dMM
dooooooooooo+/////+oooso:::o:::::::oysoyh+ :/::/+::::+hyo::::::::+:sss :/NM
hoooooooooooooo+ooosyho+::/+::::::+ys- +sy` ./::/::::+hyyy/:::::::::+s- +oM
hoooooooossooooooyhhyyyh/:+:::::::sss` /sy.  ./:::::::hyyo:::::::::-:s/ -/N
moooooooooosssyhhyyyyyh+::/:::::::yss:`osy.   +::::::://:::::::::::/+s- ./y
Myooooooooosohyyyyyyyh+:::::::::::yssssssy    /::::::::::::::::::::ysy.:/:s
MMhooooooso//hyyyyyyy+:::::::::::::/+oooso----/:::::::::::::::::::::+/::::s
MMMNhssss/:::oooooo+/::::::::::::://::::::::::::::::::::::/:::::/:::::///oN
MMMMMNds:::::::::::::::::::::::::::::/+::++//::::::::::::::::::/++o+//:smMM
MMMMMMs::::::::::::::::::::::://:::::::/+ssssyssssooooooosssssyyhs/:+hNMMMM
MMMMMy::::::/:::++/+/:::::::::::///:::::::/oo++////////////++++//ohNMMMMMMM
MMMMN::::::yyys+:+ss/:::::::::::::/so++/::::::/+++++++++++++++++:sMMMMMMMMM
MMMMy::::::hyyyyyo:h/:::::::+ys+:::/yooosoooo+++++++oooooo+/:::--hMMMMMMMMM
MMMMs:::::+hyyyyyy:+o:::::::oyyo/+::/sooooooooooooooooooo/shys/--NMMMMMMMMM
MMMMs:::::+hyyyyo:/oy/:::::::/::oyhs+osoooooooooosssooooo/hyyysosMMMMMMMMMM
MMMMd/:::::+sso/:/oood/:::::::::/hyyyshooossyhdNyooooooo+/hyysosMMMMMMMMMMM
MMMMNo+/::::::::/ooooyy+:::::::::syyyosyssohMMMMNsoooooo+:/syoomMMMMMMMMMMM
MMMMMdoo+///://+oooohMMMs:::::::::yhyyshsomMMMMMMMyoooooo/::::dMMMMMMMMMMMM
MMMMMMmooooooooooosdMMMMMm+::::::::/++:hMNMMMMMMMMMmsoooo//://dMMMMMMMMMMMM
MMMMMMMMds-oys.ydosMMMMMMMMdo:://:/:/://NMMMMMMMMMMMMNd//hds+dNMMMMMMMMMMMM
MMMMMMMMMMNMMMMMMMMMMMMMMMMMMMms/dy::mmdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

charmander_art = """\n
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMMMMMMMdyso+++osydNMMMMMMMMMMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMMMMds:------------/smMMMMMMMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMMNo+:------------...-/hMMMMMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMd++/--------------....-/mMMMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMm+++/:-::-------------.--:dMMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMN++sd+o/-+--------------/--/MMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMs+yNo .y/:--------------/-+hMMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMm+ommo /h/:---------------/./NMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMMs+yhmmymh-----------------+`ydMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMN++hhddhhs-----------------ymdhMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMd++osyssh/-----------------yhyhMMMMMMM
ssssssssssssssssssssmMMMMMMMMMMMMMMMMy++++////------------------++/:mMMMMMM
sssssssossssssssssssmMMMMMMMMMMMMMMMMh++++++/:---------------------:oMMMMMM
ssssso+ossssssssssssmMMMMMMMMMMMMMMMMN++++h/:o+/::---/-----::---:+/+oMMMMMM
hhhho+++ssssssssssssmMMMMMMMMMMMMMMMMMm++++soooooooo+++//::/++s++++sNMMMMMM
hhhho+++s+/sssssssssmMMMMMMMMMMMMMMMMMMm++++so+::////+ooooooss+++ymMMMMMMMM
hhhh++++o-.+osssssssmMMMMMMMMMMMMMMMMMMMy+++++o/:::::::/osoo+oymMMMMMMMMMMM
hyys/:+++:--osssssshMMMMMMMMMMMMMMMMMMMNh++++++++++++++ooyhmMMMMMMMMMMMMMMM
yo++-:++++++sssssshMMMMMMMMMMMMMMMmhs+::/+++++++++oo+++++oymMMMMMMMMMMMMMMM
d/:..:++++++osssshMMMMNMMMMMMmhs+:-------://++++/:::/++/::--:+ydNMMMMMMMMMM
yy:..:/++//+-+sssmMMMMd/+ss/:---------------:+:.......:/-/-------/oydmNMMMM
o/+:..-++-.--./ssdMMdo+++/:----------------::``````````.//------------::ydN
h://:..-//....-sssNMMh+++++::-------------/-`````````````+/------------:odM
my+++-...-..-+sssyMMMMMNdhso+//:::::///:-/.``````````````.s//:::::::--:NMMM
mdo++:.....-sssssyMMMMMMMMMMMNmmmmy++/:-/.````````````````+NmmmmmmmmmhsNMMM
ddso+/-:-:/ossssssmMMMMMMMMMMMMMMs:::--/.`````````````````.MMMMMMMMMMMMMMMM
mmdddNhohmdhhhhhhNMMMMMMMMMMMMMm/-----/-```````````````````NMMMMMMMMMMMMMMM
NNNMMMh.-NMMMMMMMMMMMMMMMMMMMMh:------/````````````````````mMMMMMMMMMMMMMMM
MMMMMMN--/NMMMMMMMMMMMMMMMMMMs-------/.````````````````````NMMMMMMMMMMMMMMM
MMMMMMMy--:hMMMMMMMMMMMMMMMN+-------:+````````````````````-sdMMMMMMMMMMMMMM
MMMMMMMNo:-:+hNMMMMMMMMMMMm:---------::-...```````````````/--/hMMMMMMMMMMMM
MMMMMMMMd//://+oydmNMMMMMN:--------..-::-----............/:----+mMMMMMMMMMM
MMMMMMMMMm:+++++++++++oooo/--------....+----------------//---...-dMMMMMMMMM
MMMMMMMMMMNo/+++++++++++o++:-----------+--------------:++/::--...-mMMMMMMMM
MMMMMMMMMMMMmo:/++++++++o+++/:--------:+-----------:/++++++//:----oMMMMMMMM
MMMMMMMMMMMMMMNy+://+++s++++++////////o--------:/+++++++++++++////yMMMMMMMM
MMMMMMMMMMMMMMMMMMmyo+/+++++++++++++ohsssyhdmNNddhys+++++++++++++oNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMN+++++++++++hMMMMMMMMMMMMMMMMMs+++++++++++odMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNs+++++++++oNMMMMMMMMMMMMMMMMMMhso+++++++o+//+sNMMMMM
MMMMMMMMMMMMMMMMMMMMd/:o/o+++++++NMMMMMMMMMMMMMMMMMMMMMMMNmdhy/-/+::ssmMMMM
MMMMMMMMMMMMMMMMMMMNhy/-:+s/-ooymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddMmhMMMMMM
MMMMMMMMMMMMMMMMMMMMMmdmMmoymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

squirtle_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyso+++oooshdNMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy+:::::::::::----/sdMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo:::::::/::::::::-----/yNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs::::::////+:::::::::::::++mMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMN+:/::::ss  :h:::::::::::::/+oMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMo+++/::/hd++hNh:::::::::::::/omMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMh++++++//oydMMMmo:::::::::::::dhNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMo++++++++/oodNNdy:::::::::::::osmMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM+++++++++/:++oooo::::::::::::::++hMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMo+++++++++://::::::::::::::/:::://NMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMd+++++++oo++++++++++ooooooo++//+osMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMy+++++++++ooooooooo+++++++oooooyNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMso+++++++++++++++++++++++++++smMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNh+-+o+++++++++++++++++++//:/odNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMdo+s.:/ssoo++++++++++++++//+ohdmNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNy++os+o+o+++oo+ooooooo+oo++///+//++shmNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNoossyo+++/::::/+////////:::::-.-//:::::/ohmMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMssooso+++/::::--:+/::::::::--....-+/:::::--:+ymMMMMM
MMMMMMMMMMMMMMMMMMMMMMdo++oy++++::::::-::+/::::--.----::-.//:::::::::/oo+yM
MMMMMMMMMMMMMMMMMMMMMN+/++o+++++/:::::::::+/::::+:----.....//::::::::+o+sNM
MMMMMMMMMMMMMMMMMMMMMy//+++-o++++/::::///::/..../-..........+:::////+oo+odM
MMMMMMMMMMMMMMMMMMMMM+//++o`/oo++++/::o+//:+....-/.........-osoooooooosss+m
MMMMMMMMMMMMMMMMMMMMN///++s.-:+o+o+++/++++//:-...+........./-mNNNNNNNNMMMMM
MMMMMMMMMMMMMMMMMMMMN+//++o/.::o+oo+++++++++/:...+........::.dMMMMMMMMMMMMM
MMMMMMNNNNNNNMMMMMMMMs++++oo`::o://+++o+/:-......+.-----::+..mMMMMMMMMMMMMM
MMMNho//::::/oymMMMMMysooooo.::o:::::::+:::::::::o::-----./:/MMMMMMMMMMMMMM
MNy/::----------+dMMMmossoo/-:/+//::://-........./-........+sNMMMMMMMMMMMMM
Mo::::::----------sNMMyosss-//+////++/::-......../-......../-/dMMMMMMMMMMMM
h::::::::/:::::::::/dMNsos++/:::::::/+/::::--....+-......-/:---yMMMMMMMMMMM
s:::::////////:::::::sNmsy+:::::::::::++:::::::::+----:::+:-----dMMMMMMMMMM
h::::::::::::+::::::::/sds/::::::::::::/+:::://++++++//++:::----:MMMMMMMMMM
N/:::::::::::+/:::::::::+o/:::::::::::::o//++//:::://ooo+/:::::--mMMMMMMMMM
Mm+::::::::::o::::::::::o++:::::::--:::/o//:::///+sso++++++///::/dMMMMMMMMM
MMNy/:::::/++:::::::::::o++/::::::-:::/yyyhhhddmNMMMy++++++++++++mMMMMMMMMM
MMMMMmyo++/:::::::://+oyh++++/:::::::/dMMMMMMMMMMMMMMs++++++++++//sNMMMMMMM
MMMMMMMMNmddhhhddmmNMMMMm++++++++++++hMMMMMMMMMMMMMMMNmhyso+++os++mNMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMd+++++++++++oMMMMMMMMMMMMMMMMMMMMMNmdysMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMM+/++++/++o+/oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMmNMMdooymMMmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

beedrill_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMmhdhhdNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhss-+````:hNMMMMMM
MMMMMMMMMMMMMNmyssymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd+.:+.-o.--.``hMMMMMM
MMMMMMMMMMMMN+--````:sNMMMMMMMNdNMMMMMMMMMMMMMMMMMMNy:``//..:s.`````:NMMMMM
MMMMMMMMMMMNy```---::..omMMMMMNosNMMMMMMMMMMMMMMMNy-``.o:..-:o```````mMMMMM
MMMMMysmNMMMo.``.+soss/.-sNMMMmoosmMMMMMMMMMMMMNh:...-s-...:/+````..-dMMMMM
MMMMMN/-/ymNo.:+soso:oy+``:dNMhssoomNMMMMMMMMMm+````-o-...::o:.--.```dMMMMM
MMMMMMm/..:oy/soss+.``:so-:/hdyhdsosmNMMMMMMNh-````/+....-::y:-/````-NMMMMM
MMMMMMMm/..:sooyo.:--.`:yy+//+y++ssohNMMMMMNs.````/+.....:::y``/````sNMMMMM
MMMMMMMMm/.soos+//+-`./o/o+::/+:+ssyyNMMMMNs````.+/.....-::/o``/---/mMMMMMM
MMMMMMMMMN+-+/--::///++s:::::::/s.`/+dMMMNh.`---:/......:::s:.-..`:mMMMMMMM
MMMMMMMMMMm+.....-:::y:.o::::::oo.-+ohydmm/::-``+/.....-:::y.````/mMMMMMMMM
MMMMMMMMMMMN+......-:+y/o/:::::+o/+os+/+osy:--...o/:---///o/```-sNMMMMMMMMM
MMMMMMMMMMMMm+......-/sy+s/::::/os+/::/oyyhh----:::so//+/o-`.:omMMMMMMMMMMM
MMMMMMMMMMMMMN+...-:/oy/./:+++oyd/::::::/syss+//:-+sy/:::+/++/oNMMMMMMMMMMM
MMMMMMMMMMMMMMNyosyy/oyo:::.:ohsh+:::::::osyoossossoy/::::-..``yNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNy//osos++ssyooo/:::::shy+/++oyooo--...`````.mMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNdhdsoyoos+/oyooooooooyso/--:o:-----.....``yNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNy-/oso/+ydhdddddddhyysoo+::.`````./.....oNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNo.--++shmddhhhhddmmNmdysooo+/-.``.:`````sNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNh/+oosyy+//:::::/+ohmNmh/ooooos/.:`````.dNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNysoos+s+syhhhhhso/:/odNN:-::+ooy+-:```.yNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMmyshy:/-odmmmmmmmmmmmho++hNdo-````+ss+../hNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNyosNNs:`dmmddddddmmmmmNy++mMMmho:-+ooyydNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNooyMMMmymdo//:::/+ohmNNNyomMMMMMMNmoosdNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNhooyMMMMMN+:://///::/omNNmdMMMMMMMMNyooyNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNdooohNMMMMNh/o+///+o+//yNNNMMMMMMMMMMhoosmMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNmo+osmNMMMMMMdy::::/+y++hNNMMMMMMMMMMNs+oshNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNs+osmNMMMMMMMNo:::/+hhdmNMMMMMMMMMMMMNy++oyNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNsoomNMMMMMMMMN/::/odNMMMMMMMMMMMMMMMMNmoooyNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMmosNMMMMMMMMMm/:/yNNMMMMMMMMMMMMMMMMMMMmooyNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNssmNMMMMMMMMd:+dNNMMMMMMMMMMMMMMMMMMMMMhodMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNmyossdMMMMMMMMdsmMMMMMMMMMMMMMMMMMMMMMMMNdoyNMMMMMMMMMMMMM
MMMMMMMMMMMMMMNmhsyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdoooymNMMMMMMMMMMM
MMMMMMMMMMMNNhssdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdddhysyhmNNMMMMMMM
MMMMMMMMMMNNosdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmyssyhNMMMMM
MMMMMMMMMMMNyNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhsdNMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMM
\n\n"""

pidgeot_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-hMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+`-NMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:``yMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+``-NMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-y```sMMMMMMMMMMMMMMM
MMm/:/++ossyhhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/`o.``.mMMMMMMMMMMMMMM
MMmo:......--::::/+oshdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/`-/```/MMMMMMMMMMMMMM
dhhddhyo/-.`...-::://::/ssyhmNMMMMMMMMMMMMMMMMMMMMMMdy``:```.hMMMMMMMMMMMMM
y......------.--....--::///+++oyhmNMMMMMMMMMMMMMMMMMoh-`..```oMMMMMMMMMMMMM
Mmo:.```````...--.......---:://+++osdNMMMMMMMMMMMMMM+:o`````.oMMMMMMMMMMMMM
MMMNmhs/:..`````.----::....----:://+++yMMMMMMMMMMMMMy`/-````-yMMMMMMMMMMMMM
MMs---:::::--....:.......``..-----:/+/+hMMNNMMMMMMMN/-.:```-omMMMMMMMMMMMMM
MMd/-.```````....----.--...``..-----:+/+mMMdymMMMMMM:-`.`..syMMMMMMMMMMMMMM
MMMMNds+:..`````````:--....````.-----:+/o+yddyshmNMM+```./+syMMMMMMMMMMMMMM
MMMMMMMMdyso/:--.```.----.``````.-----/+++::/+so++os/---:++osddddmNMMMMMMMM
MMMMMMMMd:----...----.-:..---.```.-----/+++o/::://:-:://////////////sdNMMMM
MMMMMMMMMNho/-.``````...----......------/++os+/++++++oooossssoooooo+/:+yNMM
MMMMMMMMMMMMMNdhs+/:-...``:-....-..------:/++ossssssssssssyo+oooyy+sys+/odM
MMMMMMMMMMMMMMMMNo+:--.----.-----..-:------:/++oshdmm:o++s+/++shhh-:s+o++hM
MMMMMMMMMMMMMMMMMms:-...``````---...----------:/++ohdo++++//ohhs/-.``-/::/o
MMMMMMMMMMMMMMMMMMMNmmdhyso+/:-..----:::--------::/++++o////+sh/`````///+so
MMMMMMMMMMMMMMMMMMMMMMMMs:--...```.--.---::--------:/+/o+/////os.````-yNNMM
MMMMMMMMMMMMMMMMMMMMMMMMNhysoo++/:----:----:::-------/++o/////++.``./dMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs/-....--.::-::::------///:::::/.`.-sNMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs++syo:---://:/:::/:--..``````````-oMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+/+oo/::/::://:-.`````````````yMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMNhy++++:/::-.`````````````.mMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+os/::--.``````````````/MMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy/oo-----``````````````.dMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN++s:----.````````````.-yMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/o+--::::..````````.-sNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy+s:--/+:/:/-.```.-+hNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNss+-:/o++o/+/..--+dMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhysssys:-++oooooos+++//oMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNdysoossssyysyo++syhdNNs+osyoshMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNdyooosssssyysssyssyyNMMMMMMNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNdyooosssssyyssssyyssyshMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMmsoossssyyssssssyyssyysyNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNddhyysssssyhysssyyssmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNdhyshmdyssyhyyhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

arbok_art = """\n  
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMNmdddddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNdsoooooooooydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNsoooooooooooooohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNysoooooooooooosoooymNNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNdsyooooooooood-oooooosydmNMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNmhyyhsmsooooooooyNysooyhhhhhhyhhdNNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNmhssyyhdosooooooooossoooodooooooossyyydNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNmysyyssooyyoooooosooooossosmooooooooooooooymMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNyossooooosyhdysyhssyssydyshhhhhhyooosyyoooooohNMMMMMMMMMMMM
MMMMMMMMMMMMMMmsooooohhsooshmmhhh+ohhhhyymmhysoosyhdmmmooooooosmNMMMMMMMMMM
MMMMMMMMMMMMMNsooooosmmmmhysodhhh/shhhhsdyosyhdmmdhyyNmoooooooosmNMMMMMMMMM
MMMMMMMMMMMMNdoooooosmdsyhdmdddhh/hhyhyhyhdmmdhyssyoymdoooooooooyNMMMMMMMMM
MMMMMMMMMMMMNyooooooommoyosyhmmdd/yhyyhhmmdysoo+//sodmyooooooooooNMMMMMMMMM
MMMMMMMMMMMMNyooooooodmyoo:/osymmoohysymmhoso/--/sohmdooooooooooomMMMMMMMMM
MMMMMMMMMMMMNmooooooosmmys+/osohmh/yoohmmoooos/osshmdsoooooooooosNMMMMMMMMM
MMMMMMMMMMMMMNdsoooooosdmhyoooohmd:yoosmmhsooossymmhsooooooooooodNMMMMMMMMM
MMMMMMMMMMMMMMMmyoooooooydmdddmmhy/hyooshdmddddmdhsosyooooooooodNMMMMMMMMMM
MMMMMMMMMMMMMMMMNmysooshssssssssso/mmdyssssyyyssssyddsoooooooymNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNmhsoshdddddddsy+mmmmmmddhhhhddmmdsooooosymNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNNNmhssyhmmdhdmyhmmmmmmmmmmmmmdyoooosydmNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNddmMMNmhyysshdmmddmmmmmmmddhysossyhmNNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNysmNMMMMMNdsooosydmmhysssoooosyhmNNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNmysdNMMMMMMMMmsoooooyooooooooosdNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMmhssmNMMMMMMMMMNhooooooooooooooymNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMmhsohNMMMMMMMMMMMNdsssssssssssoosmNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMNhsssdNMMMMMMMMMMMMNyooooooooooossdhhhhhdmNNNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMNyooohNMMMMMMMMMNNNNdoooooooooooooodooossssssshmNMMMMMMMMMMMMMMMMM
MMMMMMMMMhossshNMMNNNmddyysohooooooooooooooodooysoooooooosdNMMMMMMMMMMMMMMM
MMMMMMMMMysooooyhysssssooooyyooooooooooooooohsyooosssssssooyNMMMMMMMMMMMMMM
MMMMMMMMNdoooossooooyoooooodssssssssssssssssyhhysssoooooosssyNNMMMMMMMMMMMM
MMMMMMMMMNyoooyoooooyoooooshoooooooooooooooosyhsoooooooooooosmMMMMMMMMMMMMM
MMMMMMMMMMNdysyoooooyoooooyyooooooooooooooooossosssoooooooooohMMMMMMMMMMMMM
MMMMMMMMMMMMMNmdhyyyyhysyyhdoooooooooooooooooyooooosyoooooooomMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNNNNNNNNNyoooooooooooooooysoooooossooooooyNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNNhsooooooooooosysooooooooyooooohNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdysoooossyysoooooooooysooshNNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdhysooooooooooooshhdNNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmmmmmmmNNNMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

pikachu_art = """\n
oMMMMMMMMMMMMMmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMNMNhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMNdo--NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh+dMMo   
oMMMMMMMMMm+----MMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMNNmMMMMMMMMMNs-``-NMo   
oMMMMMMMMM:..--/MMMMMMMMMMMMMMMMMMMNdhs+:-hMMMNNmmNMMMMMMMmo-`````sMo   
oMMMMMMMMN.....sMMMMMMMMMMMMMMMNds/:-----+NMNNNNNMMMMMMMd+-.......:Mo   
oMMMMMMMMm...-:hdhhhhddmNMMMmy+:--------+NMMNMMMMMMMMMd+--.......--do   
oMMMMMMMMN-..-.-....----::+o:----------oNMMMMMMMMMMMd+-----.--....-oo   
oMMMMMMMNh-......../-+y:------::::+oyhmMMMMMMMMMMMd+----------------o   
oMMMMMMd+-........-dhdm+------:+mNNMMMMMMMMMMMMMmo:----------------:+   
oMMMMMhdyo..-....--:oo/-::/:---:sMMMMMMMMMMMMMNs:---------------:+hmo   
oMMMMm:ys:-:/:::/+....-+//+o/::-:yMMMMMMMMMMMh/--------------/ohNMMMo   
oMMMMd+----:ssssss.---++++oo/:::::dMMMMMMMMMM+:::::------:/odNMMMMMMo   
oMMMMm+o-...:ssysy----:ooooo:::::::mMMMMMMMMMN+::::::::/ohNMMMMMMMMMo   
oMMMMMds+----:so+o--:::://::-::::::+NMMMMMMMMMN+::::/odNMMMMMMMMMMMMo   
oMMMMMMNy/::::://:---::-----://:::--+NMMMMMMMMMNo//oNMMMMMMMMMMMMMMMo   
oMMMMMMNmho/-::::-::::-----////:/----oNMMMMMMMMNy//+dMMMMMMMMMMMMMMMo   
oMmmhs+::-------:---:::::-:+::/:/:-..-odMMMMMmyo++++yMMMMMMMMMMMMMMMo   
os//---....-...------------/--/:::--...-sNMms++++ohmMMMMMMMMMMMMMMMMo   
o+//-----....-.....---------:-----:--....+mMms++yNMMMMMMMMMMMMMMMMMMo   
omdhysso+//::+-......-.......----------...+mMMdsohNMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMN/....-..........-------------/hNmhssymMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMd.....---...---..-------------/ysyhmNMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMM:.....-----------.----------://ydNMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMM+.......-----------......---///hdmMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMMy..--.....----------------:////mMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMMN:---------:::::::::::::://////MMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMMMmo:::::////+osyso+///////////hMMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMMMMMmhso++oymMMMMMMMNdhysss+++oMMMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMMMMMMMMMs+omMMMMMMMMMMMMMMMho+omMMMMMMMMMMMMMMMMMMMMMMo   
oMMMMMMMMMMMMMMMMMMMMMNyoNMMMMMMMMMMMMMMMMho+mMMMMMMMMMMMMMMMMMMMMMMo
\n\n"""

sandslash_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNdhymNMMMMMMNMNmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNNNNdyysymddNMMNmdyyyNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNNMMNmyhdhhyhhyyhNNmhyyssdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNhymNhysydhhhyyssymhhhhyshNNNNmmddddmNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMmymNNmyyhyssssdhyysssyymhhhhyhddhhyyyysydNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMd//odhyhysyyysyysssssyhdhhhhhhhhdhyyyydNNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMd///+hhhyys/yysssssssyhdys+//+ohdhhhhmmmmmNMMMMMMMMMMMMMMMMMMMMMMMM
MMNmhhddd+///ohyho//+dssssssyhs+////+sddhyyyyyyyyhdmdddddmmmNNNMMMMMMMMMMMM
MMMNhyssyy+//o+ys////hysssooy+/////shdhhysssyyhhhhhyyyyysyyyhdNNMMMMMMMMMMM
MMMMNmhysyyss//y////+yy+///////+oshhhhhhyyhhdhhhhhhhhhhhhhmmNMMMMMMMMMMMMMM
MMMMMMNmdysys//s+///+y////oo//+hhhhhhddhhddhhhhhdhhhhhhhddmNNMMMMMMMMMMMMMM
MMMMNdyo+//+s///o//+o//+ymNd-::dhhhhhhysyyyyyhdhhhhhyyyyyyhmNMMMMMMMMMMMMMM
MMMNs++/+///ms+///////o:/NNy-::dhhhhhhyssssyyhhhhhhhhhhdmNNMMMMMMMMMMMMMMMM
MMNo:o.`.+++yyo+//////y:hNh/::odhhhhhhyyyyhhhhhhhhyyyyyyhhddmNNMMMMMMMMMMMM
MN+.+.``.:yohNho//////oo+/:::+hyyhhhhhyyssyhhhhhhhhyyyysssssyyhdNNMMMMMMMMM
Ny`/-``-+dmNMMd-////:---://++h///oh+++++++++oosyhhhhhhyyysyyyhhdNNMMMMMMMMM
N:.o``-sNMMMMMNo::::-:/+//::+y++++h////++++++++++oyhdhhhhddhhdmNNMMMMMMMMMM
m`+:`:hNMMMMMMMNho+oyd+:--/o+/++osh::///////+++++++oydhhhhhdhhhhhNNMMMMMMMM
m-h.:mMMMMMMMMMMMMMMMNy:/o+//////sy..-://///////+++++sdhhhhhhdhhyydNMMMMMMM
NhN+dMMMMMMMMMMMMMMMNmh++///////+oo....:o/////////++++odhhhhyyhdysshmNMMMMM
MMNNMMMMMMMMMMMMMMNho///////////+s/....++///////////+++sdhhyysshmdhyhNMMMMM
MMMMMMMMMMMMMMNmdho//++////////++y-....s/////////////+++dmdyyysshNNNNmMMMMM
MMMMMMMMNmmhs+:-``````.-:s////++s+.....y//////////////++hNNNmdhyymNMMMMMMMM
MMMMNNho/:.```````````.-:y+/++oso.....-y+/////////////++dsymNNNNNNMMMMMMMMM
MMMMMNNdyo++/////////+oo+:ssoshy/::::::+h/////////////+odo+++ydmNNNNMMMMNMM
MMMMMMNdys+++/+++++++/++shdhyyoossoossyyNdo///////////ohs+++////+ooossssyNN
MMMMMMMMMMMMMMMMNNNNNMMMNNmsosssssssso+omMNdy+//////+sysys+++++//++++oydNMM
MMMMMMMMMMMMMMMMMMMMMMMms+o+/+o+++++ooymNMMMMmsoososso+++hhhyyyhhddmNMMMMMM
MMMMMMMMMMMMMMMMMMMMMNy:-/:.-:yosyhdmNMMMMMNmo////++o+++omMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNdyy+/sydNNMMMMMMMMMMNmo.`-so/.-/sshNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNo..-+o/.-:+ydNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNyydmNd/+ydNNNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

arcanine_art = """\n
//////////////////////////////////////////////////////////-////////////////
//////////////////////////////////////////////////-oy+-/:/:dm/:::://///////
//////////////////////////////////////////////////::mNNNms+dNd/oy//////////
//////////////////////////////////////////////////:+NNNNNNNNmddddh-//:::///
//////////////////////////////////////////////-::::oydNNmddddddhyyydds:.`./
//////////////////////////////////////////////::+shs+/o+/+y::/yhNNmhhyh++h:
//////////////////////////////////////////:/+oo++/oys/:++oy++dNNNs::/:::sy-
//////////////////////://///://///////////ohNNNNNmhso++dNmmmNNNd/:::::::s:/
///////////////////:+o+do:/:oy+/////////-/shyymNNhodNNNNNNNNNNh::::::::s://
//////////////////:-dNNNNh+/hNms:/:///:+hdyymNNdddymNNNNNNNNNh...:::::o////
////////////////:/+omNNNNNNNNNNNh/s/:-oNNhsmNNdodmNNNNNNNNNNN-.```:::/o////
//////////////:odmNNNNNNNNNNNNNNNmdooyhNyyhyshshdmNNNNNNNNNNN+so//:::s++///
/////////////:/NNNNNNNNNNNNNNNNNNNN+-/dNNNmoyhhhshNNNNNNNNNNNmoyyyy+-sdy:-/
/////////////:::smNNNmNNNNNNNNNNNNd:odmmmNmodmddysNNNNNNNNNNNNhsyyyy:sd:://
////////////////NNNNdhNNNNNNNNNNNmo+hdddddoyhss/:oNNNNNNNNNNNNNhyyyy/s+:///
//////////////:oNNNmymNNNNNNNNNNNmdy:shdddys:``./hNNNNNNNNNNNmmmmmhyo/:////
//////////////:hNNNodmNNNNNNNNNNNNd://:/o+-`.-::+ooohhmNNNNNNNdddmysyo.////
/////////:/:+shNNNm+ddmNNNNNNNNmdy--::/:.`.:++///:.-+hNNNNNNNNmddmmms-:////
//////////yydmNNNmd+dddmNNNdy+:o+```-++::/++++/-.`:+dNNNNNmmmddddddhy/:////
//////////:-sdhhhhhy+dddmh/.```:+-``.+++++++/-``./shmNNNNNNNNddddho+:/-////
/////-/osdhsdNNmm+//:+hh+/:````.++/-:++++:..`.-/////:omNNNNNmddddh+:://////
//////:/dNNNNNNNNm+://:-+++-````/++++++/-..:/++++//:ommmNNNmNNdddddy+://///
///////++dNNNNNNNNNo:/:`++++-:``/+++++:``./++++++--.o//+dNNNNmdddhdy/-/////
////-/mhdsNNNNNNNNNNhNm::+++++/.:++++++/:-:--hNs.`.:/+::NNNNmddddy-s-://///
////odNh+mNNNNNNNNNNNNNd.+++++++/+++++++/oddhNNNhy/+++/:Nmo/::ddyy-.-//////
::ohdmNysNNNNmNNNNNNNNNN/-++++++/+++/+///++NNNNNNNdo++/-s//.``hy:-/-://////
///::+sdyymNNmmNNNNNNNNNo.-/++++////`.`.-hdNNNNNNNNN+++/://:.`:-///-://////
/////:/ohdo/smmdmNNNNNNNm///+++++//.`..--/+hmNNNNNNNd.:://:::``.:/--///////
/////////+::+ddddmmNNNNNNd+++++++/-://///:/sdmmNNNNNh```-.`:/-``-://///////
/////////::+//sddddmmNNNNNNho++++/-///////:/oyddmmNm//--``.-:::////////////
///////:-/+++///+ydddddmNNNNNNdhho:///////////:/+++s/+++/./-///////////////
//////::+++++///-::+shdddddddddy+://///////////////-/++++//:///////////////
//////-++++/+:/:://:+///+++///::///////////////////-+++++///:://///////////
///////://-/::::///-+++/////::::///////////////////-++++++////:::://///////
///////////////////-+++++/:/::::-//////////////////::/++++++:/::/-:////////
////////////////////::+++++://:/-/////////////////////::++++://-/-:////////
//////////////////////:://:-::-::///////////////////////:::::::/://////////
\n\n"""

alakazam_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+:::/+ymMMMMhso/:sNMMMMmNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM--------./mMy++:::--dNy/:-/mMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMM+--------.-ooo+::---o++/::-+MMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh+MMMMMh/-------//+oo/:---+o++::--mMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo:yMMMMMMM+/////+ooo+o/::--++o+/:--+MMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/-/mMMMMMMMy/::+++++o+o+/:::++oo+/:::hNNMNM
MMMMMMMMMMMNddmNMMMMMMMMMMMMMMM/-:+NMMMMMMMMMNmho++++o+++++oo++++++/oo+//-o
MMMMMMMMMMMNh/::/oydNMMMMMMMMMs:::oMMMMMMMMMMMMMdso+++ooooo++ooo+osmMMMms+d
MMMMMMMMMMMMMMd+--:/+sdNMMMNdh::::sMMMMMMMMMMMMMysssssyyyssso+++ohhNMMMMMMM
MMMMMMMMMMMMMMMMd/---:/+so/:::::::oMMMMMMMMMMMMhyoosyyhhhhhhhhyhhhdMMMMMMMM
MMMMMMMMMMMMMMMMMMh:-::::::::::---/hNmNMMMMMMMmysosyyyyyyyyyhhhdmNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMm:::/::::::::--:/+syyydmMMMdyosyyyyyyyyyhhhdNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMo::/::::::::::/:::--oyyhNMmyssyyyyyyyyhhhhNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMdo::/+/:::::::/::::+syyhs+:-/yyyyyyyyyhhhdNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMmy+::::/+-/:/::+::osyyyyho/::::/osyhhhdmmNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMms/--::::/:::+/:/:+hhhyyhhosshdddmmddhdMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMdyyyyyyyhho:/+:/:+////+yhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNdhhhhho/:+/++++yhhy+:::odMMMMMMMMMmMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNhd/ohms::+hdhyyshddhhhs/::-+hNMMNdyoyNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNmdyyyyhMN:-/ydddddddddddNMh+:::::+/:/++smmMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMmysyyyyhhdMd--/mNmdddddddddNMMNy+/:::://++oyNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMNosyyyhhdNMNo--+NMMmddddddddhNMMMNdyo++osshmMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMNysyyyhhhNh/:::/oMMMmddddddhy+mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMNysyyyhhhdMd/:/++mMMMN/ohhhhy:::yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMyyhhhhhNMMMmyshNMMMN+:++yddds+/::sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMm+-:+ys:sMMMMMMMMMMMh::+ymMMMMMMds::/hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMh-/::/+oMMMMMMMmhhms/+hNMMMMMMMMMMmo+yhhddmMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMNmd/::::/sMMMMMMhyyyhhydMMMMMMMMMMMMMMhhyyyyomMMMMMMMMMMMMMMMMMMMMMMMM
MNs:-:::yNmhhNNMMMMMMyyyyhhhdNMMMMMMMMMMMMmhhyyysssmMMMMMMMMMMMMMMMMMMMMMMM
h--:///+MMMMMMMMMMMMMMhys+++omMMMMMMMMMMMMMdhhyyyo::MMMMMMMMMMMMMMMMMMMMMMM
/////+yNMMMMMMMMMMMMMMMo:::++hMMMMMMMMMMMMMMNdso+:--dMMMMMMMMMMMMMMMMMMMMMM
NdhhmMMMMMMMMMMMMMMMMMM::::++sMMMMMMMMMMMMMMMMo/::--:dMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNNNMMo-:::/++shhMMMMMMMMMMMNyo/:::---sNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMh:/:::/:////ossshyhMMMMMMMMMMMdo/:/:::--/yNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNdoshhmmmmmNMMMMMMMMMMMMMMMMMMMMMmy+/:+yy+:/yMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs+:yMMMds/mMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy:dMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

machamp_art = """\n
MMMMMMMMMMMMMMMMMMNNNdyshdhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNdd+------:---sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMNd:-----/:--:+--+NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMd---o---:+---o--+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMo/--:+---o---o--oNMMMMMMMMMMMMMMMMMMMMMNyhmMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMm+--+/:o//+s++ooshNMMMMMMMMMMMMMMMMMMMNms::-:omMMMMMMMMMMMMMMMMMM
MMMMMMMMMm:---+oo+/so/:::/hNMMMMMMMMMMMMMMMMMMMN+::/:-:-:ymMMMMMMMMMMMMMMMM
MMMMMMMMNo----//o/yNNmmmmNMMMMMMMMMMMMMMMMMMMMMN+o/://:---/dMMMMMMMMMMMMMMM
MMMMMMMMM:----:////NMMMMMMMMMMMMMMMmhmMMNdhdNMMN+:+s:://---/mMMMMMMMMMMMMMM
MMMMMMMMM/-----///ooooymNMMMMMMMMMNs+ommyo++mMMNmdysos:-----+mMMMMMMMMMMMMM
MMMMMMMMNh/---:///+/////yNMNNNMMMMNso+y++o++mdysdMMNmhysso/--:yNMMMMMMMMMMM
MMMMMMMMMMmy/-////o+/////yo+++oydNh:/oo+:o+s+yosmMMMMMMMN+/+---omMMMMMMMMMM
MMMMMMMMMMMMmo:::::++://///////:++/::+s+-soosoyNMMMMMMMMm:-/---:omMMMMMMMMM
MMMMMMMMMMMMMNds/////+//++++o++:/./:-oh/:yosssmmmNMNhsosh:-----:/hMMMMMMMMM
MMMMMMMMMMMMMMmh+::::----:--:o--+`++/-:://ysos++++h/-----//:---:/hMMMMMMMMM
MMMMMMMMMMMMMd:----:/----o---//-+.++++:--:/::o//:-:----:/+////sydNMMMMMMMMM
MMMMMMMMMMMMNy--+---+----+/---o-:/::://++oo+/+/++----:+o+///+dNMMMMMMMMMMMM
MMMMMMMMMMMNoo--o---+----:o--:s:-:::::::/+//+/:-/o//+///++/smMMMMMMMMMMMMMM
MMMMMMMMMMNh-o--o---o/:://s++s/------::/+///+o/::s//:/:--:hNMMMMMMMMMMMMMMM
MMMMMMMMMMNh-/+/os+/ss++////+s:----:/-://////+/+os+o:-:::-+NMMMMMMMMMMMMMMM
MMMMMMMMMMMNs-:/+oosyy+++++oo+:-::/+:://///+y+//+:+o+/:::-:mMMMMMMMMMMMMMMM
MMMMMMMMMMMMNdhddhhdNNh////++o+//+o/////++ymm:::/++oso+//-/mMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNNmdyyso++os++/+++oshmNMMNo---+o+ooo++sdNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNmy+//+yddho/oo+syhdmNMMMMMMNms:-o--/////hNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMdo:------+mmdsssyddysymNMMMMMMMMmyo--:////sNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNs:-------:+hmmmmmyo//:::+yNNMMMMMMMNy/-://smMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMNs-------:+o/dNNNmo//++-----/hNMMMMMMMMmysydMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMN:----:/+++odNMMMNy/:::--:----yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMN/---////+osdMMMMMNy:----+:----dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMdso+//////+hMMMMMMMNhs/:-:----oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNy//++//sNMMMMMMMMMy/-+:-----/NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMd+--/--:+NMMMMMMMMMM+:++:----:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMN+:/sy--:hMMMMMMMMMMNm//////odmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNNNN+:+yNMMMMMMMMMNdo:////yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNmNNMMMMMMMMMMN/--:///hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyo/-://+sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/-:/+s//hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyoomNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

victreebell_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMNhs+/+syhdddddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMd+/++++/::::::://+oshdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNmdddm+o+:::::::::::://///::/ohNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNds+:::::os/::::::::::://oyshddhhhyydMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMms/:::::::::+::::::::://///oNdyhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMmo/::/:::::::+:::::::///////+mMMMmhhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMy/////::::::::+/://////////oy//sNMMMmyhNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMNo//+sy::::::::://///////+shmNNd+:/dMMMNdydMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMNo+ymNMNs+/:::::::////+shmNMMMMMMN/::NMMMMmyhNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMddNMMMMMMNNmdhs++////yNMMMMMMMMMMMy::hMMMMMNhsmMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMy/+mhodMMMMMMMMMMMMMy::dMMMMMMMdsdMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMM+/+MMMMMMMMMMNmmdddd/:/mMMMMMMMMdsdMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMd//yMMMMMMMMNmdy:shh/-:++NMMMMMMMMdsdMMMMMMMMMMMMMMMMMMMM
MMMMMMMMNmmmmmhhdms//doyMMMMMNdddd//+:-/+:-+NMMMMMMMMhsmMMNNmdhyyssooossyhN
MMMMMNhs+////:/://o-/o-yMMMMMNdhys/:://o:--./mMMMMMMMmsss+//:://///+///ohmN
MMMMmossso+//::::/+/:--/ossoo//::/:/+:./--...:hMMMNho/::::::////::::/smMMMM
MMMMsydmmNy++//////oo++//+/://ssos/:--::-....:/sNy/:::::///::::::::/dMMMMMM
MMMMNMMMMMN+++++++++oo++++s:-:/-------.......-:o/::::///::::::::::/dMMMMMMM
MMMMMMMMMMMs+++++++++oo+++o/-............-....+/::/++/::::::::::::sMMMMMMMM
MMMMMMMMMMMs++++++++++s++++/............-/:...o//++/:::::::::::::/mMMMMMMMM
MMMMMMMMMMMo+++++++++++s++o:......`````.......o/o+/::::::::::::::/MMMMMMMMM
mMMMMMMMMMM++++++++++++s+s+:...........`....../s//:::::::::::::::oMMMMMMMMM
oyNMMMMMMMM++++++++++++os:/.```````.//:```....+//:::::::::::::::/dMMMMMMMMM
o-+hNMMMMMMy+++++++++++o-`.````````.//:.``...////::::::::::::::/sMMMMMMMMMM
h:::+shNMMMNs+++++++++o-````````````.-.`.....o/////:::::::::///oMMMMMMMMMMM
N+//////sNMMMh+++++++++````````.-.``````....-s///////://:::///yNMMMMMMMMMMM
Md///////+MMMMNyo+++++/```````://-`.......---/+/////////////odMMMMMMMMMMMMM
MMms+////sMMMMMMMNdhhh+```````.-.``....-------+s+////////+ymMMMMMMMMMMMMMMM
MMMMNmdmNNmmmNMMMMMMMMd.............----------+/yNmddddmNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNmmmmmmmmmy::-.....-----/:-------+dMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNNNNNy/---------::-----:odMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMmhs+/::--:://oydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

tenracruel_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmho+++++oosydmmmNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMmdyyyyyys+/////+oyyyhhhhhhhdNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMmhhs/---:+/////////::/oyyyhhhhhhmMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMhhhyo:---////::::///--:osyyyhhhhhhdMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMhhhhs+/::////:::::::///osyyyyyhhhhhhdMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMmhhhy+--/////:::::::://osyyyyyyyyyyhhyNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMhhhyyy+///+/+++ss////////oyyyyyyyyyyhhmMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMdhhyo+/////+y+oyys::://////osyyysssyhhyNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNsso+////////oosoo/:::////////++ooosyysosdNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNmho+++////////:://::::::::::///////++++oooooshNMMMMMMMMMM
MMMMMMMMMMMMMMmhso+++///////////::/::::::::::::::://///+++++++++oshmNMMMMMM
MMMMMMMMMMMMNso++++/////++++///:::/:::::::///////:::://///++++++++++shMMMMM
MMMMMMMMMMMMNysyyoooossyyddy/++/::/::://+++///+ysoo++///++++ooooo+ooosNMMMM
MMMMMMMMMMMMMMMMMNNNNNNMMMNmh+oo++//+oys++o:/omMMNNNdssshhhddmmdddhhhmMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNdysdmdmmdh++hNNmmmmmNMMMNhyysssydmNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNMMMMMMMMMdsoossssydds/+osymMmyssNNhsoosysosyysydNMMMMMMMMMMMM
MMMMMMNmdysyssyyydmNNNyoooooosshmo//+oooymhss+ohyoos+sdyosdmhysymNMMMMMMMMM
MMMMdyo++oosyyyyysssssooooooosdMd//+oooyNNdooo++yoodhoohhsoymNmysymMMMMMMMM
MMms//+osydNMMMMNNdooshhhhs+ymMh//++oooyMMMsooo++++yMms+shhoohdhoooyhdmNMMM
My+:/+osdNMMMMMMMdoo+smhsosdMMm+///+oyosMMMyoooos++odmmh++soooooooo++/+ohNM
h+/:+osNMMMMMMMNy+os+ooshmMMMMh+//+oyNsoNMMdoooyNdsooooossssyysoyyso+/::/oh
s+/+oshMMMMMMNms+ooo+ymMMMMMMMy+//+odMy+dMMmo+ohMMNoodmmmNy/dMd+yNdsso+//os
sooosyNMMMNdyo++sydd+sMMMMMMMMy+//+oMMd+sMMMo+ohMMMs+dMMMMN+oNMs+dNsosssssy
dyyyymMMMdo++o/omMMNo+dMMMMMMMy+//+yMMm++mMMy+omMMMs/yMMMMMo+mMd+sNsssymmmN
MMNNMMMMdo+oss/omMMMy/omMMMMMMy+/+ohMMMo/sMMh+oNMMNo/sMMMMMo/hMm+odmyymMMMM
MMMMMMMMNddmNs/+hMMMmo/ohNMMMMmo+oodMMMs/odMm+sMMMh++sMMMMm++hMdooyMMMMMMMM
MMMMMMMMMMMMMh+/+hNMMdo+/+ydNMMsooomMMMy++sNNohMNh++ohMMMMs/odNs+osMMMMMMMM
MMMMMMMMMMMMMNs+/+sdMMmyo+/+smMdooodMMMdo/+yNyNNs/+oyNMMMh//smy++oyMMMMMMMM
MMMMMMMMMMMMMMmyo/+sMMMMmhysyNMMsooNMMMMyo/oyMMNsoshNMMNy//oymo+osdMMMMMMMM
MMMMMMMMMMMMMMMMdyshMMMMMMMMMMMMNsoNMMMMMdsydMMMNNMMMMNs//osmMdhdmMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhMMMMMMMMMMMMMMMMMMMs//osmMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMyosyNMMMMMMMMMMMMMMMM
\n\n"""

golem_art = """\n
hhhhhhhhmdNNNNmNmmNdhmmmNNNNdhysoooshmNmmmNmNNNNmNNmNdmmmyyyyyyyyyyyyyyyyyy
hhhhhhhhmdNNNNmNmmNdhmmdyo/-----------/smmNNNmmmmNNmNdmmmyyyyyyyyyyyyyyyyyy
hhhhhhhhmdNNNNmNmmNmdh+/:::--------------/ydhhh-:ohmNdmmmyyyyyyyyyyyyyyyyyy
hhhhhhhhmdNNNNmNmNNMMo///:::::-------------:yhhy/--:sdNmmyyyyyyyyyyyyyyyyyy
hhhhhhhhmdNNNNNMNNNMMs:///:::::::------------hyyhs:---+hmyyyyyyyyyyyyyyyyyy
hhhhhhhhmmmhhhhddNNMMNyo+/:::::::::---------/dmyyyhs/---+hhyyyyyyyyyyyyyyyy
hhhhhhhmdhhyyhhhyNNMMMNNNmdhyo+/::::::---/ohddNhhyyhhy+:--sdyyyyyyyyyyyyyyy
dddddmmhhhhyyhhhmNNMMMNNNNNNNNNNmmdhyyyyhddmmNdo/---:/shyo/smdddddddddddddd
mmmmmNhyyhhhhhhdNNNNMMNNmhyysssyhdNNNNmdmmNNh+:--------/ydyyNdddddddddddddd
yyydmNdddhddddmNMNNNNNmso+++++/////oyhNmmmmy:::::--------+dhNNNysssssssssss
sydNMmdddddmNNNmmmmNNNyso++++++////:::+mdddd/:::::--------odyyhdyyyyyyyyyyy
dNNmNNmddmNNmmmmmmdNMmssoo+++++////:::/sNmddh::::::--------h/:/+mmmmmmmmmmm
mNmmmMMNNmdddmddmmdNMhsysooo+++++///://+NNNmNo:::::::------/y:::smddddddddd
NmmmmNMNddhddmmmmdmMMsyyyssoo+oo+++///++hMNNNmo+++++++++///:d::::hddddddddd
NmmmmNMdhddddmmmmmmmmyyyyyyssooooo++++++oMMNNNdhs::::-.---/oy+/:/dmdddddddd
NmmmmMNhhddddmmho/:--:+yhyyyyssooo++++++sNNMms++s/:---.`````.-/ohmmmmmmmmmm
NmmmNMNmdddmNNy:---...../yhyhyssooooo++omNNh+++//+h///:-.``````.shhdhhhhhhh
NmmNMNMMMMMMMhos+:--....../hhhhyysssssymNNh++++///y.`.hy/-...```.h:sdhhhhhh
dmNMmmmNMMNNNyoooss/:......-smdhhhyyhmNNNmoo+++///+s/:dhd+-----.-d/-/mddddd
hdNNmmmmNMNNNmyoooosso/-..:/:syhmNNNMNNNNNsooo+++///+oosyho------ds:.+mdddd
mmmmmmmmmNMNNNNmysoooosso+:...../ohmNMMMMMNyooosysso++//++oo:----yss/-ddddh
mmmNmmmmmNMNNNNNNmdysoood/--:/-.-:/++yMMMMMNdysooosssyyo++ooo+/::/myo/+ydhy
mmmmNmmmmmNMNmddhhdmmmdym+::/sds/::/y/NNNNNmmNmmddysoooyyy+yo++++odoo+:-/sh
ddddNmmmmmms/:------/yNNNmy/-/dMdh:`o-mmmmmmmmmmmmmmdhysossyyysyydo+yds:-od
hhhhhmNNNm+:-------...+NMMMh/:oNMNh+ydNmmmmmmmmmmmddhhddsyyyyhdddmo+smmo+sm
yyyyyyNNNo+:--------..-dMMMMmds+MMMMMmmmmmmmmmmmmdhyyhm/-:/mmNmdhddoymmy+mm
mmmmmmNNN++:----------.oMMMMMMMNMMMMMNmmmNmmmNmmmhyyhd/----+Nmmmdddmdhhdhhh
mmmmmmmmNs+/-------.---/NNNNNNNNNMMMMMmmmmmmmmmmmdhddo+/::::NmmmmmmNdysdhss
mmmmmmmmNyo+:------..--oNNNNNNNNNNNMMMMNmmmmdmNmmhysooooooooNmmmmmmNdysdhss
ddddddddmooo+/----...:/mNNNNNNNNNmmmNMNNNNmNNNNyooooooooooosNmmmmmmNdysdhss
dddddddmyooooso:::-/yodmNNNNNNNNNmNNNNmNNMNNNmmN+ooooooooooyNmmNNNNNmssyyss
ddddddmd++oooosoooos+ddhmNNNNmNNNmNNNNmmmmdmNmddoooooooooo+ooshdNNNNmssssss
mmmmmmNs+oooooo+++++oNNNNNNNNmNNNmNNNNdddddNmysdsssssooo++//++syo+shNyyyyyy
dddddmdoooooo++++++/smddhhddmmNNNmNNNNdddddNNNNNNNmmmmdhyo+soh/:/+syNdddddd
dddddms:+oso/soy::ss.`ohhhhhhhdmNmNNNNdddddNNNNNNNNNmNNNNNNdo/+NmddNNhhhhhh
mmmmmN+`-ms.`-N:. /ms+:omdddddddmmNNNNdddddNNNNNNNNNmNNNNNNNmNNmNNNNMhhhhhh
hhhhhhh/ydh-`.Nds..NmNNNNmmmmmmmmmmmNNdddddNNNNNNNNNmNNNNNNNmNNNNNNNMhhhhhh
sssssssNmhymsydhhNhdddmmNmmmmmmmmmmmNNdddddNNNNNNNNNmNNNNNNNmNNNNNNNMhhhhhh
\n\n"""

gengar_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNymMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms/odMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms//+smMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo///+ssmMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo////+sssNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMdhdNNMMMMMMMMMMMMMmNMMMdso/////osssMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMdyhddddmNNMMNdMNdhmMdyss+/+o+osssyMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMmdhhhhhhhhdyyyyyyyysssooossosssshMMMMMMMMMMMNMMM
MMMMMMMMMMMMMMMMMMMMMMMmmmNNdhyyssssooo++++++oooossssssssssdMMMMMMMNmhsmMMM
MNmmmmmmmmmmmmmmmNNNNNNmdhyysssso++///////////////++oosssssmMMMMdyo+osssosm
Mdsoo+++++++++++++++++sssssssso+/////////////////////osyyssNNmy++/+ossssdMM
MMNdyssoo+++///////++ossssssso///////////////////////+ossyyhyo+++osssssyymM
MMMMNmysssssoo++//++ossssssss/////////////////////////+ossssssoossssssdNMMM
MMMMMMMmhssssssssoo+osssssssso//////////////////////+//+ossssssssssssdMMMMM
MMMMMMMMMNdysssssssssssssssssso+///////////////////oosssssssssssssssdMMMMMM
MMMMMMMMMMMNmysssssssssssssssssso++///////////////o+-/sssssssssssssdMMMMMMM
MMMMMMMMMMMMMMNhyssssssssssssssssssoo++/////+o+/+oo:--:ysssssssssymMMMMMMMM
MMMMMMMMMMMMMMMMNdhsssssssssssssssssoossoooossoosh/----yssssssssssdMMMMMMMM
MMMMMMMMMMMMMNNNNNmssssssssso//+ssss+/+sssssssssso+:.-+ssssysssso++NMMMMMMM
MMMMmdhyhhyyyyyyysyssssssssss///:/+so+ossssssssso//++sssss:ossss+//hMMMMMMM
MMNmysssssssssssssysssssssssso//---:+/+sssssssssssssssss+-`+sss+///sMMMMMMM
MMNhhssssssssssssssssssssssssss+/:::::+sssssssssssssso++.``osso////oMMMMMMM
MMMMMyyyyssssssssssssssssssssssssssssssssssssssssss/-.`.:`/ssso////oMMMMMMM
MMMMMNMMNNdhyssssssssssssssssyoossssssssssssoo+/--/`````//ssss+////oMMMMMMM
MMMMMMMMMMMMMNmmdhhyyssssssssso---+::::::+--.`````--``.-osssss+////yMMMMMMM
MMMMMMMMMMMMMMMMMMNNNdhyysssssso:`.-`````--````````/.:osssssyy+///+dmMMMMMM
MMMMMMMMMMMMMMMMMMMMMMdhhhhhhhhhhs/+.`````/`````.-/ssyyyyhhhhho///shhmMMMMM
MMMMMMMMMMMMMMMMMMMMMMNdhhhhhhhhhhhdyso+//o++osshdhhhhhhhhhhhhy//oysssMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhosyssssMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMddhyssoosyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhysssshMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMds////////+oyhhhhhhhhhhhhhhhhhhhhhddhhssssyNMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNss+//////////ohhhhhhhhhhhhhhhhhddddhhhhyhdMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMmsso+/////////oshhhhhhhhhhhhhhddNmdddhhdNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMmsssssoo++++oossshhhhhhhhddddmNMMNmddmdMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMysssssssssssssshmmddddddmNMMMMMMMMNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMmsssshhyyhssssmMMMNdhddNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMmyhhdhddhdssmMMMMMNmNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhhhhhhhymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmddddNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

eevee_art = """\n
MMMMMMMMhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMs+sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMmyNyoNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMhdddyodMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMyddhdh+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMhhhdhhh+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMmyhhhhhh+mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMsdhhhhhyoMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMhymdhhdmohMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmddhyyNMMMMMMMMMMMM
MMMMMMMMMyhNmdmMhoMMmMm+dNMh/mMMMMMMMMMMMMMMMNmdhyyyysyhhdhohNMMMMMMMMMMMMM
MMMMMMMMMMyyNNNMN+Nmo+s//++o:/hdyMNMMMMMMNdysyhhhhhhdddddyymMMMMMMMMMMMMMMM
MMMMMMMMMMMdsmMMN+yo/////////////ooNMMMmyshmNNmdhhhhhhhyydMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMNyhho++//////////////+++dmyymNMMNmdhhhhhhssdNMMMMMMMmydMMMMMMMM
MMMMMMMMMMMMMMmy++++///////////+++++oshNMMMMNNNmmdhsydNMMMMMMMNy:-:MMMMMMMM
MMMMMMMMMMMMMMN++++o++++++++++++++++++yNNNmmmdhyyyhNMMMMMMMNds:----hMMMMMMM
MMMMMMMMMMMMMMh++y/dso++++++++++++++++oyhhhhhdmmNMMMNNmdyo/:-------sMMMMMMM
MMMMMMMMMMMMMMs+yMhMy++++++++++ooys+++omMMMMMMMNmhysso+///:::/:----oMMMMMMM
MMMMMMMMMMMMMMo+dNMNs+++++++++sN+hm+++sMMMMMNdysoooooooooooooo/----yMMMMMMM
MMMMMMMMMMMMMN++shdh++++++++++NMMNN++omMMMMmyooooooooooooooooo/----hMMMMMMM
MMMMMMMMMMNh+y+++oo++++++++++ommNdh+oyMMMMNsoooooooooooooooooo:-:-:NMMMMMMM
MMMMMMMMNs-../oo+++++++oo+++++syhyooosshNMhsoooooooooooooooooo/oo/sMMMMMMMM
MMMMMMMMy.``..-/oo++++++o+oo++++++ooo:--/hyysooooooooooooooooossssNMMMMMMMM
MMMMMMMN.``.....:/++oo++++++++ooooo+::::-:oyyssssoooooooooossssyydMMMMMMMMM
MMMMMMMy-```........:/++oooooo++o/::::::::oyyyyyysssssssssssyyyydMMMMMMMMMM
MMMMMMMdo-...-.``.-....--::::::::/::::::::+osyyyyyyyyssyyyyyyyydMMMMMMMMMMM
MMMMMMMMms-..:```...........-:/:::/::::::sssooyyyyyyyyyyyyyyydNMMMMMMMMMMMM
MMMMMMMMMMd+::`.-.````````...::+::o:::::ooooooohyyyyyyyyyyhdNMMMMMMMMMMMMMM
MMMMMMMMMMMMmy--::.....`````.::+:/+:::/oooooooohmdddddmmNNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMh/-+---..-....-:+//o/++ooooooooooyMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNs/+:::::---::/++sssoooooooooooohMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMmoss+:--::/ooooooyoosymo++++ooodMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMyoooo++yooosoooohyhydMm+++++++mMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNoooossso+oooooyhyyymMMy++++++MMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMy+++++s++++++ohyyhmMMMo+++++dMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMd+++++s++++++syyhNMMNs+++++hMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNo////o+//+++smdmMMMMoo++++yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNhoo/+o/////oNMMMMMMMNmhdhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNMNhsssymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

lapras_art = """\n
MMMMMMMMMMMMdyyyyhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMN+sssssyhyMNmmmmNNddddmhssNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMM+:://osyhsosssysssooooossdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMm---:-:osyosssssssoo++osyyyNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMd---:::osossso++++++osyyosdhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMM:--:-/sssssssyyysssyyyshsymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMNss-:osssoososysyyyyyyshhyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM--/ossshN.oooyyyyyyyyyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM:-:+ssssd-h-osyyyyyyhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM/:oyhyssso/osyyyyyyyyhhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM:+dmhysoossssssyyyyyyhhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMoommmyyyyo+++oossysyyyyNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMyodmmdyyyyo/o+o+/+ossyyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMhohmmmmdyso::MNddhhddyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMdsydmmmmmdo::yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMmsyhmmNNmmdso+NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMdsyhmmmmmmmsssyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMdsyydmmmmmmyssyhMMMMmdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMdsyyhmmmNNmhsssydMMMMohyMMMMMMMMMMMMMMmmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMmsyyhmmNNNNmsssssmMMMMssdhMMMMMmmNMMMMhohyMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMNoyyydmNNmNmyssssodMMMMhoydhmddhhdhdddsoymyMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMssyyhmmmmNNdssssssosddddmmmmmmdmmhhyysoshmydmNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMhssyydmmmmNmyssssss+yhddddddddddddmdyhdddddhmmdydMMMMMMMMMMMMMMMMMMMMMMMM
MmossyydmmmmNdsssso++/ohhhhhdhhhyyysoosshsdddddmmmdhddydMMMMMMMMMMMMMMMMMMM
MssssyydmmmmNysssss+//-/+oyhyyhyso+ooosydyddddddhyssshhyNMMMMMMMMMMMMMMMMMM
mosssyydmmmNmsssssssoo++///+syyyhhs+ooshyhhdddddhyoshyymMMMMMMMMMMMMMMMMMMM
sssssyyhmmmmdsssssso+ssssso+/+syyhhhssyhyhhhhhhhdhhhyhdhdMMMMMMMMMMMMMMMMMM
ossssyyymmmmhsssssssssssssyss+/oyyyhhhhhhhhhhhhhhhhhhhhhhmMMMMMMMMMMMMMMMMM
+sssssyyhmmmhssssssssssssyhhsso++oyyyhyyyyhhhhhhhhhhhhhhhyNMMMMMMMMMMMMMMMM
ossssyyyyhmmdsssssssssssssyysssso/+oyyyyyyyhhhyyyhhhyyyhhhydMMMMMMMMMMMMMMM
osssssyyyyhdmyssssssssssssssssssss+//+osyyyyyyyyyysssssssooyhMMMMMMMMMMMMMM
yossssssyyyyhdssssssssssssssssssssss+//---:///////osyyyhhddyohmMMMMMMMMMMMM
N+ooossssyyyyyhsssssssssyyysosssssssoo++/:://////ossssssyyyddhsoyNMMMMMMMMM
N:oooosssssyyyyy+sssssssyyhhhyosssssoo+++////////osssssssssyhhds+/mMMMMMMMM
y.:oooossssssyyo+sssssssshhyhhhoooooo++///////://+sssssssssshhyhhdMMMMMMMMM
/..:ooooosssssso/ossssssssssyyhds/+////////:/+::::+ossssssssssssyyyMMMMMMMM
/..-++ooooooosso:/ooossssssssyyyhs:::://+oosoyo::::/oooooooooooossysNMMMMMM
h.../o+++ooooooo::/+ooooosssssssyhsosssosyhmMMNs/:--:/+oooooooooooosohMMMMM
My.../oooo+++/oo+--:/ooooooooooosshsomNMMMMMMMMMmy+:---:/+oooooooooooosNMMM
MMm+..-+oo+oo+omMm---:+oooooooooooosssNMMMMMMMMMMMMmhs/::--:/++oooooooooyNM
MMMMNs:.-/+oooo+odMy---:/ooooooooooossoymMMMMMMMMMMMMMMNdhs+/::::::://////s
MMMMMMMNho/::++oo+sdNs:---:/+oooooooooooooydmMMMMMMMMMMMMMMMMMNmddhhyyyyyhm
MMMMMMMMMMMMNdhyyyyssNMds/----:/++oooooooooo++osNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMmhso+/::::::///+osyhNMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

steelix_art = """\n
ddddddddddddddddddddddddddddddddddddddddddddddds-hddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddd+`/dddddddddddddddddddddddddd
ddddddddddddddddddddddddddddddddddddddddddddh:`.hdddddddddddddddddddddddddd
ddddddddddddddddddddddddddddddddddddddddddds...+ddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddd+....hddddddddddddddddddddddddddd
ddddddddddddddddddddddddddddddddddddddddy-....+dddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddhs+/::-...-ydddddddddddddddddddddddddddd
ddddddddddddddddddddddddddddhddddo:-::----..--odddddddddddddddddddddddddddd
ddddddddddddddddddddddddho/:--:+so/:------:----odhys+/+osyddddddddddddddddd
ddddddddddddddddddddddh:--------/+++------:----+o+++++---::+hdddddddddddddd
ysyhdddddddddddddddddd/--:------/++++:://++/:/ooo++++++:--:--sddhsydddddddd
d+---/+oyhdddddddddddo----:/:::/oo+++o++++++ooo++o+oooo+/--:-+dy++:yddddddd
ddhs/-----:+oyddddddd/:--:+++++o+ooooo++++++oo+++o+++++++---:--://-:ddddddd
dddddy+:-------/oyyyso+++o++++++o+oo++oo+++osyoooo++/-------:-----:-+hddddd
dddddddds/-----::-::-:+ooooo++oooso+++++yhddddho//-----------::---:---oyhhd
ddddddddddho/-:----::-:ooooosooooo++++ohdddddds/--------------:--:/-------o
dddddddddddddy+:-:::::-::/oososhdo+++ohdddddddso/-------/+:---:---/-------/
ddddddddddddddo+o+++++o++++oooodh+++sdddddddddhso/---:/::+o:--:---/---:-/oy
ddddddddddddddo+o+++++oo+++++oohs+ohdddddddddddddhy:-::::/hs--:---:---:-hdd
ddddddddddddddyo+oooooooo+++o++o+ohddddddddddddddddh:---://+o--:--:---::ddd
dddddddddddddddho+o+++++oooo+++oo++oyhddddddddddddddy---//:-:/-:--:--/-+ddd
dddddddddddddddddyooooooooo+oooo++++++s+-.-ohdddddddds----::-:/:---/:/-oddd
ddddddddddddddddddsoooo+++++oooos/+++++++//:/oyyyyyhddy:-----:-:----:--hddd
ddddddddddddddddddhsoo++ooo+++++o-:/::/+oooo++o++++-/sdh/------:::::--odddd
dddddddddddddddddddhso++++o+++oo+:++++//oooo++oooo+---:ohy/-------..-oddddd
dddddddddddddddddddddhhysooooo+++o++ooo+ooooosooooo+/::--+hhyo+//++shmmmmmm
ddddddddddddddddddddddddydddhysooo+o++++++oydddysooooooo+//odddddddddmmmmmm
ddddddddddddddddddddddddydddddyddddhyso+++++yddddddddddddddddmmddddddmmmmmm
ddddddddddddddddddddddddydddddyddddddddhyso++oyddddddddddddddmmddddddmmmmmm
ddddddddddddddddddddddddydddddyddddddddddddhysoydddddddddddddmmddddddmmmmmm
\n\n"""

houndoom_art = """\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNyo//+oymMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+/---::::+dMMMMMMNdyo+/+oymMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd///::+:---/sNMMdo-------.../mMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs///:/+:-/+yhds:------::--..-mMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNh+///syooooyy+::::+hNNMNs--.+MMMMM
MMMMMNNmmddmmmmdmmmNNMMMNMMMMMMMMMMMMMMMMMmy+yysooooyyyyssyNMMMMMM+--/MMMMM
MMMNmmNNMMMMMMMMMMNNmmmmddNMMMMMMMMMMMMMMMMMmhys//syyssyyyyNMMMMMMo//yMMMMM
MNdmMMMMMMMMMMMMMMMMMMNmdddmMMMMMMMMMMMMMMMMNhy+//ohyosyyyyNMMMMMh+/sMMMMMM
NdNMMMMMMMMMMMMMMMMMMMmddddddNMMMMMMMMMMMMMMNh+////+yyyyyyyNMMmh++smMMMMMMM
dmMMMMMMMMMMMMMMMMMMMMMMNNmdddNMMMMMMMMMMMMmo////++oossyyyhMMNddmNMMMMMMMMM
dmMMMMMMMMMMMMMMMMMMMMMMMMMMNmmNMMMMMMMMMMMmdyyossyssyshyydMMMMMMMMMMMMMMMM
mdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhsoosyyhyyymMMMMMMMMMMMMMMMM
NdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmh///syyhyyhNMMMMMMMMMMMMMMMM
MMmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNh+hy:/+yohyyyydMMMMMMMMMMMMMMMM
MMMNmdmNMMMMMMMMMMMMMMMMMMMdysshmNmmmNNdhydo--hhsoysyyyyy+-sMMMMMMMMMMMMMMM
MMMMMMNmmmmNNNMMMMMMMMMMNmo/://++///++:::/o-.-hhhyyyyyyyy:.`dMMMMMMMMMMMMMM
MMMMMMMMMNNNmmNNNNNNmmmdhs//+ss++oso//+sssy/--oyyyyyyyyyy/-.dMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNdhhhhy+shysoyyy+/syyyyyy/::syyyyyyyyy/-oMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNhsyhhhhshhhyohhh/syyyyyyyys++syy+::yys+hNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNyssyhhhhhhhhhhhhhshyyyyyyyyyyyyyds-:hyydMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMhsyyhhhhhhhhhhhhhhyyyyyyyyyyyyyyyys:shyyhMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNhyhhhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyssyyhyymMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMmhhhhhhhhhdhhhyyyyhhhhyyyyyyyyyyyyyyyyyyyshMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMmhhhhhhhhdmNmmmmmdhyssyhyyyyysyyyhyyyhhyysosNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMmhhhhhhhhmNMMmmmmmmm+-/shyyyyssyyhsooyhyyysoohMMMMMMMMMMMMMMM
MMMMMMMMMMMMMmdhhhhhhdNMMMMmmmmmm+   -yyyyysoyyhyhdhhyyyysssMMMMMMMMMMMMMMM
MMMMMMMMMMMNdddddddmNMMMMMMmmmmmd`   -yyyyyssydMMMNmdyyyyyysmMMMMMMMMMMMMMM
MMMMMMMMMMNdddddNNMMMMMMMMMmmmmms    :yyyysyydMMMMMMMmhyyyyyhMMMMMMMMMMMMMM
MMMMMMMMMMNddddmMMMMMMMMMMMMNmmmmo`` oyyyyyydMMMMMMMMMNdyyyyymMMMMMMMMMMMMM
MMMMMMMMMdhhhhhmMMMMMMMMMMMMMMmmmmhy:hhyyyhmMMMMMMMMMMMMmhyyyydMMMMMMMMMMMM
MMMMMMMMMo++/:-+MMMMMMMMMMMMMMNdhyyydhhhhhNMMMMMMMMMMMMMMNmhyyyhNMMMMMMMMMM
MMMMMMMMMsoo+//hMMMMMMMMMMMMMMMNdysyhhhhhNMMMMMMMMMMMMMMMMMNdyyyyysdMMMMMMM
MMMMMMMMNo++:--hMMMMMMMMMMMMMMMMMNmmhhhhhMMMMMMMMMMMMMMMMMMMNo+/-..-mMMMMMM
MMMMMMMMMmhyyyymMMMMMMMMMMMMMMMMMMdyyyyyysNMMMMMMMMMMMMMMMMMMh++/:::oNMMMMM
MMMMMMMMNdddddhdddMMMMMMMMMMMMMMMMs::-....mMMMMMMMMMMMMMMMMMMMy::-...sMMMMM
MMMMMMMMMNNmyddhmdNMMMMMMMMMMMMMMMm///::::dMMMMMMMMMMMMMMMMMMMMNhyyyyhmNMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+:-....hMMMMMMMMMMMMMMMMMMMMMNdhyyyhyymM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyyyhhhhhdMMMMMMMMMMMMMMMMMMMMNdhysdodd
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhyyyhyyhsdMMMMMMMMMMMMMMMMMMMMMMNmNmdM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmdoddodNmMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

sylveon_art = """\n

MMMMMMMMMMMMMMMMMMm+:yMMMmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMd-.-:s/--hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNm--:-...:dNmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMm:+/:::-.-:----/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMs:::::++:---/sdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMy````-:/++/dNMMMMMMMMMMMMMMMMmhs+:-:MMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMN/`    ./+/::MMMMMMMMMMMMMMNdo:--...-sMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMN:    `:oo+:::MMMMMMMMMMMMms/:-------sMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMM+   `::+oo+::/MMMMMMMMMMmo::::::::::hMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMM-  `+::+ooo//sMMNs+mMMNy::/+oo::::/+MMMMMMMMMMMMMNdhyNMMMMMMMMMMM
MMMMMMMMMMh` :/::+ooo//dMm-  .mN+:/oooo::::/omMMMMMMMMMNdy+:--omNMMMMMMMMMM
MMMMMMMMMMMms+:+//ss//o/y-   .:o:+ooo+::::+hMMMMMMMMmy+//+/-.-/odMMMMMMMMMM
MMMMMMMMMMMMMd+s+/+o//+::   ...+ooss+::-/hNMMMMMMNh/```.::/ohmNMMMMMMMMMMMM
MMMMMMMMMMMMMMy/:://:---:   ---/+/:-.````yMMMMMNs-`    `+hNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMh+:-------:.  -:/::::-`   :NMMMdo.     `-dMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMN/..-.`.::::::::/--.``  -sNNds:`    `-o::sMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMo`::-`- .:::..-.-o:-..-:++:-`    `-+hNN:::mMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMN`.:-.`/  /-`-`:: yMNmy+:-.``..-:odNMMMy:::hMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMd  ----. `. :..:/`yMMMMMNmmmmmmNMMMMMMN/:::dMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMo.``` `````.---.`dMMMNdy+/+ohNMMMMMMNo:::/NMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMd.`.``.-.``-`.:yMMms-`  ``..:oNMMMd+::::hMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMy  -::--`  /hmMMd+.  `/hds:.--/dms/////sMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMd  --:-:` `:ymh:`  `:hNmmmms://+///+++smMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM/``-/:. .-.`.   `..:--...-::////+sydNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMN+`-+.`....`..`....`      `   `-//+MMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMN: `dy                    .`     `/:mMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM+  :Mm``   ``            `.       `+hMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM:  /NM:.-``-           ` `         -hMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMs  .+ys.--:.     ..----....         oMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMs.`--:/..:     :yhmNMMs:---.`      `dMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMdso+++:.   `oMMMMMMMMd/---:o+-`   /MMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMo   ./+MMMMMMMMMMh/::+MMd.  .MMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMm`  -::sMMMMMMMMMMMm::+MMM-  sMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMd+oos/ `/::/NMMMMMMMMMMMh/+mMMN`.+MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNh/:+/-o++osMMMMMMMMMMMm++dMMMo:/NMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMh+///::shho+hMMMMMMMMMMdo+hMMNy::dMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMd/-:oMNsoyMMMMMMMMMMmhhmMMd/::yMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMm+/+yMMMMMMMMMMMMMMMMMMMMMMMmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

dragonite_art = """\n      
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMoMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdomMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMyyMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNysyyyhyyyyyyyhNMMNy/sMMMMMMMMMMMMMMMMMysMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMMd+o+////ohNMMMMMMMMMMMMMMM/MMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms++++:::::::sNhyyyyyhdmNMmsyMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy+////:::::::::/mMMMMMMNdhhdNMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh////+:::::::::::dMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNho//NMMMMMMMMMMMMMMM+///oN--::::::::/hMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMdo+//+:yMMMMMMMMMMMMMMd////hmy-::::::::mNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMh+/+///so/NMMMMMMMMMMMMMo/////+/:::::::::hMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMmo+/////ooo+oMMMMMMMMMMMMm///+++/:::::::::::mMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMy/+//////o+oo+sMMMMMMMMMMMo///+oo//::::::::::dMMMMMMMMMMMMMMMM
MMMMMMMMMMMMs+o//////++/+oo+oNMMMMMMMMy/////ooo+/::::::::+odMMMMMMMMMMMMMMM
MMMMMMMMMMMo+oo//////+////ooo+hNMMMMMd::://++//+++//+/+++oo+hMMMMMmMmdodMMM
MMMMMMMMMMy+ooo//////o/////+oooohNMMm/:::::/+:://///o//+//+o+mMMMd:o//:ohhN
MMMMMMMMMm/sooo+/////o///////+oooosh/:::::::/.------:+/o////ssmy+:::::::/hM
MMMMMMMMMsooosys+////+////////+oooo:::::::::+--......////////:::::::::::+MM
MMMMMMMMM+sydNMMNmho//+//+syyyhys+::::::::::+.........-/:::::::::::::::+mMM
MMMMMMMMM+dMMMMMMMMMmyyymNMMMMMNo:::::::::::/:..-------:/::::::::::::/sNMMM
MMMMMMMMMsmMMMMMMMMMMMMMMMMMMMd/::::::::/::::/.........../+//::://+ohNMMMMM
MMMMMMMMMNdMMMMMMMMMMMMMMMMMNy/::::::::/o::::/...........-ommmmmmNNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMmo:::::::::/o:::::+--...........+NMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMh+:::::::::++/:::::/............../NMMMMMMMMMMMMM
ydMMMMMMMMMMMMMMMMMMMMMMMs/:::::::::++/::::::/.-------.....--/NMMMMMMMMMMMM
o:sNMMMMMMMMMMMMMMMMMMMMm//::::::::++/:::::::/................+MMMMMMMMMMMM
h::+hNMMMMMMMMMMMMMMMMMMN+/:::::::o///::::::/-.................hMMMMMMMMMMM
N/:::+hNMMMMMMMMMMMMMMMMdss/::::/+////::::::+.-----------------+hNMMMMMMMMM
Md:::::/ymMMMMMMMMMMMMMMMMN-/++:+::::/::::::/..................-/+mMMMMMMMM
MMy:::::::+ymNMMMMMMMMMMMMMmo///:::::::::::/...................-/:/mMMMMMMM
MMMy:::::::::/oyhmNNNNNNNNmo///:::::::::///:---...........-----/:::+MMMMMMM
MMMMd+::::::::::::://++++o+///:::::::::::+-..................../::::dMMMMMM
MMMMMNs+::::::::::::::::/+////::::::::::::/..................-/:::::yMMMMMM
MMMMMMNdo+/::::::::::::/o/////::::::::::::+-.--------------..-/:::::yMMMMMM
MMMMMMMMNyo++//::::::::+o/////::::::::::::/................-//:::::/NMMMMMM
MMMMMMMMMMNyo+o+++/////+o/////:::::::::::::-----......----:/::::::/mMMMMMMM
MMMMMMMMMMMMMdy/o/o++++/o/////::::::::::/+---...--------:++/////+yNMMMMMMMM
MMMMMMMMMMMMMMMNmss//o/+oo/////:::::::///////:::::://+o++///++ohNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMmhso//oo////::::://///::://///+oo++/////+ymMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNdhd+///:::+//+////++oyhdmNMmo+///////+ooshdNMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMN+//::::ymmmmNNNMMMMMMMMMMMho+//::::::::::oymMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNo//:::::+MMMMMMMMMMMMMMMMMMMMho+/::::::/:---:yMMM
MMMMMMMMMMMMMMMMMMMMMMMMm+/::::::::hMMMMMMMMMMMMMMMMMMMMMmhyo+++/--:oosmMMM
MMMMMMMMMMMMMMMMMMMMMMMm+/:::::::::/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMM+/:::/::://::NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMM-.//-.-//`.+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMM.-y+``-y:-sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMdMMd/hMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\n\n"""

# ASCII ART SECTION ENDS

# POKEMON CREATION - In this section, we will create the
# Pokémon objects we will use for the training section.
# After creation they are stored in the trainer_pokemon list

pikachu = Pokemon("Pikachu", "Electric", pikachu_art,
                  19, 4, 5, 2, 6, 2,
                  [thunder_shock, quick_attack, thunder, iron_tail],
                  ["Thunder Shock", "Quick Attack", "Thunder", "Iron Tail"])

eevee = Pokemon("Eevee", "Normal", eevee_art,
                12, 3, 4, 4, 7, 3,
                [sand_attack, quick_attack, iron_tail, swift],
                ["Sand Attack", "Quick Attack", "Iron Tail", "Swift"])

beedrill = Pokemon("Beedrill", "Bug", beedrill_art,
                   16, 5, 3, 2, 6, 1,
                   [poison_sting, twineedle, fury_attack, bite],
                   ["Poison Sting, Twineedle, Fury Attack, Bite"])

pidgeot = Pokemon("Pidgeot", "Flying", pidgeot_art,
                  18, 3, 7, 3, 7, 1,
                  [gust, wing_attack, quick_attack, fly],
                  ["Gust", "Wing Attack", "Quick Attack", "Fly"])

arbok = Pokemon("Arbok", "Poison", arbok_art,
                12, 3, 6, 6, 5, 3,
                [wrap, acid, poison_sting, bite],
                ["Wrap", "Acid", "Poison Sting", "Bite"])

sandslash = Pokemon("Sandslash", "Ground", sandslash_art,
                    21, 7, 2, 7, 5, 2,
                    [defense_curl, scratch, sand_attack, fury_attack],
                    ["Defense Curl", "Scratch", "Sand_Attack", "Fury Attack"])

arcanine = Pokemon("Arcanine", "Fire", arcanine_art,
                   20, 7, 7, 3, 6, 1,
                   [flare_blitz, ember, flamethrower, bite],
                   ["Flare Blitz", "Ember", "Flamethrower", "Bite"])

alakazam = Pokemon("Alakazam", "Psychich", alakazam_art,
                   13, 1, 8, 5, 2, 4,
                   [confusion, psybeam, reflect, recover],
                   ["Confusion", "Psybeam", "Reflect", "Recover"])

machamp = Pokemon("Machamp", "Fighting", machamp_art,
                  22, 5, 5, 5, 5, 3,
                  [bulk_up, low_kick, seismic_toss, wide_guard],
                  ["Bulk Up", "Low_Kick", "Seismic_Toss", "Wide Guard"])

victreebell = Pokemon("Victreebel", "Grass", victreebell_art,
                      18, 2, 6, 5, 6, 6,
                      [razor_leaf, wrap, vine_whip, bite],
                      ["Razor Leaf", "Wrap", "Vine Whip", "Bite"])

tentacruel = Pokemon("Tentacruel", "Water", tenracruel_art,
                     16, 4, 5, 5, 5, 4,
                     [water_gun, acid, recover, surf],
                     ["Water Gun", "Acid", "Recover", "Surf"])

golem = Pokemon("Golem", "Rock", golem_art,
                22, 5, 2, 7, 2, 1,
                [skull_bash, defense_curl, scratch, explosion],
                ["Skull Bash", "Defense Curl", "Scratch", "Explosion"])

gengar = Pokemon("Gengar", "Ghost", gengar_art,
                 14, 4, 4, 4, 4, 4,
                 [shadow_ball, shadow_ball, curse, confusion],
                 ["Shadow Ball", "Shadow Punch", "Curse", "Confusion"])

lapras = Pokemon("Lapras", "Ice", lapras_art,
                 22, 7, 2, 2, 2, 2,
                 [ice_beam, water_gun, surf, recover],
                 ["Ice Beam", "Water Gun", "Surf", "Recover"])

steelix = Pokemon("Steelix", "Steel", steelix_art,
                  24, 4, 5, 4, 6, 4,
                  [iron_tail, slam, skull_bash, wrap],
                  ["Iron Tail", "Slam", "Skull_Bash, Wrap"])

houndoom = Pokemon("Houndoom", "Dark", houndoom_art,
                   19, 5, 6, 4, 5, 1,
                   [quick_attack, bite, flamethrower, smoke_screen],
                   ["Quick Attack", "Bite", "Flamethrower", "Smoke Screen"])

sylveon = Pokemon("Sylveon", "Normal", sylveon_art,
                  17, 5, 5, 5, 5, 5,
                  [quick_attack, swift, moon_blast, recover],
                  ["Quick Attack", "Swift", "Moon Blase", "Recover"])

trainer_pokemon = [pikachu, eevee, beedrill, pidgeot, arbok, sandslash,
                   arcanine, alakazam, machamp, victreebell, tentacruel,
                   golem, gengar, lapras, steelix, houndoom, sylveon]


# BATTLE TRAINER - This functions will display a list of
# current trainer Pokémon to battle with. It asks the user to input
# a number corresponding to the Pokémon they want to train with from
# the list

def battle_trainer(my_pokemon):
    slow_prompt("\nTRAINER MENU\nChoose your Trainer Pokémon!\n\n")
    # Iterates over Trainer Pokémon list
    n = 1
    for i in trainer_pokemon:
        slow_prompt(str(n) + "- ")
        slow_prompt(i.name)
        slow_prompt("\n")
        n += 1

    # Validates trainer choice input
    valid_trainer_choice = False
    trainer_choice = input("\nSelect: ")
    while not valid_trainer_choice:
        if 0 < int(trainer_choice) <= len(trainer_pokemon):
            my_pokemon.battle(trainer_pokemon[int(trainer_choice) - 1])
            valid_trainer_choice = True
        else:
            trainer_choice = input("Please select a valid trainer number : ")


# BATTLE BOSS - The following section creates an
# object of type Pokemon representing the boss of the game
# It will then define the battle boss function which in turn
# calls the battle function of the current my_pokemon and
# passes Dragonite object as the opponent Pokemon argument


def battle_boss(my_pokemon):
    dragonite = Pokemon("Dragonite", "Dragon", dragonite_art,
                        30, 7, 7, 7, 7, 7,
                        [flamethrower, thunder, wing_attack, hyper_beam],
                        ["Flamethrower", "Thunder", "Wing Attack", "Hyper_Beam"])

    my_pokemon.battle(dragonite)


# CHOOSE_BATTLE - This function will prompt the user with
# a choice to battle the boss Pokémon if the criteria
# meets the standards set by the scenario constraints
# or traiN with other Pokemon.

def choose_battle(my_pokemon):
    boss_ready = assess_pokemon(my_pokemon)
    valid_battle_choice = False

    # Offers battle options if available
    if boss_ready:
        slow_prompt("\nBATTLE MENU\nWhat would you like to do?\n\n")
        battle_choice = input("1- Fight Boss! \n2- Train! \n\nSelect:")

        # Validates battle choice input
        while not valid_battle_choice:
            if battle_choice == "1":
                battle_boss(my_pokemon)
                valid_battle_choice = True
            elif battle_choice == "2":
                battle_trainer(my_pokemon)
                valid_battle_choice = True
            else:
                slow_prompt("\nBATTLE MENU\nWhat would you like to do?\n\n")
                battle_choice = input("1- Fight Boss! \n2- Train! \n\nSelect:")

    else:
        battle_trainer(my_pokemon)


# ADD POKEMON - This function adds a Pokemon to the
# my_collection variable. It checks if the Pokemon
# is present on the collections first then restores
# its hp to maximum and stores it.

def add_pokemon(defeated_pokemon):
    if defeated_pokemon in my_collection:
        pass
    else:
        defeated_pokemon.hp = defeated_pokemon.max_hp
        my_collection.append(defeated_pokemon)
        slow_prompt("You have unlocked " + defeated_pokemon.name + "!\n")


# CHANGE POKEMON - This function will allow the user
# to change its current Pokémon. These are stored
# in a list of Pokemon objects.

def change_pokemon(current_pokemon):
    slow_prompt("\nCOLLECTION MENU\nThese are your current Pokémon\n\n")
    n = 1
    for i in my_collection:
        slow_prompt(str(n) + "- ")
        slow_prompt(i.name + " : " + i.type + "\n")
        n += 1

    slow_prompt("\nDo you want to switch your current Pokémon?\nY / N\n")
    switch_choice = input("Select: ").upper()

    # Validates input for switch choice
    valid_switch_choice = False
    while not valid_switch_choice:
        if switch_choice == "Y":
            slow_prompt("Please input the index of the Pokémon to swap\nSelect:")
            collection_index = input()

            # Validates input type for integer
            try:
                int(collection_index)
            except ValueError:
                slow_prompt("Please input the index of the Pokémon to swap\nSelect:")

            valid_switch_choice = True
            valid_collection_choice = False

            # Validates input range for my_collection length
            while not valid_collection_choice:
                if 0 < int(collection_index) <= len(my_collection):

                    # Swaps out Pokemon
                    changed_pokemon = (my_collection[int(collection_index) - 1])
                    del my_collection[int(collection_index) - 1]
                    my_collection.append(current_pokemon)

                    valid_collection_choice = True
                else:
                    collection_index = input("Please select a valid Pokémon number : \n")
        elif switch_choice == "N":
            return current_pokemon
        else:
            slow_prompt("\nDo you want to switch your current Pokémon?\nY / N\n")
            switch_choice = input("Select: ").upper()
    return changed_pokemon


# ASSESS_POKEMON The following code will determine
# is the Pokémon is fit to battle a boss or if it
# needs more training.

# INTERPRETATION - This function is written in the order
# of constraints established by the scenario. It is i
# interpreted in the form of a Pokémon needing an agility
# of 4(Skilled) and either a ranged attack of 3(Associate)
# or melee attack of 4(Skilled). If these statistics do not
# return True then it will require the Pokemon to have an
# agility of 4(Skilled) and either block or healing with a
# rating of 3(Associate)

# Fun fact: This is supposed to be the main part of the code. XD

def assess_pokemon(my_pokemon):
    if (my_pokemon.agility >= 4) and ((my_pokemon.ranged >= 3) or (my_pokemon.ranged >= 4)):
        slow_prompt("\n*** Pokemon is ready to battle boss ***\n")
        return True
    elif (my_pokemon.agility >= 4) and ((my_pokemon.block >= 3) or (my_pokemon.healing >= 3)):
        slow_prompt("\n*** Pokemon is ready to battle boss ***\n")
        return True
    else:
        slow_prompt("\nPokemon is not ready to battle boss.\n")
        return False


# MAIN MENU - This function will print out general options
# for the user to do. It can redirect to the battle menu
# view current Pokémon stats, and chage current Pokémon

def main_menu(my_pokemon):
    winsound.PlaySound("route24", winsound.SND_FILENAME | winsound.SND_ASYNC)
    slow_prompt("\nMAIN MENU\nWhat would you like to do? \n\n")
    menu_choice = input("1- Battle! \n2- View Stats \n3- Change Pokémon \n" +
                        "4- Exit Game \n\nSelect:")
    valid_menu_choice = False
    while not valid_menu_choice:
        if menu_choice == "1":
            choose_battle(my_pokemon)
            main_menu(my_pokemon)
            valid_menu_choice = True
        elif menu_choice == "2":
            my_pokemon.draw()
            my_pokemon.view_stats()
            main_menu(my_pokemon)
            valid_menu_choice = True
        elif menu_choice == "3":
            if len(my_collection) >= 1:
                my_pokemon = change_pokemon(my_pokemon)
            else:
                slow_prompt("There is no collection available.\n")
                slow_prompt("Battle Pokémon to capture them! \n")
            main_menu(my_pokemon)
            valid_menu_choice = True
        elif menu_choice == "4":
            valid_menu_choice = True


# SKILL LIST, MY COLLECTION list will pertain to the
# skill level values established by the scenario constraints
# None value was added in order to link stats to direct
# damage and ease the reading of Pokémon stats.

skill_level = ["None", "Beginner", "Apprentice", "Associate", "Skilled", "Professional",
               "Artisan", "Master", "God"]

my_collection = []

# PROGRAM DEFINITIONS END

# MAIN PROGRAM - This section will start running first
# as it is not part of any function. It will start
# playing a track, displaying a message and prompting for
# the selection of a Pokémon. Afterwards the main_menu
# function will display

winsound.PlaySound("intro", winsound.SND_FILENAME | winsound.SND_ASYNC)

intro = """\n        Hello, welcome to the world of Pokémon! ...err, I mean Python. In this
        world, Pokémon are made of ASCII art. That's right, they look even uglier than
        the originals, but they can still be fun. Choose one and see! \n\n"""

slow_prompt(intro)
input("\tPress any key to continue")
clear()

slow_prompt("BULBASAUR")
bulbasaur = Pokemon("Bulbasaur", "Grass", bulbasaur_art,
                    22, 4, 5, 5, 3, 7,
                    [tackle, vine_whip, leech_seed, growth],
                    ["Tackle", "Vine Whip", "Leech Seed", "Growth"], )
bulbasaur.draw()
bulbasaur.view_stats()
input("Press any key to continue")
clear()

slow_prompt("CHARMANDER")
charmander = Pokemon("Charmander", "Fire", charmander_art,
                     20, 6, 7, 4, 3, 1,
                     [scratch, ember, smoke_screen, flamethrower],
                     ["Scratch", "Ember", "Smoke Screen", "Flamethrower"], )
charmander.draw()
charmander.view_stats()
input("Press any key to continue")
clear()

slow_prompt("SQUIRTLE")
squirtle = Pokemon("Squirtle", "Water", squirtle_art,
                   24, 4, 4, 7, 3, 2,
                   [bite, water_gun, withdraw, skull_bash],
                   ["Bite", "Water Gun", "Withdraw", "Skull Bash"], )
squirtle.draw()
squirtle.view_stats()
input("Press any key to continue")
clear()

# The selection interface will prompt the user to
# make a valid choice and will continue looping
# until the a valid selection is made

slow_prompt("1- Bulbasaur  - Healing Specialist\n")
slow_prompt("2- Charmander - Ranged  Specialist\n")
slow_prompt("3- Squirtle   - Tank    Specialist\n")
pokemon_choice = input("\nChoose a starter Pokémon :")

valid_pokemon_choice = False
while not valid_pokemon_choice:

    if pokemon_choice == "1":
        slow_prompt("\nYou have selected Bulbasaur\n")
        my_pokemon = bulbasaur
        valid_pokemon_choice = True
    elif pokemon_choice == "2":
        slow_prompt("\nYou have selected Charmander\n")
        valid_pokemon_choice = True
        my_pokemon = charmander
    elif pokemon_choice == "3":
        slow_prompt("\nYou have selected Squirtle\n")
        valid_pokemon_choice = True
        my_pokemon = squirtle
    else:
        pokemon_choice = input("Please select a Pokémon using keys 1, 2, or 3: \n")

winsound.PlaySound("victory", winsound.SND_FILENAME | winsound.SND_ASYNC)
print("Congratulations! You now have a " + my_pokemon.name + "\n")
time.sleep(3)
input("Press any key to continue")

clear()

main_menu(my_pokemon)
