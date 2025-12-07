from Entities.Weapons.weapon import Weapon  # Import the base Weapon class

class Jills_Samurai_Edge(Weapon):
    def __init__(self):
        super().__init__("Jill's Samurai Edge", 15, "Handgun Ammo")  
                     # Set weapon name,        damage, and ammo type
                     # Maybe later attack damage values and specific weapon skills
