class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Creating an instance of Person
p = Person("Alice", 30)

# Printing the object will call __repr__ and display a programmer-friendly string
print(p)

