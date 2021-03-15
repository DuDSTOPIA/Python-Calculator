def calculator():
    type_math = input('''choose  the type of mathematical calculation you want
    + for Addition
    - for Subtraction
    * for Multiplication
    / for Division: ''')

    operation(type_math)


def operation(type_math):
    x = int(input("Numero x: "))
    y = int(input("numero y: "))

    if type_math == '+':
        addition(x, y)
        again()

    elif type_math == '-':
        subtraction(x, y)
        again()

    elif type_math == '*':
        multiplication(x, y)
        again()

    elif type_math == '/':
        division(x, y)
        again()

    else:
        print('we do not recognize this symbol, please try again')


def addition(x, y):
    z = x + y
    print("O resultado de {} + {} = {}".format(x, y, z))

def subtraction(x, y):
    z = x - y
    print("O resultado de {} - {} = {}".format(x, y, z))

def multiplication(x, y):
    z = x * y
    print("O resultado de {} * {} = {}".format(x, y, z))

def division(x, y):
    z = x / y
    print("O resultado de {} / {} = {}".format(x, y, z))

def again():
    calc_again = input('Do you want to try again? Y for yes and N for no:  ')
    if calc_again.upper() == 'Y':
        calculator()
    elif calc_again == 'N':
        pass
    else:
        print('Sorry, the options are only Y or N')
        return
calculator()
again()