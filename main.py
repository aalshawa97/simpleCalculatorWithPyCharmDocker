# This is a sample Python script.

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('welcome!')
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    print('Enter a command:')
    print('(1) Add')
    print('(2) Subtract')
    print('(3) Multiply')
    print('(4) Divide')
    operation = int(input())
    if operation == 1:
        # Code for addition
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operation == 2:
        # Code for subtraction
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operation == 3:
        # Code for multiplication
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operation == 4:
        # Code for division
        if num2 == 0:
            print('Error: Division by zero')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('Invalid entry')
