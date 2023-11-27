# Function to check if a triangle is a right-angled triangle
def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Function to calculate area using Heron's formula
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Example usage
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if is_right_triangle(a, b, c):
    print("It is a right-angled triangle.")
else:
    print("It is not a right-angled triangle.")

area = calculate_area(a, b, c)
print(f"Area of the triangle: {area:.3f}")
