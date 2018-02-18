#Functional demonstration of simple Game

#First, we need a data structure to store the Characters properties. We use a python dict for this purpose
#a field "maincharacter" is needed to distinguish the characte
#to add even more different types of characters, like a witcher, we would need to modify the Maincahracter field to "CharacterType" and add numbers/names
#to distinguish the character type
Frodo = {"Name":"Frodo", "HP": 100, "Weapon": ("Dolch", 12), "Bandages":3, "Maincharacter": True}
Orkan = {"Name":"Orkan", "HP": 20, "Weapon": ("Keule", 15.5), "Maincharacter": False}

#To get detailed info about a character, we add a procedure to prints its datastructure
def print_character(character):
    #Because character types have different properties to be printed, we need to distinguish the cases and duplicate the print code
    #For each character type, we need a new if-else statement.
    if character["Maincharacter"]:
        print("Name: {}. HP: {}. Weapon: {} ({} demage). Bandages: {}".format(character["Name"], character["HP"], character["Weapon"][0], character["Weapon"][1], character["Bandages"]))
        return
    print("Name: {}. HP: {}. Weapon: {} ({} demage).".format(character["Name"], character["HP"], character["Weapon"][0], character["Weapon"][1]))

#To attack each other, we need to hand in two players. Only one such attack method can be used for all possible players, otherwise we would need to create
#new, character specifi methods like attack_main or attack_side
#When we would add a new character that has an armor, we would have to add new if-statements to react on that.
def attack(attacker, attacked):
    print("{} attacked {}!".format(attacker["Name"], attacked["Name"]))
    attacked["HP"] -= attacker["Weapon"][1]
    if attacked["HP"] <= 0:
        print("{} is dead!".format(attacked["Name"]))

#Only the main character can heal, therefore we need to check first whether character is main to prevent malfunctioning code
def heal(character):
    if character["Maincharacter"]:
        if character["Bandages"] > 0:
            character["Bandages"] -= 1
            character["HP"] = 100
            print("{}'s health is restored to 100!".format(character["Name"]))
        else:
            print("No bandages left!")
    else:
        print("Can not heal!")

#again, looting is a propertie that is restricted to main characters, so we need to add if-statements again
#Maybe frodo can not loot a witcher because a wand is not worth much to him, so new if-statements are needed
def loot(character, body):
    if character["Maincharacter"] and body["HP"] <= 0:
        print("{} looted {}. New weapon found: {} with streangh {}".format(character["Name"], body["Name"],
                                                                           body["Weapon"][0], body["Weapon"][1]))
        character["Weapon"] = body["Weapon"]
    else:
        print("Looting not possible!")

#The game is run by calling the procedures with the right arguments
#attacks are distinguished by different order of attacker-attacked
if __name__ == "__main__":
    print_character(Frodo)
    print_character(Orkan)
    attack(Frodo, Orkan)
    attack(Orkan, Frodo)
    attack(Frodo, Orkan)
    print_character(Frodo)
    loot(Frodo, Orkan)
    heal(Frodo)
    print_character(Frodo)
    print_character(Orkan)
