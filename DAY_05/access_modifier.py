## Public : Public attributes can be accessed from anywhere — inside or outside the class.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Jagdish", 22)

# Accessing directly outside the class
print(s1.name)
print(s1.age)


## Protected (_salary) :Protected attributes are intended to be accessed within the class and its child classes. Python does not strictly enforce this rule.
class Employee:
    def __init__(self):
        self._salary = 50000
    def show_salary(self):
        print("Employee Salary:", self._salary)

class Manager(Employee):
    def show_manager_salary(self):
        print("Manager Salary:", self._salary)
        
m1 = Manager()
m1.show_salary()
m1.show_manager_salary()


## Private (__balance) : Private attributes are intended to be accessed only within the class.
#Python uses name mangling to make accidental external access harder.

class BankAccount:
    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print("Account Balance:", self.__balance)

account = BankAccount()
account.show_balance()





# Public Access Modifier

# Create a Student class with:
# - Public attribute name
# - Public attribute age
# - Method show_details() that prints both attributes.
# Create an object and access name and age directly.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age  
            
    def show_details(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
               
s = Student("Jagdish",22)
s.show_details()

# Direct access to public attributes
print("Direct Access:")
print(s.name)
print(s.age)



# Protected Access Modifier
# Create a parent class Employee:
# - Initialize a protected attribute _salary = 50000.
# - Create a method show_salary().
# Create a child class Manager(Employee):
# - Create a method show_manager_salary().
# - Access the parent's _salary attribute inside this method.

class Employee():
    def __init__(self):
        self._salary= 50000
    def show_salary(self):
        print(f"Employee salary:{self._salary}")

class Manager(Employee):
    def show_manager_salary(self):
        print(f"Manager salary:{self._salary}")
m= Manager()
m.show_salary()
m.show_manager_salary()



# Private Access Modifier
# Create a BankAccount class:
# - Initialize a private attribute __balance = 10000.
# - Create a method show_balance().
# - Display the balance using that method.

class BankAccount():
    def __init__(self):
        self.__balance= 10000
    def show_balance(self):
        print(f"balance:{self.__balance}")

b= BankAccount()
b.show_balance()















































