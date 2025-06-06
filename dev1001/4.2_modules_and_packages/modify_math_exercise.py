"""
MODIFY Exercise: Working with the math module

Tasks:
1. Import the `math` module.
2. Calculate and print the circumference of a circle with a radius of 7.
   The formula for circumference is C = 2 * pi * r.
3. Use the `math.ceil()` function to round the number 4.3 up to the nearest integer and print it.
4. Use the `math.floor()` function to round the number 4.8 down to the nearest integer and print it.
5. Calculate 10 to the power of 4 using a function from the math module and print the result.
"""
import math

# --- Your code for Task 1 (import) is already implicitly here if you use math. ---

# Task 2: Calculate circumference
radius = 7
circumference = 2 * math.pi * radius
print(f"The circumference of a circle with radius {radius} is: {circumference:.2f}")

# Task 3: Use math.ceil()
number_to_ceil = 4.3
ceiled_number = math.ceil(4.3)
print(f"Ceiling of {number_to_ceil} is: {ceiled_number}")

# Task 4: Use math.floor()
number_to_floor = 4.8
floored_number = math.floor(4.8)
print(f"Floor of {number_to_floor} is: {floored_number}")

# Task 5: Calculate 10 to the power of 4
base = 10
exponent = 4
result_power = math.pow(base, exponent)
print(f"{base} to the power of {exponent} is: {result_power}")

print("--- Modify Math Exercise Complete (Placeholder) ---") # To ensure it runs
# Expected output (values will vary based on student implementation):
# The circumference of a circle with radius 7 is: 43.98
# Ceiling of 4.3 is: 5
# Floor of 4.8 is: 4
# 10 to the power of 4 is: 10000.0

# import math

# radius = 7
# circumference = 2 * math.pi * 7
# print(f"The circumference of a circle with radius {radius} is: {circumference:.2f}")

# number_to_ceil = 4.3
# ceiled_number = math.ceil(4.3)
# print(f"Ceiling of {number_to_ceil} is: {ceiled_number}")

# number_to_floor = 4.8
# floored_number = math.floor(4.8)
# print(f"Floor of {number_to_floor} is: {floored_number}")

# base = 10
# exponent = 4
# result_power = 10 ** 4
# print(f"{base} to the power of {exponent} is: {result_power}")