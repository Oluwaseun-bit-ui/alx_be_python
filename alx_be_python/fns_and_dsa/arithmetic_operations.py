def perform_operation(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error: Invalid operation"

# Get user input
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the operation and display result
    result = perform_operation(a, b, operation)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values for numbers.")
