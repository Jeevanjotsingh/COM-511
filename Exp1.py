# Type checking of various data types
var_str = "Hello, World!"
var_int = 42
var_float = 3.14159
var_list = [1, 2, 3, 4, 5]
var_tuple = (10, 20, 30)
var_dict = {"name": "Alice", "age": 30}
var_bool = True

# Demonstrating the use of built-in functions
print("Type of var_str:", type(var_str))
print("Type of var_int:", type(var_int))
print("Type of var_float:", type(var_float))
print("Type of var_list:", type(var_list))
print("Type of var_tuple:", type(var_tuple))
print("Type of var_dict:", type(var_dict))
print("Type of var_bool:", type(var_bool))

# abs() - Absolute value
num = -42
print("Absolute value of num:", abs(num))

# len() - Length of sequences (strings, lists, tuples, etc.)
print("Length of var_str:", len(var_str))
print("Length of var_list:", len(var_list))
print("Length of var_tuple:", len(var_tuple))

# min() - Minimum value in iterable
numbers = [10, 5, 8, 20, 3]
print("Minimum value in numbers:", min(numbers))

# round() - Round a floating-point number to a specified number of decimals
pi = 3.14159
rounded_pi = round(pi, 2)
print("Rounded pi:", rounded_pi)

# isalnum() - Check if all characters in a string are alphanumeric
alphanumeric_str = "Hello123"
non_alphanumeric_str = "Hello, World!"
print("Is alphanumeric_str alphanumeric?", alphanumeric_str.isalnum())
print("Is non_alphanumeric_str alphanumeric?", non_alphanumeric_str.isalnum())