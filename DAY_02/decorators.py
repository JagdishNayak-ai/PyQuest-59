## without wrapper
def my_decorator(func):
    print("Before execution")
    func()
    print("After execution")

def greet():
    print("Hello Jagdish!")
my_decorator(greet)

## with wrapper
def my_decorator(func):

    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator
def greet():
    print("Hello Jagdish!")
greet()


