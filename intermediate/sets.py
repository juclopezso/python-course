# Sets: unordered, mutable, no duplicate elements

myset = set()
myset = {1,2,3,4,5}
myset2 = set([1,2,3,4,5])
myset3 = set("Hello")
print(myset3)

# remove element without exception
myset.discard(99)
myset3.discard("o")
print(myset)
print(myset3)

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
# union
uni = odds.union(evens)
print("union", uni)
## updates the set
# odds.update(evens)

# intersection
inter = odds.intersection(primes)
print("intersection", inter)
## updates the set
# odds.intersection_update(primes)

# diference: elements in odds but not in primes
diff = odds.difference(primes)
print("diference", diff)

# symetric difference: all elements that are in either odds or primes but not both
sim_diff = odds.symmetric_difference(primes)
print("symetric difference", sim_diff)
## updates the set
# odds.symmetric_difference_update(primes)

setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8}
# subsets
print("is subset:", setB.issubset(setA))

# superset: A superset contains all the elements of a subset
print("is superset:", setA.issuperset(setB))

# disjoint: two sets have no elements in common
print("is disjoint:", setB.isdisjoint(setC))

# copy set
newset = setA.copy()
newset = set(setA)

# Frozenset: inmutable set
inmu_set = frozenset([1,2,3,4,5])
print(inmu_set)