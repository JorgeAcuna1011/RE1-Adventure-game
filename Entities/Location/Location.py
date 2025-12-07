class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.enemies = []
        self.exits = {}

    def set_exit(self, direction, location):
        """Sets an exit for this location."""
        self.exits[direction] = location

    def get_exit(self, direction):
        """Returns the location in the given direction, or None if no exit exists."""
        return self.exits.get(direction)

    def add_item(self, item):
        """Adds an item to the location."""
        self.items.append(item)

    def remove_item(self, item):
        """Removes an item from the location."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def describe(self):
        """Returns a string description of the location, including items and exits."""
        desc = f"--- {self.name} ---\n{self.description}\n"
        
        if self.items:
            desc += "\nItems here:\n"
            for item in self.items:
                desc += f"- {item}\n"
        
        if self.exits:
            desc += "\nExits:\n"
            for direction in self.exits:
                desc += f"- {direction.title()}\n"
        
        return desc
