def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif op == "^":
        try:
            return a ** b
        except OverflowError:
            return "Error: Result too large"
    else:
        return "Error: Invalid operation"

try:
    a = float(input("Write your first number: "))
    b = float(input("Second number: "))
    op = input("Choose operation (^, /, *, +, -): ")

    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")
