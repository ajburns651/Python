print('The operations are: Addition, Subtraction, Multiplication, Division, Power')
operation = str(input('Enter the operation you want to perform: '))

def sum(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)
    
def multi(a, b):
    return(a * b)

def divi(a, b):
    return(a / b)

def power(a, b):
    return (a ** b)

if operation == "Addition":
    a = int(input('Enter 1st number:'))
    b = int(input('Enter 2nd number:'))
    print(f'The sum of {a} + {b} is {sum(a, b)}')

if operation == "Subtraction":
    a = int(input('Enter 1st number:'))
    b = int(input('Enter 2nd number:'))
    print(f'{a} minus {b} is {sub(a, b)}')

if operation == "Multiplication":
    a = int(input('Enter 1st number:'))
    b = int(input('Enter 2nd number:'))
    print(f'{a} multiplied by {b} is {multi(a, b)}')

if operation == "Division":
    a = int(input('Enter 1st number:'))
    b = int(input('Enter 2nd number:'))
    print(f'{a} divided by {b} is {divi(a, b)}')

if operation == "Power":
    a = int(input('Enter the base: '))
    b = int(input('Enter the power: '))
    print(f'{a} to the power of {b} is {power(a, b)}')
