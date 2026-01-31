import random

# Class Section
class Dice:
    def __init__(self):
        self.chanceToAttack = 1

    def roll_the_dice(self):
        self.chanceToAttack = random.randint(1,10)
        return self.chanceToAttack

## Character Section
class Character():
    def __init__(self,name,health,damage):
        self.char_name = name
        self.char_health = health
        self.char_damage = damage

    def attack(self):
        if attackChance < 8 and attackChance > 0 : # 70% chance to attack
            enemies[enemyNumber].enemy_health -= self.char_damage
            print(f"{self.char_damage} damage was given!")
        else :
            print("Damage was not given!")

    def take_damage(self):
        print("Enemy is attacking...")
        if attackChance < 5 and attackChance > 0 : # 40% chance to take damage
            self.char_health -= enemies[enemyNumber].enemy_damage
            print(f"{enemies[enemyNumber].enemy_damage} damage was taken!")
        else :
            print("You didn't take any damage!")

    def areYouAlive(self):
        if self.char_health <= 0 :
            print("You died.")
            return 0

    def escape(self):
        if escapeChance < 10 and escapeChance > 0 : # 90% chance to escape
            self.char_health -= 20
            print("You escape the room and took 20 damage")
            return 1
        else :
            self.char_health -= 30
            print("You didn't escape the room and you took 30 damage.")

    def information(self):
        print(f"{self.char_name} | Health={self.char_health} | Damage={self.char_damage}")
        print(f"{enemies[enemyNumber].enemy_name} | Health={enemies[enemyNumber].enemy_health} | Damage={enemies[enemyNumber].enemy_damage}")

class Knight(Character):
    def __init__(self,name,health,damage):
        super().__init__(name,health,damage)

class Sorcerer(Character):
    def __init__(self,name,health,damage):
        super().__init__(name,health,damage)

## Enemy Section
class Enemy():
    def __init__(self, name, heatlh, damage):
        self.enemy_name = name
        self.enemy_health = heatlh
        self.enemy_damage = damage

    def areYouAlive(self):
        if self.enemy_health <= 0 :
            print("Enemy is dead")
            return 0

# Object Section
knight = Knight("Knight",120,50)
sorcerer = Sorcerer("Sorcerer",100,70)
e1 = Enemy("Monster1",30,10)
e2 = Enemy("Monster2",50,20)
e3 = Enemy("Monster3",70,30)
e4 = Enemy("Monster4",120,40)
e5 = Enemy("Monster5",140,50)
dice = Dice()

characters = [knight,sorcerer]
enemies = [e1,e2,e3,e4,e5]

roomNumber = 1
enemyNumber = 0

# Game Section
print("--Characters--")
print(f"1 - Knight | Health={knight.char_health} | Damage={knight.char_damage}")
print(f"2 - Sorcerer | Health={sorcerer.char_health} | Damage={sorcerer.char_damage}")
charNumber = int(input("Select a character:")) - 1
if charNumber == 0 :
    print("=>You selected a Knight")

elif charNumber == 1 :
    print("=>You selected a Sorcerer")

else :
    print("Wrong number!")

characters[charNumber].char_name = input("Enter your character's name: ")
print("You entered a dungeon room and a monster appears")

while roomNumber < 6 :
    print(f"-----Room {roomNumber}-----")
    print(f"Health:{characters[charNumber].char_health}    Health:{enemies[enemyNumber].enemy_health}")
    print(f"  {characters[charNumber].char_name}  vs  {enemies[enemyNumber].enemy_name}")

    # Menu Section
    print("------------------------")
    print("1 - Attack")
    print("2 - Information")
    print("3 - Escape (-20 health)")
    choice = int(input("Enter a number: "))
    print("------------------------")

    if choice == 1 :
        attackChance = dice.roll_the_dice()
        characters[charNumber].attack()

        if enemies[enemyNumber].areYouAlive() == 0 :
            roomNumber += 1
            enemyNumber += 1
            continue

        attackChance = dice.roll_the_dice()
        characters[charNumber].take_damage()
        if characters[charNumber].areYouAlive() == 0 :
            break

    elif choice == 2 :
        characters[charNumber].information()

    elif choice == 3 and roomNumber < 5 :
        escapeChance = dice.roll_the_dice()
        if characters[charNumber].escape() == 1 :
            enemyNumber += 1
            roomNumber += 1
    else :
        print("You can't escape the last room!")
print("Game Over!")
