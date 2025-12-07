class Weapon:
    def __init__(self, name, damage, ammo_type):
        self.name = name
        self.damage = damage
        self.ammo_type = ammo_type
    
    def __str__(self):
        return self.name  # This ensures the weapon prints correctly

    def __repr__(self):
        return f"Weapon({self.name}, {self.damage}, {self.ammo_type})"
