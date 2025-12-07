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
        from Entities.Character.Inventory import Inventory
        # Ensure inventory is an Inventory object, if it's a list, convert it
        if isinstance(inventory, list):
             self.inventory = Inventory(inventory)
        else:
             self.inventory = inventory if inventory else Inventory()
             
        self.special_item = special_item
        self.current_location = None
        
    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"Weapon: {self.weapon}")

    def equipped_weapon(self):
        print(f"Weapon: {self.weapon}")

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)

        if self.current_health <= 0:
            self.health_state = "Dead"
            print("YOU HAVE DIED")
        else:
            print(f"{self.name} has taken {damage}")
    
    def attack(self):
        if self.weapon is not None:
             print(f"{self.name} fires {self.weapon}")
        else:
             print(f"{self.name} does not have a weapon equipped!")
    
    def heal(self, amount):
        self.current_health = min(100, self.current_health + amount)

        if self.current_health >= 60 and self.current_health <= 100:
            self.health_state = "Fine"
        elif self.current_health >= 30 and self.current_health <= 59:
            self.health_state = "Caution"
        elif self.current_health >= 15 and self.current_health <= 29:
            self.health_state = "Extreme Caution"
        elif self.current_health >= 1 and self.current_health <= 14:
            self.health_state = "Danger"
            
        print(f"{self.name}: {self.health_state}")