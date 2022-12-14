# collections: COunter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter: counts the number of times each value appears in a list
# returns a dictionary
var_a = "aaaabbbccc" # any iterable
my_counter = Counter(var_a)
print(my_counter)
# most common element
print(my_counter.most_common(1)) # returns a list of tuples
# list of elements
print(list(my_counter.elements()))


# namedtuple: tuple with named fields, similar to struct
Point = namedtuple("Point", "x,y") # creates a Point class with x and y fields
my_pt = Point(1, -4)
print(my_pt)
print(my_pt.x, my_pt.y)

# OrderedDict: dictionary that remembers the order in which its contents are added
# since python 3.7 dictionaries are ordered
ordered_dict = OrderedDict() # or = {}
ordered_dict["d"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["a"] = 4
print(ordered_dict)

# defaultdict: dictionary with a default value for new keys
default_dict = defaultdict(int) # int() returns 0
# default_dict = defaultdict(list) 
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict)
print(default_dict['a'], default_dict['f'])

# deque: double-ended queue, optimized for inserting and removing from both ends
my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
my_deque.appendleft(0)
print(my_deque)

my_deque.pop() # removes the last element
my_deque.popleft() # removes the first element
print(my_deque)

# my_deque.clear() # removes all elements
my_deque.extend([4,5,6]) # adds multiple elements at the end
# my_deque.extendleft([4,5,6]) # adds multiple elements at the beginning
print(my_deque)

my_deque.rotate(2) # rotates the deque n steps to the right. If n is negative, rotates to the left
# my_deque.rotate(-1) # rotates 1 place to the left
print(my_deque)