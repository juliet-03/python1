print("Input two numbers to find their sum, difference, product, and quotient")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
ope = input("Enter the operator (+, -, *, /): ")

# Convert inputs to float
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

# Perform the operation
if ope == "+":
    result = num1 + num2
elif ope == "-":
    result = num1 - num2
elif ope == "*":
    result = num1 * num2
elif ope == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2
else:
    print("Error: Invalid operator.")
    result = None

# Display the result if valid
if result is not None:
    print(f"Result: {result}")



        
