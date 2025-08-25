# Simple Calculator

print("=== Simple Calculator ===")

# Take user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user which operation to perform
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter choice (+, -, *, /): ")

# Perform calculation based on choice
if choice == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif choice == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif choice == '*':
    result = num1 * num2
    print(f"{num1} × {num2} = {result}")

elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} ÷ {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation choice. Please try again.")
