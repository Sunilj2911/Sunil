# Input the length in feet
length = float(input("Enter length in feet : "))

print("****************************************")
# Display the available conversion options
print("1. Feet -> Inches")  # 1 feet = 12 inches
print("2. Feet -> Yards")  # 1 feet = (1/3) yard
print("3. Feet -> Miles")  # 1 feet = (1/5280) miles
print("4. Feet -> Millimeters")  # 1 feet = 304.8 mm
print("5. Feet -> Centimeters")  # 1 feet = 30.48 cm
print("6. Feet -> Kilometers")  # 1 feet = 0.0003048 km

# Input the user's choice
ch = int(input("\nEnter choice from above: "))

# Conversion units and corresponding conversion factors
units = ["inches", "yards", "miles", "millimeters", "centimeters", "kilometers"]
conversions = [12, 1/3, 1/5280, 304.8, 30.48, 0.0003048]

# Perform the conversion and print the result
print(f"{length} feet = {length * conversions[ch - 1]} {units[ch - 1]}")
