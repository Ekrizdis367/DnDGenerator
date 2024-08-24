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
fFeatures = open('features.json')

# Initialize JSON Variables
classes = json.load(fClasses)
personalities = json.load(fPersonalities)
professions = json.load(fProfessions)
races = json.load(fRaces)
features = json.load(fFeatures)

def roll(dice, die):
    x = dice * die
    print(random.randint(dice,x))

def info():
    a = random.choice(['Male','Female','Other'])
    c = random.choice(['Straight','Bisexual','Gay'])
    print(a)
    print(c)
    print(' ')

def randomClass():
    c = random.choice(classes)
    print('Class: ' + c)

def randomRace():
    r = random.choice(races)
    print('Race: ' + r)
    if r == "Changeling":
        s = r
        while s == "Changeling":
            s = random.choice(races)
        print('Presentation: ' + s)

def randomPersonality():
    a = random.choice(personalities["Positive"])
    b = random.choice(personalities["Neutral"])
    c = random.choice(personalities["Negative"])
    print(' ')
    print('Positive: ' + a)
    print('Neutral: ' + b)
    print('Negative: ' + c)
    print(' ')

def randomProfession():
    # credit: https://www.reddit.com/r/DnDBehindTheScreen/comments/bjkejj/i_made_a_list_of_every_profession_i_could_think/
    p = random.choice(professions)
    print('Profession: ' + p)

def randomFeature():
    f = random.choice(features)
    print('Feature: ' + f)

def randomNPC():
    r = random.randint(1,100)
    info()
    randomRace()
    randomPersonality()
    randomFeature()
    randomFeature()
    print(' ')
    if r <= 10: randomClass()
    else: randomProfession()

# =============================================================
while True:
    clear()
    print("==============================")
    print("1. NPC                        ")
    print("2. Class                      ")
    print("3. Race                       ")
    print("4. Personality                ")
    print("5. Profession                 ")
    print("6. Feature                    ")
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
            randomProfession()
        case "6":
            randomFeature()
        case _:
            print()

    print("\n")
    input("Press Enter to continue...")