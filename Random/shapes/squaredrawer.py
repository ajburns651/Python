# Square Drawer

i = 1 
rows = int(input('Enter how tall you want the square to be in rows: '))
print('\n')

while i <= rows:
    if i == 1 or i == rows:
        print("*  " * rows)
    else:
        print("*" + (" " * (3 * rows - 4)) + "*") # Weird spacing on online python environment.
    i = i + 1
    
print('\nDone')
