# Advanced Calculator Program in Python

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to perform floor division
def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x // y

# Function to get modulus
def modulus(x, y):
    return x % y

# Function to get exponentiation
def exponentiate(x, y):
    return x ** y

# Main program
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Division")
print("6. Modulus")
print("7. Exponentiation")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} // {num2} = {floor_division(num1, num2)}")

        elif choice == '6':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")

        elif choice == '7':
            print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
    else:
        print("Invalid Input")

    # Check if the user wants to perform another calculation
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break