def enter_dungeon(level):
    if level < 5:
        raise ValueError("You must be at least level 5 to enter the dungeon!")
    else:
        print("You bravely enter the dungeon")

    
# Main
try: 
    player_level = int(input("Enter player level: "))
    enter_dungeon(player_level)
except ValueError as err:
    print(f"Access Denied: {err}")
