#Define the input string
input_string = "Welcome to Python World"

#1-Count number of alphabets
alphabet_count = 0
for char in input_string:
    if char.isalpha():
        alphabet_count = alphabet_count + 1

#Extract characters from given range
start = int(input("Enter starting index:"))
end = int(input("Enter ending index:"))
extracted_character = input_string[start:end]

#check if string is alphanumeric
is_alphanumeric = input_string.isalnum()

#print results
print("Number of alphabets:", alphabet_count)
print("Extracted characters:",extracted_character)
if is_alphanumeric:
    print("The string is alphanumeric:")
else:
    print("The string is not alphanumeric:")