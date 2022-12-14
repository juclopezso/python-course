# tuples is a collection data type innmutable, allows dupicate elements
import sys
import timeit

# tuple usses less space than list
mytuple = ('Max', 28, 'Boston')
mylist = ['Max', 28, 'Boston']
print(sys.getsizeof(mytuple), "bytes")
print(sys.getsizeof(mylist), "bytes")


# tuple is faster than list
# time to create tuples and list
print(timeit.timeit(stmt="(1,2,3,4,5)", number=1000000))
print(timeit.timeit(stmt="[1,2,3,4,5]", number=1000000))
