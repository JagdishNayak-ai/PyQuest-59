def my_decorator(func):
    print("Before execution")
    func()
    print("After execution")

def greet():
    print("Hello Jagdish!")

my_decorator(greet)