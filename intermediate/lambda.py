# lambda: a function that is defined without a name 

# lambda arguments: expression
add10 = lambda x: x + 10

# same as:
def add10_func(x):
    return x + 10

print(add10(5))


mult = lambda x, y: x * y
print(mult(5, 4))

# commonly used with sorted(), filter(), map() and reduce()

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D)

points2D_sorted = sorted(points2D, key=lambda x: x[1]) # sorted by y
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) # sorted by sums
print(points2D_sorted)

# map function: applies a function to all the items in an input_list
# map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)
print(list(b))
# same with list comprehension
b = [x * 2 for x in a]
print(b)

# filter function: creates a list of elements for which a function returns true
# filter(func, seq)
b = filter(lambda x: x % 2 == 0, a)
print(list(b))
# same with list comprehension
b = [x for x in a if x % 2 ==0]
print(b)

# reduce function: applies a rolling computation to sequential pairs of values in a list
# reduce(func, seq)
from functools import reduce

product_a = reduce(lambda x, y: x * y, a)
print(product_a)