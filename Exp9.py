# Base class for Employee
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


# Derived class for Manager, inheriting from Employee
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    # Overriding the display_info method of the base class
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


# Derived class for Developer, inheriting from Employee
class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    # Overriding the display_info method of the base class
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# Example usage of the classes
if __name__ == "__main__":
    # Creating instances of Manager and Developer classes
    manager = Manager("Akshat", 1001, "IT")
    developer = Developer("Aniya", 1002, "Python")

    # Calling display_info method for Manager and Developer instances
    print("Manager Information:")
    manager.display_info()
    print("\nDeveloper Information:")
    developer.display_info()
