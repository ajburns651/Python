birth_year = input('Birth year? ') #Prompts user for birth year and stores it in the variable birth_year
print(type(birth_year)) # prints the type of birth year, in this case a string
#int()    converts string to integer
#float()  converts string to float
#bool()   converts string to boolean
age = 2021 - int(birth_year)
print(type(age)) # prints the type of age, which is an integer
print(age)

weight_lbs = int(input('What is your weight in pounds? ')) #prompts user for weight, converts it to an integer, stores it in the varaible weight
weight_kg = (weight_lbs / 2.20462) # converts pounds to kg
print(weight_kg) # prints the kilograms