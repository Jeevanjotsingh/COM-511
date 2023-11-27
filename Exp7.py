# Creating a database using lists and tuples
database = [
    ("Akshat", 20, "Male"),
    ("Ujjwal", 21, "Male"),
    ("Rakshit ", 19, "Male"),
    ("Gaurang", 20, "Male"),
    ("Vivek", 19, "Male")
]

# Accessing and printing records from the database
for record in database:
    name, age, gender = record
    print(f"Name: {name}, Age: {age}, Gender: {gender}")