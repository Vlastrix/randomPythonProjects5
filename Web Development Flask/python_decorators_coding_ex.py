import time

current_time = time.time()


def speed_calc_decorator(function):
    def wrapper():
        before_start = time.time()
        function()
        after_start = time.time()
        print(f"The time used to run {function.__name__} is {round(after_start - before_start, 2)} seconds.")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
         i * i


fast_function()
slow_function()
