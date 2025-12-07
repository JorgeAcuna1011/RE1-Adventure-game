import time
from Entities.Character.Playable_Character.Jill_Valentine import Jill_Valentine
from Entities.Location.Spencer_Mansion.First_Floor.MainHall import MainHall

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
    
    # Initialize Game State
    player = Jill_Valentine()
    main_hall = MainHall()
    player.current_location = main_hall
    
    print("\n" + player.current_location.describe())

    while player.health_state != "Dead":
        print("\nWhat do you want to do? (type 'help' for commands)")
        command_input = input("> ").strip().lower().split()
        
        if not command_input:
            continue
            
        action = command_input[0]
        argument = " ".join(command_input[1:]) if len(command_input) > 1 else None

        if action == "look":
            print(player.current_location.describe())
        
        elif action == "go":
            if argument:
                next_location = player.current_location.get_exit(argument)
                if next_location:
                    player.current_location = next_location
                    print(f"You go {argument}.")
                    print(player.current_location.describe())
                else:
                    print("You can't go that way.")
            else:
                print("Go where? (north, south, east, west)")
                
        elif action == "take":
            if argument:
                # Logic to take item would go here
                # item = player.current_location.find_item(argument)
                # if item:
                #    player.inventory.append(item)
                #    player.current_location.remove_item(item)
                print(f"You attempt to take {argument}, but you can't pick things up yet.")
            else:
                print("Take what?")

        elif action == "inventory":
            print("Inventory:")
            items = player.inventory.list_items()
            if items:
                for item in items:
                    print(f"- {item}")
            else:
                print("Empty")
        
        elif action == "check" and argument == "status":
             print(f"\n{player.name} - Health: ({player.health_state})")
             player.equipped_weapon()

        elif action == "help":
            print("Available commands:")
            print("- look: Examine current location")
            print("- go [direction]: Move (north, south, east, west)")
            print("- take [item]: Pick up an item")
            print("- inventory: Check your items")
            print("- check status: Check health and weapon")
            print("- quit: Exit the game")

        elif action == "quit" or action == "exit":
            print("Exiting the game... Goodbye!")
            break
        
        else:
            print("I don't understand that command.")

    if player.health_state == "Dead":
        print("\nGame Over.")

if __name__ == "__main__":
    game_intro()
    main_game_loop()
