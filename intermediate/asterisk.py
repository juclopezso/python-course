# uses of *

# power operator
result = 2 ** 3
print(result)

# repeat elements in a list
zeros = [0, 1] * 10
print(zeros)
# also for strings
myab = 'ab' * 10
print(myab)

# args and kwargs
# check function_args.py for more!
def foo(a, b, *args, **kwargs):
  print(a, b)
  for arg in args:
    print(arg)
  for key in kwargs:
    print(key, kwargs[key])

print("FOO")
foo(1, 2, 3, 4, 5, six=6, seven=7)
print("END FOO")

# unpacking lists
my_list = [1, 2, 3]
foo(*my_list)

# unpacking dictionaries
def foo(a, b, c):
  print(a, b, c)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

# unpacking containers
numbers = [1, 2, 3, 5, 6]

*beginning, last = numbers
print(beginning) # always unpacks to a list
print(last)

beginning, *last = numbers
print(beginning)
print(last) # always unpacks to a list

# Merge iterables
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# Merge dictionaries
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

new_dict = {**dict_a, **dict_b}
print(new_dict)
