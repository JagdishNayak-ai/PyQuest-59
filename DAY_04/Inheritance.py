# Inheritance allows one class (child class) to reuse the attributes and methods of another class (parent class).

class Animal: #parent class
    def eat(self):
        print ("animal is eating")

class Dog(Animal): #child class
    def bark (self):
        print("Dog is barking")
        
d1= Dog()
d1.eat()
d1.bark()


# Create a parent class Employee:
# - Attribute: name
# - Method: show_name() → prints employee's name
# Create a child class Developer that inherits from Employee:

# - Method: work() → prints "Developer is writing code"

# Create an object of Developer and call both methods.

class Employee():
    def __init__(self,name):
        self.name = name
        
    def show_name(self):
        print(f"Employee Name:{self.name}")
        
class Developer(Employee):
    def work(self):
        print("Developer is writing code")
    
d = Developer("Jagdish")
d.show_name()
d.work()


# Create:
# - Parent class: Person
#   - Constructor accepts name and age
#   - Method show_person() displays both
# - Child class: Student(Person)
#   - Constructor accepts name, age, and course
#   - Use super() to initialize name and age
#   - Store course in the child class
#   - Method show_student() displays the course

class Person:
    def __init__(self, name ,age):
        self.name = name 
        self.age = age 
        
    def show_person(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
        
    def show_student(self):
        print(f"Course:{self.course}")
        
s = Student("Jagdish", 22, "MCA AI/ML")
s.show_person()
s.show_student()


# Create a parent class Animal:
# - Method: sound() → prints "Animal makes a sound"
# Create a child class Dog(Animal):
# - Override the sound() method.
# - Print "Dog barks"
# Create an object of Dog and call sound().


class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def sound(self):
        print("dog barks")

d= Dog()
d.sound()


# Create a parent class Vehicle:

# - Method start() → prints "Vehicle is starting"

# Create a child class Car(Vehicle):
# - Override start().
# - First, call the parent's start() using super().
# - Then print "Car engine is running"
# Create a Car object and call start().


class Vehicle:
    def start(self):
        print("Vehicle is starting")
        
class car(Vehicle):
    def start(self):
        super().start()
        print("Car engine is running")
c= car()
c.start()       























