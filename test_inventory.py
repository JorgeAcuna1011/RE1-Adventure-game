from Entities.Character.Playable_Character.Jill_Valentine import Jill_Valentine
from Entities.Character.Inventory import Inventory

print("Initializing Jill...")
jill = Jill_Valentine()
print(f"Jill's Inventory: {jill.inventory}")
print(f"Jill's Inventory Items: {jill.inventory.list_items()}")
print(f"Slot count: {len(jill.inventory.slots)}")
