# Lists ordered, mutable, allows duplicate elements

mylist = [1,2,4,5,6,3]
# mylist = ["banana", "cherry", "apple"]

# mylist2 = list()
mylist2 = [2, True, "apple", 3.14]

# last item in list
print(mylist[-1])

# iterate
for item in mylist:
    print(item)

# check if item exists
if "banana" in mylist:
    print("banana exists")

# append items
mylist.append("orange")

# insert item at index
mylist.insert(1, "blueberry")
print(mylist[1])

# remove last item an returns it
item = mylist.pop()

# remove specific item
mylist.remove("banana")

# remove all elements
mylist.clear()

# reverse list
mylist.reverse()

# sort list changing original list
# mylist.sort()

# sort list without changing original list
newlist = sorted(mylist)

# list with 5 0s
newlist = [0] * 5

# concatenate lists
newlist = mylist + mylist2

# slice list
newlist = mylist[1:3] # from index 1 to 3
newlist = mylist[1:] # from index 1 to end
newlist = mylist[:3] # from start to index 3
newlist = mylist[::2] # from start to end with step 2
newlist = mylist[::-1] # reverse the list

# copy list
newlist = mylist.copy()
newlist = mylist[:] # same as above using slicing

# list comprehension
newlist = [x*x for x in mylist if x % 2 == 0] # square each item in list if it is even

