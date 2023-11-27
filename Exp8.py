# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("(1) Celsius To Fahrenheit\n(2) Fahrenheit To Celsius\n(3) Exit")
    ch = int(input("Enter choice : "))
    if ch == 1:
        celsius_temperature = float(input("Enter temperature in celsius : "))
        fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
        print(f"{celsius_temperature:.2f}°C is equal to {fahrenheit_temperature:.2f}°F")
    elif ch == 2:
        fahrenheit_temperature = float(input("Enter temperature in fahrenheit : "))
        celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
        print(f"{fahrenheit_temperature:.2f}°F is equal to {celsius_temperature:.2f}°C")
    elif ch == 3:
        print("<< Thank You! >>")
        break
    else:
        print("Invalid choice. Please enter a valid option (1, 2, or 3).")
