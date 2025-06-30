# Implement a decorator that caches the return values of a function, so that when its called with the same arguments, the cached value is return instead of re-executing the function
import time

def cache(func):
    cache_value = {}  # We take dictionary because its easirer to acces in dict
    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]  # Store the values in cache and retrieve when present
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper
 
@cache
def long_running_func(a,b):
    time.sleep(4)
    return a + b 

print(long_running_func(2, 3))
print(long_running_func(2, 3))