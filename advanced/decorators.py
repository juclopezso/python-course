

# commonly used as a timer decorator to calculate the time a function takes to execute
# deug decorator to print the arguments and return value of a function
# check decorator to check if the arguments of a function are valid
# cache return values or add information or update the state

# functions in python are first class objects. They can be defined inside another function, passed as arguments to another function, returned from another function 
def start_end_decorator(func):

  def wrapper():
    # do something before
    print('Start')
    func()
    print('End')
  
  return wrapper

# function decorator: takes other function as argument to add new functionality to an existing function
@start_end_decorator # decorator
def print_name():
  print('Juan')

print_name()
# another way to use the decorator
print_name_dec = start_end_decorator(print_name)
print_name_dec()

# preserve the information of the original function
import functools

# with arguments
def my_decorator(func):

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    # do something before
    # print('Start')
    result = func(*args, **kwargs)
    # do something after
    # print('End')
    return result
  
  return wrapper

# function decorator: takes other function as argument to add new functionality to an existing function
@my_decorator # decorator
def add10(x):
  return x + 10

result = add10(10)
print("With args", result)
# info of the function
print(add10.__name__)


# decorator function with params

def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times=3)
def greet(name):
  print(f'Hello {name}')

greet('Juan')

# Nested decorators
# executed in order
@start_end_decorator 
@repeat(num_times=3)
def print_lastname():
  print('Lop')

print_lastname()

# Class decorator: do the same as function decorator but used to maintain and update a state

class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0

  # allows to call the class as a function
  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f'Executed {self.num_calls} times')
    print('I am called')
    return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc() 

@CountCalls
def say_hello():
  print('Hello')


say_hello()
say_hello()