# Write a Function that measures the time taken to execute 

import time

def timer(func):   # Accepts a function    # Imagine we want to make this function as toll gate, like other functions can execute after passing through this. Make it into a decorator.
    def wrapper(*args,**kwargs):   # Takes unlimited arguments
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper      # This return wrapper is for the decorator


@timer    #Decorator
def example_function(n):
    time.sleep(n)

example_function(2)   # Whenever this function is called first the timer decorator will be called and only after that the example_function will be called
# The example_function is passed to the decorator 