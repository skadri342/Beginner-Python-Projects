#Calculator
from art import logo

print(logo)

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    calculate = True

    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)

    while calculate == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        while True:
            cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
            if cont == "y":
                break
            elif cont == "n":
                calculate = False
                calculator()

calculator()