# Create a decorator named welcome_decorator.

# Requirements:
# - Print "Welcome to Python!" before the original function.
# - Execute the original function.
# - Print "Keep Learning!" after the original function.

def welcome_decorator(func):
    def wrapper():
        print("welcome to python!")
        func()
        print("keep learning!")
    return wrapper
    
@welcome_decorator
def study():
     print("I am learning Decorators.")
study()


# Create a decorator named execution_decorator.
# It should:
# 1. Print "Function is starting...".
# 2. Execute the original function.
# 3. Print "Function has completed.".

def execution_decorator(func):
    def wrapper():
        print("function is starting")
        func()
        print("function has completed")
    return wrapper

@execution_decorator
def calculate():
    print("Calculating result...")
calculate()


# Decorator with Arguments
# Now let's make your decorator work with function arguments.

# Create a decorator named greet_decorator.

def greet_decorator(func):
    def wrapper(name):
        print("welcome!")
        func(name)
        print("Goodbye!")
        print()
    return wrapper
        
@greet_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Jagdish")
greet("Rahul")


# Decorator with Multiple Arguments
# Create a decorator named logging_decorator.

# Requirements:
# - Print "Function is called" before execution.
# - Execute the original function.
# - The decorator should support multiple arguments.


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is called")
        func(*args, **kwargs)
        print()
    return wrapper

@logging_decorator
def add(a, b):
    print(f"Sum: {a + b}")

add(10, 20)
add(50, 100)


# Login Verification Decorator
# Intermediate
# Create a decorator named login_required.

# Requirements:
# 1. Create is_logged_in = True.
# 2. If logged in, execute the original function.
# 3. Otherwise, print "Please login first!".
# 4. Apply it to dashboard().



def login_required(func):
    def wrapper():
        is_logged_in = False
        if is_logged_in:
            func()
        else:
            print("Please login first!")
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard!")

dashboard()       



# Execution Time Decorator
# Create a decorator named timer_decorator.

# Requirements:
# 1. Print "Starting execution..." before the function.
# 2. Execute the original function.
# 3. Print "Execution completed!" after the function.

def timer_decorator(func):
    def wrapper():
        print("Starting execution")
        func()
        print("Execution completed!")
    return wrapper

@timer_decorator
def process_data():
    print("Processing data...")

process_data()


# Return Value Preserving Decorator
# This is an important decorator concept.

# Create a decorator named result_decorator.

# Requirements:
# 1. Execute the original function.
# 2. Capture its returned value.
# 3. Print "Function executed successfully!".
# 4. Return the original result

def result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Function executed successfully!")
        return result
    return wrapper

@result_decorator
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Result:", result)






