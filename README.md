# Functional vs Object-Oriented Programming - A showcase

On the following pages, I want to present you a quick side-by-side comparison between developing a mini-game in a functional vs. in a object-oriented way. We are going to implement a very easy command line game, first only using functions and datastructures like older, non-object oriented programming languages like C would propably implement it. Then, we are going to implement the same functionalities, but following an object oriented approach. You will develop a good unterstanding of how Object-Orientation provides more flexibility and cleaner architecture. 

# How this tutorial is structured
With following this tutorial, we are going to learn the following

  - The process you go thorugh to build a Functional / Object-Oriented Script
  - How OO is different and how to build an OO-Design. 
  - The advantages of OOP over Functional Programming 

## The mini-Game

First of all, let's specify the scope of our game. Let's keep it simple: We want to implement a game where we play Frodo from *Lord of the Rings*. We, Frodo, can fight with Orks by by demaging them with our weapon. The orks, on their side, can demage us with their weapon of choice. When frodo wins the fight, he can loot the Ork, namely taking his weapon. To continue with the game, he can heal himself using bandages. 

![Two characters](https://github.com/joelbarmettlerUZH/Functional_vs_OOP_Showcase/raw/master/README_Resources/oop1.png)

Sound easy. Let's abstract the informations we got. We differentiate between two mayour categories: Attributes and Methods. Or, generally speaking: Values that describe the state of our character, and actions they can perform. 

### Attributes
The attributes of our Main character are his **Name**, his number of **Health Points**, his current **Weapon** as well as how many **bandages** he has left. Our Ork has a **Name** as well (*Let's call him Orkan, that sounds so cool*), his **Health Points** and he also has a **weapon**. 

![Attributes](https://github.com/joelbarmettlerUZH/Functional_vs_OOP_Showcase/raw/master/README_Resources/oop2.png)

To make it a little more interesting, we define the weapon as a tuple of its *Name* and its *Strength*. Written in words, the players attributes would look somehow like this:
>**Player**: Frodo (**Health** is 100, **Weapon** has name «Dagger», its **strength** 12.0, he’s got 3 **bandages**.)

### Methods
Now the methods are, as described, the things a character can do. Our main Character, Frodo,  has the ability to **attack** someone, to **heal** himself or to **loot** his dead enemy, while the simple Ork Orkan can just **attack** someone. 

![Methods](https://github.com/joelbarmettlerUZH/Functional_vs_OOP_Showcase/raw/master/README_Resources/oop3.png)

Again, writing it down in words looks the following:
>Frodo **attack** Orkan		*--->Orkans HP decreases by 12 HP*
>Orkan **attack** Frodo		*--->Frodos HP decreases by 15 HP*
>Frodo **attack** Orkan		*--->Orkans HP decreases by 12 HP. Orkan is dead**
>Frodo **loot** Orkan   	*--->Frodo gets Orkans weapon*
>Frodo **heals**			    *--->Frodos health is reset to 100, amount of bandages decreases by 2*

### Demon
Let's get ready for a sick demonstration of how our scripted game shall look like!

![Methods](https://github.com/joelbarmettlerUZH/Functional_vs_OOP_Showcase/raw/master/README_Resources/oopv1.gif)


## Functional implementation
Let's start implementing this beauty. First, we need a way to store the characters attributes. Python offers this cool datastructure called a *Dictionary* which allows us to give features a name and a value. Seems like the perfect way to represent our characters. We create two dicts, one for each characters, and pre-fill the start values accordingly. 

```Python
Frodo = {"Name":"Frodo", "HP": 100, "Weapon": ("Dagger", 12), "Bandages":3, "Maincharacter": True}
Orkan = {"Name":"Orkan", "HP": 20, "Weapon": ("Mace", 15.5), "Maincharacter": False}
```

You will see why we need that *Maincharacter* field in a second. 

Next, let's define what functions we need in our script. Beside the already defined functions **attack**, **heal** and **loot**, we introduce another funciton **print_character** that prints the characters current state to the console. We write an empty function structure first just to get the feeling for it. 

```Python
def print_characters(character):
	pass

def attack(attacker, attacked):
	pass

def heal(character):
	pass

def loot(character, body):
	pass
```

#### Implementing the print_character procedure
Now we start implementing the actuall functions from our sekelton, starting with the easierst one: The print_character functions. When thinking about how the printing-statement should look like, we quickly realize that printing Frodo shall have a different output than printing Orkan. This is because Frodo is a Maincharacter and therefore has a set of bandages that needs to be taken into consideration when printing Frodo, but since Orkan as an Ork has no such bandage-stack, his printing function will look differently. Here we need the Character-attribute boolean *Maincharacter* for the first time to check whether we need to print bandages or not:

```Python
def print_character(character):
    if character["Maincharacter"]:
        print("Name: {}. HP: {}. Weapon: {} ({} demage). Bandages: {}".format(character["Name"], character["HP"],character["Weapon"][0], character["Weapon"][1], character["Bandages"]))
        return
    print("Name: {}. HP: {}. Weapon: {} ({} demage).".format(character["Name"], character["HP"], character["Weapon"][0], character["Weapon"][1]))
```

When we call *print_character(Frodo), we get the following result:
>Name: Frodo. HP: 100. Weapon: Dagger (12 damage). Bandages: 3

#### Implementing the attack-procedure
The attack method is simple: we just reduce the attack points of the attacked by weapon-strength the attacker has. After reducing the attack points, we quickly check whether the attacked character is dead (helth points dropped down to 0 or below) and print the according message. 

```Python
def attack(attacker, attacked):
    	print("{} attacked {}!".format(attacker["Name"],attacked["Name"]))
    	attacked["HP"] -= attacker["Weapon"][1]
    	if attacked["HP"] <= 0:
       		print("{} is dead!".format(attacked["Name"]))
```

Let's test our procedure by calling *attack(Frodo, Orkan)
>Frodo attacked Orkan!

#### Implementing the loot-procedure
Looting someone is a procedure that should only be called with a Maincharacter since Orks like Orkan can not loot at all. So we need an if-statement first to check whether the character provided as an argument really is a maincharacter. Then, we check whether the character we'd like to loot is actually dead, because a living Ork will most propably not let us loot him.

```Python
def loot(character, body):
      	if character["Maincharacter"] and body["HP"] <= 0:
        	character["Weapon"] = body["Weapon"]
		print("{} looted {}. New weapon found: {} with strengh {}".format(character["Name"], body["Name"], body["Weapon"][0], body["Weapon"][1]))
    	else:
        	print("Looting not possible!")
```

We test our proceudre by calling *loot(Frodo, Orkan)* 
(Make sure Orkans health is at most zero, otherwise the looting will fail)
>Frodo looted Orkan. New weapon found: Mace with strengh 15.5

#### Implementing the heal-procedure
Heal is one of our procedures that is only callable with Frodo, our Maincharacter. We check first whether the character is of type *Maincharacter* and reset his health back to 100% if he has some bandages left. 

```Python
def heal(character):
   	if character["Maincharacter"]:
       		if character["Bandages"] > 0:
            		character["Bandages"] -= 1
            		character["HP"] = 100
            		print("{}'s health is restored to 				      100!".format(character["Name"]))
        	else:
            		print("No bandages left!")
    	else:
        	print("Can not heal!")
    	return character
```

Let's give it a try: *heal(Frodo)*.
>Frodo's health is restored to 100!

### Testing our implementation

Let's write the script to test our implementation in the __main__ function. 
```Python
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
```
We get the following output:

>Name: Frodo. HP: 100. Weapon: Dagger (12 damage). Bandages: 3
>Name: Orkan. HP: 20. Weapon: Mace (15.5 damage).
>Frodo attacked Orkan!
>Orkan attacked Frodo!
>Frodo attacked Orkan!
>Orkan is dead!
>Name: Frodo. HP: 84.5. Weapon: Dagger (12 damage). Bandages: 3
>Frodo looted Orkan. New weapon found: Mace with streangh 15.5
>Frodo's health is restored to 100!
>Name: Frodo. HP: 100. Weapon: Mace (15.5 damage). Bandages: 2
>Name: Orkan. HP: -4. Weapon: Mace (15.5 damage).

## May I introduce you: Uruk!
To spice up the game a little, we add a new character to our game: Uruk. He is a special type of Ork that also wears an armor that protects him from demage as long as the weapon-strength of the attacker is smaller than his armor-points.

![Rare sad pepe](https://github.com/joelbarmettlerUZH/Functional_vs_OOP_Showcase/raw/master/README_Resources/oopv2.gif)

Sigh... Okay, let's quickly think about the changes we would have to implement to change our script to fit the new requirements. First, we would have to add yet another *if-*statement to the print_character, heal and loot procedures. Then, the attack season would have to be changed as well, now also taking into consideration that there are some characters that wear armor. But we are not done yet. We actually need to change our whole character-dicts, because we have a third type of character now. Since we now have introduced three character types, we can no longer use the boolean *Maincharacter*. So we need to change that to a integer: 0 = Maincharacter, 1 = Ork, 2 = Ork-with-armor. But then we also have to rewrite all our previously written if-statements. It's clear that we would have to add and rewrite a lot of code, just to introduce a minor change in the game requirements. 

Now let's imagine a bigger game, where there is even more dependency in the different characters and functions. We would quickly overpopulate our functions with *if-s*, integer-keys and new dict-representation of our characters. 

## The solution: Object Oriented Programming!
The Object-Oriented Design approach will fix all the problems that occured with the functional approach. Let's see how:

### Classes & Inheritance
When we design a software in a Object-Oriented way, we use Classes. Each class we design represents one object in the Game. Each class then consists of Attributes and Methods describing the object it represents. I assume that you are familiar with the concepts of Classes, Inheritance and Polymorphism, but I will give a very very short introduction here as well. 

This is how you write a simple (and empty) class in Python:

```Python
class MyClass():
    def __init__(self, attr1):
        self._attribute1 = attr1
        self._attribute2 = "Second attribute of any Object"
    
    def method1(self):
        pass
        
    def method2(self):
        pass
```
A Class is the blueprint of an object - the class describes what an object is and how it can behave. We can build as many objects of a class as we want by assigning a new instance of the class to a variable. So we can create two objects of the same type. See that *__ init __*-method? This is the so called *Constructor*. The constructor is called when a new Instance of a class is created. You can pass certain values into the constructor that are then used to define the initial state of the Object / Class instance. Have a look at the following two instances, object1 and object2.

```Python
object1 = MyClass("First Attribute of object1")
object2 = MyClass("First Attribute of object2")
```

See that we provide different Strings at creation? Their value *_attribute1* will be set according to the value we pass at creation. You may asking yourself why there is that underscore !!!!!!!!!!!!!!

In our game example, it's quiet easy to identify our Objects: Frodo (*Maincharacter*) and Orkan (*Ork*). These two objects will result in one class each. Frodo will again have attributes for **Name**, his **Health Points**, his current **Weapon** as well as the number of **bandages** that he has left. His methods are still **attack**, **Heal** and **loot**. 
Orkan still has the attributes **Name**, **HP**, **Weapon** and one single mathod to **attack**. 

Let's look how their empty class structure would look like:

```Python
class Player():
    def __init__(self):
        self._name = "Frodo"
        self._attribute2 = 2
    
    def method1(self):
        pass
        
    def method2(self):
        pass
```

But why would structuring the attributes and methods into classes solve our problems? Well' the trick is to use one abstract class that bundles the attributes and Methods that both, Frodo and Orkan, share. When you compare Frodo to Orkan, it is clearly visible that they share most of the features - but not all of them. We will now introduce a new Object to our Game, a so called *abstract* object, or *abstract class*. An abstract class is a class that shall not directly be used / instanciated, it just serves as a parent for other classes. 

![abstract class](https://github.com/joelbarmettlerUZH/Functional_vs_OOP_Showcase/raw/master/README_Resources/oop21.png)

We pack all attributes and methods that are shared by both Frodo and Orkan into the abstract method. Then, when let both of them Inherit from *abstract Character* so that both get access to these features. This implies that if we want to introduce change to our features (either Attributes or Methods), we only have to implement the change once: in the *abstract* class, and both of our players will immediately also have the changes as well. 
The features that are NOT shared will be implemented later in the specific classes for Frodo and Orkan, but we get to that in a minute. 

### Implementing the abstract *Character*
Let's start building our abstract class. We want our class to have fields (instance variables) for **Name**, **Weapon** and **HP**, as well as methods for **string** and **attack**. This time, we also introduce a new method called **reduceHealth** that we did not implement before. Why? Because HP shall be a private attribute, nobody shall be able to directly change a characters health except the character himself. As a rule of thumb, private variables shall never be accessed directly but only via methods, and every variable shall be private that could be potentially harmfull to be public / accessible by every other object in the heap. 

We first build our empty class construct:

```python
class Character:
	def __init__(self, Name, Weapon):
		Name
		HP
		Weapon

	def __str__(self):
		pass

	def attack(self, enemy):
		pass

    def reduceHealth(self, enemy):
        pass
```

Let's become more concrete now and implement the constructor. When we create a new instance of character, we want to set a specific name and a specific weapon. We do NOT want to manually set the **HP**, simply because the class desides by itself how much HP a character shall get. For instance, a Maincharacter will always have 100 HP, a Ork always between, let's say, 10 and 25. So we do not pass the **HP** argument manually but calculate/set it in the constructor. 

```python
	def __init__(self, Name, Weapon):
	   if type(self) == Character:
            raise Exception(str(type(self))+" can not be directly instanced. Please use subclasses.")
		self.Name = Name
		self.HP = -1
		self.WeaponName = Weapon[0]
		self.WeaponStrength = Weapon[1]
```

A few questions may have arrised up to this point. What is the *if-*statement doing? And why are we setting the HP to -1, isn't the character dead at creation then? To address the first question: Our class shall be abstract, so no instanciation is allowed. We do not want any object to be of direct type "Character". What would that even mean?? You either are an Ork or a Hobbit, but how would you just be a *general Character*? So the first mechanism to disallow the instanciation of the class itself is to raise an exception in the constructor if someone tries to make an instance of type "Character". This will not lead to problems when we later inherit from Character, since the inherited Objects will have new names. Second, we set the HP to be negative one to force our subclasses to overwrite it. If we would forget to overwrite the HP, the new instanciated character would - as you said - die directly and we would see that there is a problem arround, but our game would not crash immediately. You can see the crash-prevention as a good or as a bad thing, some like to make the game crash instantly when something wrong happens, some try to prevent all crashes if possible and react otherwise. I prefer the second way, because crasher are annoying to deal with, but it really depends on the case. 

Let's continue implementing the String function. 

```python
def __str__(self):
    return("Name: {}. HP: {}. Weapon: {} ({} demage).".format(self.name, self._HP, self.WeaponName, self.WeaponStrength))
```

Easy. What about the attack function? Remember that the object itself is no longer responsible for dealing demage to the enemy, we only call the enemies "reduceHealth" method and he will act accordingly. Why should we not act in the attacker class directly, we introduce a new method? Well, the attacker really should not care about how to deal demage for every possible character type. HOW demage is taken is an information belonging to the attacked one. The attacker just sais "I deal demage to you, reduce your health". Then, the "recudeHealth" method looks at the attacker and reduces its health according to the attackers weapon. So the Ork could say "Oh, I am being attacked with a dagger, so I reduce my health by the daggers attack-points", but another Ork could say "What, you are attacking me with such a little dagger? My armor will take that hit and I will not reduce my health". See how we can react to new situations like that? It's the Ork Uruks job to know that he does not take demage when the dagger is too weak, not Frodos. 

```python
    def attack(self, enemy):
        enemy.reduceHealth(self)

    def reduceHealth(self, enemy):
        if self._HP > 0:
            self._HP -= enemy.WeaponStrength
            print("{} attacked {}!".format(enemy.name, self.name))
        if self._HP <= 0:
            print("{} is Dead!".format(self.name))
```

You see something special here: the attribute of the methods *attack* and *reduceHealth* are both of type enemy - we pass a whole object into these methods. So our attack function knows what enemy is to attack (*enemy*) and calls him to reduce his Health, *enemy.reduceHealth(self)*. The *self* that is passed as a parameter is the current object itself, the object in whose method we are currently at, so the attacker. So when we call *Frodo.attack(Orkan)*, we enter Frodos attack-method, then continue to Orkans recudeHealth Method with Frodo as an argument: *Orkan.reduceHealth(Frodo)*. In the reduceHealth method, we normally use the opponents health by the weapon strength of the attacker. If we want to implement this reduceHealth different later, we can just **overwrite** it in our subclasses.  

### The Player Class
Fine, we finished with the implementation of the Character. Now let's implement the Player (Frodo) as a childclass of Character. We again build an empty class body. Notice that we do NOT implement anything that we inherit correctly, so the methods for **attack** and **reduceHealth** are not found in the Player class, they are inherited. Same goes for the instance variables: we do not define **Name**, **HP** or **Weapon** again, we alredy did in the abstract class. What we DO implement here is everything that is either new or no longer holds from the abstract Character, like the **string** method (we want to have a different string representation for Player, so we will overwrite this one) or the **HP** attribute (we obviously want Player to have a health bigger than -1). 

```python
class Player(Character):
	def __init__(self, Name, Weapon):
	    HP
		Bandages

	def __str__(self):
		pass

	def heal(self):
		pass

    def loot(self, body):
        pass
```

We again start with implementing the constructor. Remember that our superclass sets the attributes for **Name** and **Weapon**? Instead of setting them again in the Player class, we simply call the Parentclass and pass our arguments to its constructor. This is elegant and a great way to not repeat code. After we called the supper constructor, **HP** is set to -1, so we overwrite this argument with 100. **bandages** is not yet set at all, so we need to set this value in the local constructor. 

```python
    def __init__(self, name, Weapon):
        Character.__init__(self, name, Weapon)
        self.HP = 100
        self._bandages = 3
```

Now we overwrite the **string** method. This is pretty straight forward.

```python
    def __str__(self):
        return("Name: {}. HP: {}. Weapon: {} ({} demage). Bandages: {}".format(self.name, self.HP, self.WeaponName, self.WeaponStrength, self._bandages))
```

The methods for **heal** and **loot** are nearly identical to the functional implementation, besides the fact that we again pass a Character-type as a parameter to **loot** and check if the provided character is really dead. 

```python
    def heal(self):
        if self._bandages > 0:
            self.HP = 100
            self._bandages -= 1
            print("{}'s health is restored to 100!".format(self.name))
        else:
            print("No bandages left!")

    def loot(self, body):
        if body.HP <= 0:
            self.WeaponName = body.WeaponName
            self.WeaponStrength = body.WeaponStrength
            print("{} looted {}. New weapon found: {} with streangh {}".format(self.name, body.name, self.WeaponName, self.WeaponStrength))
```

### Implementing the Ork-Class
Now that we implemented the Player class, doing the same with the Ork is really easy. Why? Because actually, can inherit anything from the abstract Character directly without any change and addition. Well, that's not 100% true, we DO need to make a change, namely overwriting the HP. But thats really it. How will this class look like then? Well, pretty empty.

```python
class Ork(Character):
    def __init__(self, name, Weapon):
        Character.__init__(self, name, Weapon)
        self.HP = 15.5
```

## Testing the Object Oriented Implementation
Now let's test whether our code work. We write a __ __main__ __ function and create two objects: Frodo as an instance of Player, and Orkan as an instance of Ork. When we call our methods on both with following our script:

```python
if __name__ == "__main__":
    #We instanciate two objects, one of type Player and one of type Ork
    Frodo = Player("Frodo", ("Dagger", 12))
    Orkan = Ork("Orkan", ("Mace", 15))

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
```

The output looks exactly the same as with our functional implementation:

>Name: Frodo. HP: 100. Weapon: Dagger (12 damage). Bandages: 3
>Name: Orkan. HP: 20. Weapon: Mace (15.5 damage).
>Frodo attacked Orkan!
>Orkan attacked Frodo!
>Frodo attacked Orkan!
>Orkan is dead!
>Name: Frodo. HP: 84.5. Weapon: Dagger (12 damage). Bandages: 3
>Frodo looted Orkan. New weapon found: Mace with streangh 15.5
>Frodo's health is restored to 100!
>Name: Frodo. HP: 100. Weapon: Mace (15.5 damage). Bandages: 2
>Name: Orkan. HP: -4. Weapon: Mace (15.5 damage).

## Comparison - OOP vs Functional
Let's do some quick comarison, even tho you have already seen many of the advanteges of OOP over Functional Programming. 

To create a new character, we had to create a new Dict storing all the attributes as well as information about the character type. With the OOP-Approach, we simply create a new instance and the rest is done for us. 

```python
Frodo = {"Name":"Frodo", "HP": 100, "Weapon": ("Dagger", 12), "Bandages":3, "Maincharacter": True}
Orkan = {"Name":"Orkan", "HP": 20, "Weapon": ("Mace", 15.5), "Maincharacter": False}

Frodo = Player("Frodo", ("Dagger", 12))
Orkan = Ork("Orkan", ("Mace", 15.5))
```
When we wanted to print our character, we had to use *if-* s to check what type it has, now we just print the instance and it knows exactly how to print itself.

```python
print_character(Frodo)

print(Frodo)
```

Remember the trouble we had introducing Uruk, a new type of Ork? We would have to change all our Dicts, nearly all of our functions and react to even more cases if even more *if-* statements. How would we introduce a new change in our OOP approach? Well, because Uruk is a special type of Ork, we would create a new class, inerherit from Uruk and overwrite its **string** method and his **reduceHealth** method, that only reduces his own health when the armos he has got is weaker than the attackers weapon. We would have to change **no single line of code!** We WOULD need to add some existing code, but that's all right. As a training, you can quickly implement the Uruk class to see how easy it is. It's a good Training.

## Some last words
You have seen now many advantages of OOP, especially when it comes to design, structure and extendibility. There is even more to OOP than what I just showcased you, but you should see now that getting used to OOP and using Classes is a great thing and makes a programmer not just a Coder but somewhat an Engineer. The first change from Functional to OOP is hard, and often you will just start writing some functions and then suddenly realize that you are following that bad habbit again. Try to build your program as we build our game: First ask yourself what Classes are needed, then decide what features some of the classes share and introduce an abstract parent to them. Then design an empty class structure and form the inheritence. Then, as a last step, really implement the methods. When you follow these steps, you will become a Object oriented Programmer in no time!

License
----

MIT License

Copyright (c) 2018 Joel Barmettler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


