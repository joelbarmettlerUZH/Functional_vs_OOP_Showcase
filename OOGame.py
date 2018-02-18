#In object oriented programming, we use classes to achieve such small games. Each class belongs to a character and contains its
#State (instance variables) and its possible actions (methods)

class Character:
    #The general character sums up the State and actions that every character, regardless of its kind, shall have
    def __init__(self, name, Weapon):
        #We use this line of code to prevent Character fromb being instanciated, there shall be no generic character type in the game
        #We could use the abc module for this purpose, but it was not introduced in the lecture yet at the point I wrote this script for my students
        if type(self) == Character:
            raise Exception(str(type(self))+" can not be directly instanced. Please use subclasses.")
        self.name = name
        self._HP = -1
        self.WeaponName = Weapon[0]
        self.WeaponStrength = Weapon[1]

    #General characters are printed just with their states
    def __str__(self):
        return("Name: {}. HP: {}. Weapon: {} ({} demage).".format(self.name, self._HP, self.WeaponName, self.WeaponStrength))

    #Attacks are performed on another enemy which is as well of type Character.
    def attack(self, enemy):
        enemy.reduceHealth(self.WeaponStrength)

    #Each character takes care of himself HOW HealthPoints are reduced, so armor or resistance could be taken into consideration
    def reduceHealth(self, enemy):
        if self._HP > 0:
            self._HP -= enemy.WeaponStrength
            print("{} attacked {}!".format(enemy.name, self.name))
        if self._HP <= 0:
            print("{} is Dead!".format(self.name))


#The main player is a special type of Character, so we make him a subclass
class Player(Character):

    #He also has additional properties such as a fixed HP and additional bandages that a standard character does not have
    def __init__(self, name, Weapon):
        Character.__init__(self, name, Weapon)
        self.HP = 100
        self._bandages = 3

    #His string function is different, so we overwrite this one
    def __str__(self):
        return("Name: {}. HP: {}. Weapon: {} ({} demage). Bandages: {}".format(self.name, self.HP, self.WeaponName, self.WeaponStrength, self._bandages))

    #Player has the additional ability to heal, so we add the heal method just to his class
    def heal(self):
        if self._bandages > 0:
            self.HP = 100
            self._bandages -= 1
            print("{}'s health is restored to 100!".format(self.name))
        else:
            print("No bandages left!")

    #Only Players can Loot, so we add the loot method to his class. He sees the type of body he tries to loot and could - with help of
    #if-statements, react to it
    def loot(self, body):
        if body.HP <= 0:
            self.WeaponName = body.WeaponName
            self.WeaponStrength = body.WeaponStrength
            print("{} looted {}. New weapon found: {} with streangh {}".format(self.name, body.name, self.WeaponName,
                                                                               self.WeaponStrength))

#Orks are Characters as well, so we make Orks a subclass of Characters and give them fixed HP
class Ork(Character):
    def __init__(self, name, Weapon):
        Character.__init__(self, name, Weapon)
        self.HP = 15.5

#Here we test our Class
if __name__ == "__main__":
    #We instanciate two objects, one of type Player and one of type Ork
    Frodo = Player("Frodo", ("Dolch", 12))
    Orkan = Ork("Orkan", ("Keule", 15))

    print(Frodo)
    print(Orkan)

    #The attacks are distinguished by who calls attack on who
    Frodo.attack(Orkan)
    Orkan.attack(Frodo)
    Frodo.attack(Orkan)

    print(Frodo)

    #only frodo has loot and Heal because he is of type Player
    #calling Orkan.loot(SomeCharacter) would be impossible since Orkan has no method called loot
    Frodo.loot(Orkan)
    Frodo.heal()

    print(Frodo)
    print(Orkan)