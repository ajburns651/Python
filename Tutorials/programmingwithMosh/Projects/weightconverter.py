# Prompt user for their weight and store it to the variable named weight
weight = float(input("Weight: "))

# Ask user if the weight they entered was in pounds or kilograms
unit = str(input("(L)bs or (K)g: "))

# Convert weight to other unit, and print their converted weight
if unit.upper() == "L":
    convertedweight = weight / 2.205
    print(f'You weigh {convertedweight} kilograms')
    
elif unit.upper() == "K":
    convertedweight = weight * 2.205
    print(f'You weigh {convertedweight} pounds')
    
else:
    print("The unit you entered is invalid")