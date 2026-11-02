# Question 1: Student Management System
# Scenario:

# You are building a simple student management system for a college.

# Create a class called Student with the following requirements:
# 1. Create a class named Student.
# 2. Create an __init__() constructor.
# 3. Initialize three attributes:
#    - name
#    - age
#    - course
# 4. Create a method called display_info() that displays all student details.
# 5. Create three different student objects with different information.
# 6. Call display_info() for all three objects.

# class Student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
        
#     def display_info(self):
#         print(f"Student name :{self.name}")
#         print(f"Student age :{self.age}")
#         print(f"Student course :{self.course}")
#         print()
        
# s1= Student("Jagdish",22, "MCA AI/ML")
# s1.display_info()
# s2= Student("Rahul",23, "B.Tech")
# s2.display_info()
# s3= Student("Priya",21, "MBA")
# s3.display_info()



# Question 2: Employee Management System
# Scenario:

# A company wants to maintain employee information using Python OOP.
# Requirements
# 1. Create a class named Employee.
# 2. Create a constructor with four attributes:
#    - name
#    - employee_id
#    - department
#    - salary
# 3. Create a method display_details() to display all employee information.
# 4. Create another method annual_salary() that calculates and displays the yearly salary.
# 5. Create three employee objects with different details.
# 6. Call both methods for all three employees.
        
# class Employee():
#     def __init__(self,name, employee_id,department ,salary):
#         self.name= name
#         self.employee_id= employee_id
#         self.department = department
#         self.salary= salary
        
#     def display_details(self):
#         print(f"Employee Name :{self.name}")
#         print(f"Employee ID :{self.employee_id}")
#         print(f"Employee Department :{self.department}")
#         print(f"Employee salary :{self.salary}")
    
#     def annual_salary(self):
#         annual_salary = 12 * self.salary
#         print(f"Annual salary : {annual_salary}")
        
# e1= Employee("Jagdish", "E101", "AI/ML",30000)
# e1.display_details()
# e1.annual_salary()



# Question 3: Bank Account Management
# Intermediate
# Classes + Objects + Methods

# Scenario: Build a simple bank account system.

# Requirements:
# 1. Create a class BankAccount.
# 2. Constructor should initialize:
#    - account_holder
#    - balance
# 3. Create a method deposit(amount) to add money.
# 4. Create a method withdraw(amount) to subtract money.
# 5. If withdrawal amount is greater than the balance, print "Insufficient balance".
# 6. Create a method display_balance() to show the current balance.


# class BankAccount():
#     def __init__(self , account_holder , balance):
#         self.account_holder= account_holder
#         self.balance = balance 
        
#     def deposit(self,amount):
#         self.balance = self.balance + amount
#         print(f"deposited amount {amount}")
        
#     def withdraw(self,amount):
#         if amount  > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance = self.balance - amount
#             print(f"withdrawn amount  {amount}")
        
#     def display_balance(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Current balance : {self.balance}")

# p = BankAccount("Jagdish", 5000)

# p.deposit(2000)
# p.withdraw(1000)
# p.display_balance()


# Question 4: Product Management System
# Intermediate
# Create a class named Product.

# Requirements:
# 1. Constructor with:
#    - product_name
#    - price
#    - quantity
# 2. Create a method display_product() to display product details.
# 3. Create a method total_price() to calculate:
   
#    price × quantity
# 4. Create three different product objects.
# 5. Display their details and total prices.

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity= quantity
        
    def display_product(self):
        print(f"Product : {self.product_name}")
        print(f"Price : {self.price}")
        print(f"Quantity : {self.quantity}")
        
    def total_price (self):
        price = self.price * self.quantity
        print(f"Total price : {price}")

p1 = Product("Laptop", 50000, 2)
p1.display_product()
p1.total_price()





