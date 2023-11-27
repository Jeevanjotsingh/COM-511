# Function to find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# Function to check if a number is an Armstrong number
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

# Example usage
num1, num2, num3 = 5, 10, 8
print("Maximum of", num1, num2, num3, "is", max_of_three(num1, num2, num3))

armstrong_number = 153
if is_armstrong(armstrong_number):
    print(armstrong_number, "is an Armstrong number.")
else:
    print(armstrong_number, "is not an Armstrong number.") 