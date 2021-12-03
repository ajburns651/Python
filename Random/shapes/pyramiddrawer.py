# Pyramid Drawer

i = 1
spacing = 0
rows = int(input('Enter how tall you want the pyramid to be in rows: '))
print('\n')

while i <= (2 * rows):
    print((rows - spacing - 1) * " " + i * "*")
    spacing = spacing + 1
    i = i + 2


print('\nDone')