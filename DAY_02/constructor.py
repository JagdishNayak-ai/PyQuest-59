# Question 5: Library Management System
# Create a class named Book.

# Requirements:
# 1. Constructor should accept:
#    - title
#    - author
#    - price
#    - available (default value: True)
# 2. Create these methods:
#    - display_book() — display all book details.
#    - borrow_book() — if the book is available, print "Book borrowed successfully" and set availability to False. Otherwise, print "Book is not available".
#    - return_book() — set availability back to True.

class Book:
    def __init__(self , title, author , price, available=True):
        self.title= title
        self.author= author
        self.price= price
        self.available = available
        
    def display_book(self):
        print(f"book title: {self.title}")
        print(f"book author: {self.author}")
        print(f"book price: {self.price}")
        print(f"Available: {self.available}")
        print()
    
    def borrow_book (self):
        if (self.available == True):
            print("Books Borrowed successfully")
            self.available = False
        else:
            print("Book is not available")
            
    def return_book(self):
        self.available = True
        print("book returned succesfully")
        
b1 = Book("Python Basics", "John", 500)

b1.display_book()
b1.borrow_book()
b1.borrow_book()
b1.return_book()
b1.display_book()     




# Create a class named Vehicle.
# Requirements
# 1. Constructor (__init__)

# Initialize these attributes:
# - vehicle_name
# - vehicle_number
# - rent_per_day
# - available (default True)
# 2. Create these methods:
# - display_details() — display all vehicle details.
# - rent_vehicle(days):
#   - Check whether the vehicle is available.
#   - If available, calculate total rent (rent_per_day × days).
#   - Change availability to False.
#   - Otherwise, print "Vehicle is not available".
# - return_vehicle():
#   - Change availability back to True.
#   - Print a return confirmation.

class Vehicle:
    def __init__(self, vehicle_name, vehicle_number, rent_per_day, available=True):
        self.vehicle_name = vehicle_name
        self.vehicle_number = vehicle_number
        self.rent_per_day = rent_per_day
        self.available = available
        
    def display_details(self):
        print(f"vehicle_name: {self.vehicle_name}")
        print(f"vehicle_number: {self.vehicle_number}")
        print(f"rent_per_day: {self.rent_per_day}")
        print(f"Available: {self.available}")
        print()
        
    def rent_vehicle(self,days):
        if self.available== True:
            total_rent = self.rent_per_day * days
            self.available= False
            print("Vehicle rented successfully")
            print(f"Total Rent: ₹{total_rent}")
            print()
            
        else:
            print("vehicle is not available")
            print()
            
    def return_vehicle(self):
        self.available = True
        print("Vehicle returned successfully")

v1 = Vehicle("Swift", "OD02AB1234", 1500)

v1.display_details()
v1.rent_vehicle(3)
v1.rent_vehicle(2)
v1.return_vehicle()
v1.display_details()














