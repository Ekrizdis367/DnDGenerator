# Import Modules
import json
import random
import os

clear = lambda: os.system('cls')

# Import JSON Files
fClasses = open('classes.json')
fPersonalities = open('personalities.json')
fProfessions = open('professions.json')
fRaces = open('races.json')
fNames = open('names.json')

# Initialize JSON Variables
classes = json.load(fClasses)
personalities = json.load(fPersonalities)
professions = json.load(fProfessions)
races = json.load(fRaces)
names = json.load(fNames)

# Dice Functions
def roll(dice, die):
    return random.randint(dice,die)

def randomNPC():
    return False

def randomClass():
    return False

def randomRace():
    return False

def randomPersonality():
    personality = random.choice(personalities)
    return personality

def randomProfession():
    profession = random.choice(professions)
    return profession

def randomName():
    name = random.choice(names)
    return name

# =============================================================

while True:
    clear()
    print("==============================")
    print("1. NPC                        ")
    print("2. Class                      ")
    print("3. Race                       ")
    print("4. Personality                ")
    print("5. Profession                 ")
    print("6. Names                      ")
    print("==============================")
    num = input("Input: ")
    print("\n")

    match num:
        case "1":
            randomNPC()
        case "2":
            randomClass()
        case "3":
            randomRace()
        case "4":
            randomPersonality()
        case "5":
            print(randomProfession())
        case "6":
            print(randomName())
        case _:
            break

    print("\n")
    input("Press Enter to continue...")