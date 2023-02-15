# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

operators = {
    "*": multiply,
    "/": divide,
    "+": add,
    "-": subtract
}

num1 = int(input("What's the first number?: "))
for operator in operators:
    print(operator)
operation_choice = input("Pick an operation from above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operators[operation_choice]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_choice} {num2} = {first_answer}")

operation_choice = input("Pick an operation from above: ")
num3 = int(input("What's the next number?: "))
calculation_function = operators[operation_choice]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_choice} {num2} = {second_answer}")