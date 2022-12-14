# itertools: Collection of tool for handling iterators. product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product: Cartesian product, equivalent to a nested for-loop
a = [1, 2, 5, 3]
b = [3, 4]
prod = product(a, b)
# prod = product(a, b, repeat=2) # repeat the same list
print(list(prod))

# permutations of a list (order matters)
perm = permutations(a)
# perm = permutations(a, 2) # 2 elements max
print(list(perm))

# combinations of a list (order does not matter)
comb = combinations(a, 2)
print(list(comb))
# combinations with replacement
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# accumulate: returns a running total of values in an iterable
acc = accumulate(a)
print(a)
print(list(acc))
# accumulate with a function
acc = accumulate(a, func=operator.mul)
print(list(acc))
acc = accumulate(a, func=max)
print(list(acc))

# groupby: groups values in an iterable based on a function
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]

group_obj = groupby(a, key=smaller_than_3)
# group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

persons = [
  {"name": "Tim", "age": 25},
  {"name": "Tom", "age": 15},
  {"name": "Jim", "age": 33},
  {"name": "Cage", "age": 25},
  {"name": "Cam", "age": 15},
]
group_obj2 = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj2:
    print(key, list(value))

# count: count from a starting number
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle: cycles through an iterable infinitely
# for i in cycle(a):
#     print(i)

# repeat: repeats an object, optionally with a times argument
for i in repeat(1, 4):
    print(i)