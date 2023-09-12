# Now we will use dictionaries to give each of the group members roles and stats in an RPG game
# Since the original file used the math library, we will also use it here
# First import the math library
from math import pi

# Let's define the dictionary (this is actually a set of small dictionaries within a bigger dictionary!)

group1_rpg_roles = {
    "Namrata": {
        "class": "Archer",
        "atk" : 2*pi,
        "def" : pi,
        "spd" : 3*pi,
    },
    "Brayn": {
        "class": "Cleric",
        "atk" : 0,
        "def" : 4*pi,
        "spd" : 3*pi,
    },
    "Tai": {
        "class": "Tank",
        "atk" : 4*pi,
        "def" : 3*pi,
        "spd" : 0,
    },
    "Wilfredo": {
        "class": "Berserker",
        "atk" : 4*pi,
        "def" : 0,
        "speed" : 3*pi,
    }
}

# Specify which group member's stats you'd like to check:
key = "Brayn" #Modify this as necessary!

# Now let's access each of the values in the dictionary!
print("\n" + key + "'s stats are:")
print(group1_rpg_roles["Brayn"])

# Now let's look at Brayn's individual stats
print("\nBrayn's CLASS is:")
print(str(group1_rpg_roles["Brayn"]['class']))
print("\nBrayn's ATTACK is:")
print(str(group1_rpg_roles["Brayn"]['atk']))
print("\nBrayn's DEFENSE is:")
print(str(group1_rpg_roles["Brayn"]['def']))
print("\nBrayn's SPEED is:")
print(str(group1_rpg_roles["Brayn"]['spd']))