
def calculator():
    type_math = input('''choose  the type of mathematical calculation you want
    + for Addition
    - for Subtraction
    * for Multiplication
    / for Division: ''')

    x = int(input("Numero x: "))
    y = int(input("numero y: "))

    if type_math == '+':
        z = x + y
        print("O resultado de {} + {} = {}".format(x, y, z))
    elif type_math == '-':
        z = x - y
        print("O resultado de {} - {} = {}".format(x, y, z))
    elif type_math == '*':
        z = x * y
        print("O resultado de {} * {} = {}".format(x, y, z))
    elif type_math == '/':
        z = x / y
        print("O resultado de {} / {} = {}".format(x, y, z))


calculator()