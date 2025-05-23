# --- modify_exercise_2_shipping.py ---

# Inputs that will be passed to the function (examples)
package1_weight_kg = 2.5
package1_zone = "metro"

package2_weight_kg = 5.0
package2_zone = "remote"

package3_weight_kg = 1.2 # No zone specified, should use default

# --- Function definition ---
def calculate_shipping_cost(weight_kg, destination_zone="metro", base_rate_per_kg=2.50):
    """
    Calculates the shipping cost for a package.
    - weight_kg: The weight of the package in kilograms.
    - destination_zone: The shipping zone ('metro', 'regional', 'remote'). Defaults to 'metro'.
    - base_rate_per_kg: The base cost per kg. Defaults to $2.50.

    Zone Surcharges:
    - 'metro': $0
    - 'regional': $5
    - 'remote': $10
    """
    shipping_cost = 0.0
    surcharge = 0.0

    # TODO 1: Calculate the base cost (weight_kg * base_rate_per_kg)
    base_cost = weight_kg * base_rate_per_kg
    
    # TODO 2: Determine the surcharge based on destination_zone.
    # Use if-elif-else or match-case.
    # 'metro': surcharge = 0.0
    # 'regional': surcharge = 5.0
    # 'remote': surcharge = 10.0
    # (Optional: handle an unknown zone, e.g., print a message and use metro surcharge)

    if destination_zone == "metro":
        surcharge += 0
    elif destination_zone == "regional":
        surcharge += 5
    elif destination_zone == "remote":
        surcharge += 10
    else:
        surcharge == 0
        print("Zone Unknown. Metro surchage applied.")

    # OR

    # Use Match Case

    # match (destination_zone):
    #     case "metro":
    #         pass
    #     case "regional":
    #         surcharge = 5.0
    #     case "remote":
    #         surcharge = 10
    #     case _:
    #         surcharge = 0
    #         print("Zone Unknown. Metro surchage applied.")


    # TODO 3: Calculate the total shipping_cost (base_cost + surcharge)

    shipping_cost = base_cost + surcharge

    # TODO 4: Return the total shipping_cost
    return shipping_cost
    # Remove the 'pass' statement below when you start coding
    

# --- Main part of the script (provided) ---
# Call 1: Positional arguments
cost1 = calculate_shipping_cost(package1_weight_kg, package1_zone)
print(f"Package 1 (Weight: {package1_weight_kg}kg, Zone: {package1_zone}): Shipping Cost ${cost1:.2f}")

# Call 2: Using keyword arguments, and a different base rate
cost2 = calculate_shipping_cost(weight_kg=package2_weight_kg, destination_zone=package2_zone, base_rate_per_kg=3.00)
print(f"Package 2 (Weight: {package2_weight_kg}kg, Zone: {package2_zone}, Special Rate): Shipping Cost ${cost2:.2f}")

# Call 3: Using default for destination_zone
cost3 = calculate_shipping_cost(package3_weight_kg)
print(f"Package 3 (Weight: {package3_weight_kg}kg, Zone: default): Shipping Cost ${cost3:.2f}")
