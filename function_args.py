
# parameters are defined inside parenthesis while defining the function
# arguments are the values passed to the function when it is called

# name is a parameter
# default params must be at the end
def print_name(name, surname='Doe'):
  print(f'Hello {name}')

# 'John' is an argument
print_name('John')

def foo(a, b, c):
  print(a, b, c)

# can't use positional arguments after keyword arguments
# foo(1, b=2, 3)

# Variable length arguments
# *args: it's a tuple -  can pass any number of positional arguments
# **kwargs: it's a dictionary -  can pass any number of keyword arguments
def foo(a, b, *args, **kwargs):
  print(a, b)
  for arg in args:
    print(arg)
  for key in kwargs:
    print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)
# can use just positional arguments
foo(1, 2, 3, 4, 5)
# can use just keyword arguments
foo(1, 2, six=6, seven=7)
  
# force kwargs to be passed after the *
def foo(a, b, *, c, d):
  print(a, b, c, d)
foo(1,2,c=3,d=4)

# also like this
def foo(*args, last):
  print(args, last)
foo(1,2,3,4,5, last=6)

# Unpacking arguments
def foo(a, b, c):
  print(a, b, c)

my_list = [1, 2, 3] # length of the container must match the number of arguments
foo(*my_list)
# works also with dicrionaries with **
my_dict = {'a': 1, 'b': 2, 'c': 3} # keys must match the parameter names
foo(**my_dict)

# Local vs Global variables
def modify_var(x):
  global number # references the global variable outside the function
  number = x

number = 0
modify_var(88)
print(number)

# Parameters passing
# immutable types are passed by value they can't be modified but it's content can
# mutable types are passed by reference and can be modified
def add_item(my_list):
  # my_list = [900, 888, 777] # can't rebind the list
  my_list += [100, 200] # works
  # my_list = my_list + [300, 400] # doesn't work - this creates a new list (local variable)
  my_list.append(4)
  my_list[0] = -10

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)