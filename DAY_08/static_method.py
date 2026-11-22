# Static Method – Practice 1
# Question: Employee Salary Calculator

# Create a class called Employee.
# Requirements
# 1. Create a static method named calculate_bonus(salary).
# 2. If salary is greater than or equal to ₹50,000, calculate a 10% bonus.
# 3. Otherwise, calculate a 5% bonus.
# 4. Return the bonus amount.
# 5. Call the method using the class name without creating an object.

class Employee:
    @staticmethod
    def calculate_bonus(salary):
        if salary >= 50000:
            print(f"Salary :{salary} \nBonus:{salary * (10/100)}")
        else:
            print(f"salary :{salary}\n Bonus:{salary * (5/100)}")
        
# e = Employee()
# e.calculate_bonus(60000)
salary = 60000
bonus = Employee.calculate_bonus(salary)




# Practice 2
#  Password Validator using Static Method

# Create a class called PasswordValidator.

# Requirements:
# 1. Create a static method named validate_password(password).
# 2. Password must contain at least 8 characters.
# 3. Password must contain at least one digit.
# 4. Return True if both conditions are satisfied.
# 5. Otherwise, return False.
# 6. Call the method using the class name.

class PasswordValidator:
    @staticmethod
    def validate_password(password):
        has_digit = False
        
        for char in password:
            if char.isdigit():
                has_digit = True
                break
        if len(password) >= 8 and has_digit:
            return True
        else:
            return False
    
print(PasswordValidator.validate_password("Jagdish123"))
print(PasswordValidator.validate_password("jag123"))            
    



# Question: Temperature Converter
# Create a class called TemperatureConverter.
# Requirements
# 1. Create a static method named celsius_to_fahrenheit(celsius).
# 2. Convert Celsius into Fahrenheit using this formula:
   
#    \[
#    F = (C \times \frac{9}{5}) + 32
#    \]
# 3. Return the converted temperature.
# 4. Create another static method named fahrenheit_to_celsius(fahrenheit).
# 5. Use this formula: 
#    \[
#    C = (F - 32) \times \frac{5}{9}
#    \]
# 6. Call both methods using the class name without creating an object.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
celsius = 100
result = TemperatureConverter.celsius_to_fahrenheit(celsius)     
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {result}")

print()

fahrenheit = 98.6
result = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
print(f"Fahrenheit: {fahrenheit}")
print(f"Celsius: {result}")






































