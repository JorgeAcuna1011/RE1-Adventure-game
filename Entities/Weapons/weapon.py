class Weapon:
    def __init__(self, name, Ammo_type, Capacity):
        self.name = name
        self.Ammo_type = Ammo_type
        self.Rounds = Capacity
    
    def __str__(self):
        return self.name  # This ensures the weapon prints correctly

    def __repr__(self):
        return f"Weapon({self.name}, {self.damage}, {self.ammo_type})"
