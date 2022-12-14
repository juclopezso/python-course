import random

# random module: pseudo-random number generator, they can be reproduced
# random not cryptographically secure, not recommended for security purposes
# use secrets for production

a = random.random() # float between 0 and 1
b = random.uniform(1, 10) # float between 1 and 10
c = random.randint(1, 10) # int between 1 and 10 includes 10
d = random.randrange(1, 10) # int between 1 and 10 excludes 10
e = random.normalvariate(0, 1) # normal distribution with mean 0 and standard deviation 1
print(a)

# lists
my_list = list("ABCDEFGH")
a = random.choice(my_list) # random element from a list
b = random.sample(my_list, 3) # k unique elements from a list
c = random.choices(my_list, k=3) # k non unique elements from a list
random.shuffle(my_list) # shuffles a list
print(a)
print(b)
print(c)

# reproduce results
random.seed(1) # sets the seed for the random number generator
print(random.random())
print(random.randint(1, 10))

# same results as before
random.seed(1)
print(random.random())
print(random.randint(1, 10))

# secrets module: cryptographically secure pseudo-random number generator
import secrets

a = secrets.randbelow(10) # int between 0 and 10 excludes 10
b = secrets.randbits(4) # int with k random bits
c = secrets.choice(my_list) # random element from a list
print(a)
print(b)
print(c)

# numpy module: numerical python, multidimensional arrays
import numpy as np

np.random.seed(1) 
# array with random floats between 0 and 1
a = np.random.rand(4, 2) # 4 rows, 2 columns
b = np.random.randint(0, 10)  # 10 excluded
c = np.random.randint(0, 10, (4,2))  # 10 excluded, 4 rows, 2 columns
d = np.random.rand(4, 2) # 4 rows, 2 columns
print(a)
print(d)
print(b)
print(c)