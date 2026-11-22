# Create a class called BankAccount.

# Requirements:
# 1. Create a constructor that accepts:
#    - account_holder
#    - initial_balance
# 2. Store the account holder as a public attribute.
# 3. Store the balance as a private attribute (__balance).
# 4. Create these methods:
#    - deposit(amount) – Add money if the amount is positive.
#    - withdraw(amount) – Withdraw money if sufficient balance is available.
#    - get_balance() – Return the current balance.
#    - show_details() – Display the account holder and current balance.
# 5. Create an object with:
#    - Account holder: Jagdish
#    - Initial balance: ₹10,000
# 6. Perform these operations:
#    - Deposit ₹5,000.
#    - Withdraw ₹2,000.
#    - Display account details.


class BankAccount:
    def __init__ (self,account_holder,initial_balance):
        self.account_holder= account_holder
        self.__balance= initial_balance
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount 
            print(f"deposit successful: {amount}")
        else:
            print("Invalid deposit amount!")
            
    def withdraw (self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrawal successful: {amount}")
        else:
            print("Insufficient balance!")
            
    def get_balance(self):
        return self.__balance
        
    def show_details(self):
        print(f"\naccont holder:{self.account_holder}")
        print(f"current balance:{self.__balance}")
        
b = BankAccount("Jagdish",10000)
b.deposit(5000)
b.withdraw(2000)
b.show_details()


# Question 2 – Employee Management System
# OOP + Inheritance + Encapsulation + super()
#  Medium–Hard
# Create a parent class called Employee and a child class called Developer.
# Requirements
# 1. Parent class: Employee
# - Create a constructor accepting name, employee_id, and salary.
# - Store name as a public attribute.
# - Store employee_id as a protected attribute (_employee_id).
# - Store salary as a private attribute (__salary).
# - Create a method get_salary() that returns the salary.
# - Create a method show_details() that displays employee information.
# 2. Child class: Developer(Employee)
# - Create a constructor accepting name, employee_id, salary, and programming_language.
# - Use super() to initialize the parent attributes.
# - Store programming_language as a public attribute.
# - Create a method show_developer_details() that displays all employee and developer details.


class Employee():
    def __init__(self,name,employee_id, salary):
        self.name = name 
        self._employee_id = employee_id
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
    
    def show_details (self):
        print(f"Employee name :{self.name}")
        print(f"Employee ID :{self._employee_id}")
        print(f"Employee salary:{self.get_salary()}")
        
class Developer(Employee):
    def __init__ (self,name,employee_id,salary,programming_language):
        super().__init__(name,employee_id,salary)
        self.programming_language = programming_language
    
    def show_developer_details(self):
        print(f"Employee name :{self.name}")
        print(f"Employee ID :{self._employee_id}")
        print(f"Employee salary:{self.get_salary()}")
        print(f"programming language:{self.programming_language}")


d = Developer("Jagdish","EMP01",50000,"Python")
d.show_developer_details()




# Question 4 – Library Management System
# Medium
#  OOP + Encapsulation + Inheritance

# Create a Python program using the following requirements:

# 1. Create a parent class Library:
# - Create a constructor accepting library_name and total_books.
# - Store library_name as a public attribute.
# - Store total_books as a private attribute (__total_books).
# 2. Create these methods in Library:
# - add_books(quantity) – Add books if quantity is positive.
# - borrow_books(quantity) – Reduce books if sufficient books are available.
# - get_total_books() – Return the current number of books.
# - show_details() – Display library name and available books.
# 3. Create a child class DigitalLibrary(Library):
# - Accept library_name, total_books, and website.
# - Use super() to initialize the parent attributes.
# - Store website as a public attribute.
# - Create show_digital_details() to display all details.
# 4. Create an object with these values:
# Attribute	Value
# Library name	Central Library
# Total books	100
# Website	www.centrallibrary.com

# 5. Perform these operations:
# - Add 20 books.
# - Borrow 30 books.
# - Display library details.
# - Display digital library details.


class Library:
    def __init__(self,library_name ,total_books):
        self.library_name = library_name
        self.__total_books = total_books
        
    def add_books(self,quantity):
        if quantity >0:
            self.__total_books += quantity
            print(f"Books added successfully: {quantity}")
        else:
            print("Invalid book quantity!")
    
    def borrow_books(self,quantity):
        if quantity <= 0:
            print("Invalid book quantity!")
        elif self.__total_books >= quantity:
            self.__total_books -= quantity
            print(f"Books borrowed successfully: {quantity}")
        else:
            print("Not enough books available!")
    
    def get_total_books(self):
        return self.__total_books
    
    def show_details(self):
        print(f"Library Name: {self.library_name}")
        print(f"Available Books: {self.get_total_books()}")
        

class DigitalLibrary(Library):
    def __init__(self,library_name,total_books,website):
        super().__init__(library_name,total_books)
        self.website = website
    
    def show_digital_details(self):
        print(f"Library_name : {self.library_name}")
        print(f"Total Books : {self.get_total_books()}")
        print(f"Website : {self.website}")

d = DigitalLibrary("Central Library",100,"www.centrallibrary.com")

d.add_books(20)
d.borrow_books(30)
print()
d.show_details()
print()
d.show_digital_details()    
        
























































