# Triangle Drawer

i = 1
spacing = 0
rows = int(input('Enter how tall you want the triangle to be in rows: '))
print('\n')

while i <= (2 * rows):
    if i == 1:
        print((int(rows) - spacing- 1) * " " + "*")
    elif i == (2 * rows - 1):
        print("* " * (int((1/2) * i) + 1))
    else:
        print((int(rows) - spacing - 1) * " " +  "*" + " " * (i-2) + "*")
    spacing = spacing + 1
    i = i + 2

print('\nDone')

