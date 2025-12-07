class Inventory:
    def __init__(self, items=None, max_slots=8):
        self.max_slots = max_slots
        self.slots = []
        if items:
            for item in items:
                self.add_item(item)

    def add_item(self, item):
        """Adds an item to the inventory if there is space."""
        if len(self.slots) < self.max_slots:
            self.slots.append(item)
            print(f"Added {item} to inventory.")
            return True
        else:
            print("Inventory is full!")
            return False

    def remove_item(self, item_name):
        """Removes an item from the inventory by name."""
        for item in self.slots:
            # Assuming item is a string for now, or has a name attribute. 
            # Given current codebase uses strings for items in lists mostly.
            # If item is an object, we should check item.name
            if isinstance(item, str) and item.lower() == item_name.lower():
                self.slots.remove(item)
                return item
            elif hasattr(item, 'name') and item.name.lower() == item_name.lower():
                self.slots.remove(item)
                return item
        return None

    def list_items(self):
        """Returns a list of items in the inventory."""
        return self.slots

    def has_item(self, item_name):
        """Checks if an item is in the inventory."""
        for item in self.slots:
            if isinstance(item, str) and item.lower() == item_name.lower():
                return True
            elif hasattr(item, 'name') and item.name.lower() == item_name.lower():
                return True
        return False

    def __str__(self):
        if not self.slots:
            return "Inventory: Empty"
        items_str = ", ".join([str(item) for item in self.slots])
        return f"Inventory: {items_str}"
