from Entities.Location.Location import Location

class MainHall(Location):
    def __init__(self):
        super().__init__("Main Hall", 
                         "You are standing in the Main Hall of the mansion. It is a grand room with a high ceiling. "
                         "To the North is a large double door. To the West is the Dining Room. "
                         "To the East is a hallway.")
        # We can add items or exits here
        # self.set_exit("west", dining_room) # Example
