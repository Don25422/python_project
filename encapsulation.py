class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute (cannot be accessed directly)

    # Public method to get the age (getter)
    def get_age(self):
        return self.__age

# Usage
person = Person("Alice", 30)

# Accessing public attribute
print(person.name)
# Accessing private attribute using getter method
print(person.get_age())

