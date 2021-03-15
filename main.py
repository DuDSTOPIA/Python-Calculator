
def calculator():
    x = int(input("Numero x: "))
    y = int(input("numero y: "))

    def soma():
        z = x + y
        print("O resultado de {} + {} = {}".format(x, y, z))
    soma()

calculator()