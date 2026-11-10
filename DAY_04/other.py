# Class Person
# - Constructor accepts name.
# - Method show_name() prints the name.
# Class Employee(Person)
# - Constructor accepts name and salary.
# - Use super() to initialize the name.
# - Method show_salary() prints the salary.
# Class Manager(Employee)
# - Constructor accepts name, salary, and department.
# - Use super() to initialize name and salary.
# - Method show_department() prints the department.

class Person:
    def __init__(self,name):
        self.name= name
        
    def show_name(self):
        print(f"Name:{self.name}")
        
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name) 
        self.salary= salary
        
    def show_salary(self):
        print (f"Salary:{self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
        
    def show_department(self):
        print(f"Department:{self.department}")
            
m = Manager("Jagdish", 50000, "AI/ML")
m.show_name()
m.show_salary()
m.show_department()


# Multiple Inheritance
# Class 1: Father
# - Method: father_skill() → prints "Father: Business Management"
# Class 2: Mother
# - Method: mother_skill() → prints "Mother: Financial Planning"
# Class 3: Child(Father, Mother)
# - Method: child_skill() → prints "Child: Python Programming"

class Father:
    def father_skill(self):
        print("Father:Business Management")
class Mother:
    def mother_skill(self):
        print("Mother: Financial Planning")

class Child(Father,Mother):
    def child_skill(self):
        print("Child: Python Programming")
c = Child()
c.father_skill()
c.mother_skill()
c.child_skill()



# Hierarchical Inheritance
# Create one parent class and two child classes.
# Class 1: Animal
# - Method: eat() → prints "Animal is eating"
# Class 2: Dog(Animal)
# - Method: bark() → prints "Dog is barking"
# Class 3: Cat(Animal)
# - Method: meow() → prints "Cat is meowing"

class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
c = Cat()
d.eat()
d.bark()
c.eat()
c.meow()



# Hybrid Inheritance
# Create four classes:

# Class 1: Person
# - Constructor accepts name.
# - Method show_name() prints the name.
# Class 2: Student(Person)
# - Constructor accepts name and course.
# - Use super() to initialize the name.
# - Method show_course() prints the course.
# Class 3: Employee(Person)
# - Constructor accepts name and salary.
# - Use super() to initialize the name.
# - Method show_salary() prints the salary.
# Class 4: WorkingStudent(Student, Employee)
# - Inherit from both Student and Employee.
# - Create an object with name "Jagdish", course "MCA AI/ML", and salary 25000.
# - Call all three display methods.

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, course):
        Person.__init__(self, name)
        self.course = course

    def show_course(self):
        print(f"Course: {self.course}")

class Employee(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary

    def show_salary(self):
        print(f"Salary: {self.salary}")

class WorkingStudent(Student, Employee):
    def __init__(self, name, course, salary):
        Student.__init__(self, name, course)
        Employee.__init__(self, name, salary)

ws = WorkingStudent("Jagdish", "MCA AI/ML", 25000)
ws.show_name()
ws.show_course()
ws.show_salary()






