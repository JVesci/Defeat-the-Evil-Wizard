import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
    
    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} health. Current health: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def power_attack(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} uses power attack for {damage} damage!")

    def battle_rage(self):
        self.attack_power += 2
        print(f"{self.name} enters battle rage! Attack power increased to {self.attack_power}.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def cast_spell(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} casts a powerful spell for {damage} damage!")

    def ice_spell(self, opponent):
        '''Reduce the opponent's attack power by 2'''
        opponent.attack_power = max(5, opponent.attack_power - 2)
        print(f"{self.name} casts an ice spell to reduce {opponent.name}'s attack power by 2.")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
    
    def quick_shot(self, opponent):
        damage = random.randint(15, 25)
        opponent.health -= damage
        print(f"{self.name} uses quick shot for {damage} damage!")
    
    def evade(self):
        print(f"{self.name} evades the wizard's attack!")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
    
    def holy_strike(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} uses holy strike for {damage} damage!")
    
    def divine_shield(self):
        print(f"{self.name} raises the divine shield and blocks the wizard's attack!")

# Evil Wizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
    
    def regenerate(self):
        heal_amount = 10
        self.health += heal_amount
        print(f"{self.name} regenerates {heal_amount} health. Current health: {self.health}")

# Character creation function
def create_character():
    print("Choose your character:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    
    class_choice = input("Enter the number of your character: ")
    name = input("Enter your character's name: ")
    
    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_attack(wizard)
                player.battle_rage()
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
                player.ice_spell(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
                player.evade()
                continue
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
                player.divine_shield()
                continue
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            continue
        else:
            print("Invalid choice, try again.")
            continue
        
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
        
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
    
    if wizard.health <= 0:
        print(f"{player.name} defeats {wizard.name}!")

# Main function
def main():
    player = create_character()
    wizard = EvilWizard("The Evil Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()