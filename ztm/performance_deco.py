# Decorators

from time import time

def performance(func):
    def wrapper_func(*args , **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"It took {end - start:.5f} seconds")
        return result
    return wrapper_func

@performance
def long_time():
    for i in range(100000):
        i*5

long_time()