import math

"""class Car:

    def __init__(self, modelis, degviela):
        self.atrums = 0
        self.degviela = degviela
        self.modelis = modelis

    def fill_tank(self, amount):
        self.degviela += amount

    def remonts(self, stavoklis):
        self.stavoklis = stavoklis



Mana_masina = Car("Ford", 0)
Mana_masina.remonts("good")
print(Mana_masina.stavoklis)
"""

"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect1 = Rectangle(10, 20)
print(rect1.area())"""

"""class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

c1 = Circle()
c2 = Circle(5)

print(c1.circumference())
print(c2.circumference())"""

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def study(self):
        print(f"I'm studying {self.major}.")
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old and I am a student of {self.major}.")
"""




"""class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"I'm teaching {self.subject}.")"""

"""def do_something(person):
    person.greet()
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()"""

"""p1 = Person("Alice", 30)
print(p1.name)
print(p1.age)"""

"""def do_something(person):
    person.greet()
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()"""

"""p1 = Person("Alice", 30)
print(p1.name)
print(p1.age)"""
