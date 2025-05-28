class LockedItemError(Exception):

    """Raised when a weapon is locked and cannot be used yet."""

    pass

 

available_weapons = ["sword", "bow", "staff"]

locked_weapons = ["legendary sword"]

 

def choose_weapon(weapon):

    if weapon in available_weapons:
        return f"You have chosen the {weapon}!"

    if weapon in locked_weapons:

        raise LockedItemError("This weapon is locked and cannot be used yet.")
    else:
        raise ValueError("That weapon is not available!")

 

try:

    weapon_choice = input("Choose your weapon (sword, bow, staff): ").strip().lower()

    result = choose_weapon(weapon_choice)

    print(result)

except ValueError as e:

    print(e)

except LockedItemError as e:

    print(e)
