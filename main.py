from Entities.Character.Playable_Character.Jill_Valentine import Jill_Valentine
# This is fine for now as I just want to build a demo of the game.
# Eventually need to fix this as I want to just call the folder itself, so that
# I don't have to write a whole bunch of imports cause that sounds terribly lol.

from Entities.Character.character import Character
import time

# For the most part everything in terms of importing Characters and Items is done.
# Need to start working on the main.py because it's just a mess lol.
# After that I need to work on the inventory system as there really isn't one
# for the inventory system I'm thinking about using a dicitionary, so that we 
# can keep track of the items.  After that we can implement enemies to simulate comabt.
# Finally start making the actual locations and possibly NPC's later on.


def game_intro():
    """Displays an intro message"""
    print("========================================")
    print("    Welcome to Resident Evil: Escape")
    print("========================================")
    time.sleep(1)
    print("\nYou are Jill Valentine, a former S.T.A.R.S. officer trying to survive a zombie outbreak.")
    time.sleep(2)
    print("\nFind weapons, fight enemies, and escape the city alive!\n")
    time.sleep(2)

def main_game_loop():
    """Main game loop where player interacts with the world"""

    player = Jill_Valentine() # Initialize Jill
    
    while player.health_state != "Dead":
        print("\n------ What do you want to do? ------")
        print("1. Check Status")
        print("2. Equip Weapon")
        print("3. Take Damage")
        print("4. Heal")
        print("5. Attack")
        print("6. Exit Game")
        
        choice = input("> ").strip()
        
        if choice == "1":
            print(f"\n{player.name} - Health: ({player.health_state})")
            player.equipped_weapon()
        
        elif choice == "2":
            weapon_name = input("Enter weapon name: ").strip()
            player.equip_weapon(weapon_name)
        
        elif choice == "3":
            damage = int(input("Enter damage amount: "))
            player.take_damage(damage)
        
        elif choice == "4":
            heal_amount = int(input("Enter heal amount: "))
            player.heal(heal_amount)
        
        elif choice == "5":
            player.attack()
        
        elif choice == "6":
            print("Exiting the game... Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

    print("\nGame Over.")

if __name__ == "__main__":
    game_intro()
    main_game_loop()
