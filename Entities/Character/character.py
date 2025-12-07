import Entities.Items

class Character:
    #Each character is going to have some starting equipment and also have a special item unique to them
    #The function __init__ is just intializing character attributes
    
    def __init__(self, name, max_health, health_state, weapon, inventory, special_item):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.health_state = "Fine"
        self.weapon = weapon
        self.inventory = inventory
        self.special_item = special_item
        
    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"Weapon: {self.weapon}")

    def equipped_weapon(self):
        print(f"Weapon: {self.weapon}")

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)

        match self.current_health:
            #Checking health and updating health state
            case hp if hp <= 0:
                self.health_state = "Dead"
                print("YOU HAVE DIED")

            #Taking damage from enemy
            case _:
                print(f"{self.name} has taken {damage}")
    
    def attack(self):
        match self.weapon:
            #Checking to see if the Character has a gun equipped
            case weapon if weapon != None:
               print(f"{self.name} fires {self.weapon}")
            
            #Base case
            case _:
                print(f"{self.name} does not have a weapon equipped!")
    
    def heal(self, amount):
        self.current_health = min(100, self.current_health + amount)

        match self.current_health:
            case hp if hp >= 60 and hp <= 100:
                self.health_state = "Fine"
            case hp if hp >= 30 and hp <= 59:
                self.health_state = "Caution"
            case hp if hp >= 15 and hp <= 29:
                self.health_state = "Extreme Caution"
            case hp if hp >= 1 and hp <= 14:
                self.health_state = "Danger"
            
        print(f"{self.name}: {self.health_state}")