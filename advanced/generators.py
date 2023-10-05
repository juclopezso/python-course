import sys
# Generators are a special kind of function that return an iterator.
# generates thr items inside the object lazily
# memory efficiente when dealing with large datasets

def my_generator():
  yield 1
  yield 2
  yield 3

g = my_generator()

# for i in g:
#   print(i)

# # runs until the first yield statement
# value = next(g)
# print(value)
# # runs until the second yield statement
# value = next(g)
# print(value)

# can be used as normal iterable
# print(sum(g))
# print(sorted(g))

def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1

cd = countdown(4)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))

# Memory size comparison
# we don't have to wait until the end of the function to get the result

# creates a list of n firts numbers
def firstn(n):
  nums = []
  num = 0
  while num < n:
    nums.append(num)
    num += 1
  return nums

# creates a generator of n firts numbers
def firstn_generator(n):
  num = 0
  while num < n:
    yield num
    num += 1

nums = firstn(1000000)
nums_g = firstn_generator(1000000)

print(sum(nums))
print(sum(nums_g))
# compare memory size
print(sys.getsizeof(nums))
print(sys.getsizeof(nums_g))

# Fibonacci sequence
def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

fib = fibonacci(100)
for i in fib:
  print(i)

# Generator expressions
# similar to list comprehensions but returns a generator

evens_generator = (i for i in range(100000) if i % 2 == 0)
# for i in evens_generator:
#   print(i)

evens_list = [i for i in range(100000) if i % 2 == 0]

print(sys.getsizeof(evens_generator))
print(sys.getsizeof(evens_list))
