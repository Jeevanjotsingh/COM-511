def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
    
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero is not allowed"

while True:
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    match choice:
        case "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", add(num1, num2))
        case "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", subtract(num1, num2))
        case "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", multiply(num1, num2))
        case "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", divide(num1, num2))
        case "5":
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please enter a number between 1 and 5.")