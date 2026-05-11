def mydecorator(func):
    def wrapper_func():
        print("Before")
        func()
        print("After")
    return wrapper_func

@mydecorator
def say_hello():
    print("Hellooo")

say_hello()
