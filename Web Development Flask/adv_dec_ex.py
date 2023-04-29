# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        func = function(args)
        func_name = function.__name__
        print(f"You called {func_name}{args}")
        print(f"It returned: {func}")
    return wrapper


n = []


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    for arg in args[0]:
        n.append(arg)
    return sum(n)


a_function(1, 4)
