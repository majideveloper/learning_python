from time import perf_counter
from functools import wraps
def time_calculator(func):
    @wraps(func)
    def inner(*args , ** kwargs):
        start_time = perf_counter()
        value = func(*args , ** kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("the runtime of  :" , func.__name__ ,"is: " , run_time)
        return value
    return inner

@time_calculator
def A(x):
    s = 0
    for i in range(x):
        s += i**2

A(90000000)

