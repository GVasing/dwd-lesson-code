'''

Develop a function that lets a player choose a weapon.

- It should check that the chosen weapon is in the available list.

- It should raise a ValueError if not.

- It should also raise a custom LockedItemError (you must define this exception) if the chosen weapon is locked.

'''

class LockedItemError(Exception):
    pass

available_weapons = ["sword", "bow", "staff"]
locked_weapons = ["legendary sword"]

# def weapons(selected):
#     if selected:
#         print(f"You have selected {choice}.")
#     else:
#         raise ValueError(f"{choice} not available. Choose another weapon.")


# try:
#     choice = input("Fighter, choose your weapon: ")
#     if choice in available_weapons:
#         weapons(True)
#     else:
#         weapons(False)
        
# except ValueError as err:
#     print(err)
    
# #  raise LockedItemError(f"{choice} is locked.")
 

def choose_weapon(weapon):

    if weapon not in available_weapons:

        raise ValueError("That weapon is not available!")

    if weapon in locked_weapons:

        raise LockedItemError("This weapon is locked and cannot be used yet.")

    return f"You have chosen the {weapon}!"

 

try:

    weapon_choice = input("Choose your weapon (sword, bow, staff): ").strip().lower()

    result = choose_weapon(weapon_choice)

    print(result)

except ValueError as e:

    print(e)

except LockedItemError as e:

    print(e)