# Magic Methods

# Dunder __ methods

class Person:

  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # deconstructor
  def __del__(self):
    print('Person object deconstructed')

# calls the __init__ method
p = Person('John', 36)
print(p)


class Vector:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # overloading the + operator
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  # overload the / operator
  def __div__(self, other):
    return Vector(self.x / other.x, self.y / other.y)

  # overload the representarion of the object
  def __repr__(self):
    return f'Vector({self.x}, {self.y})'

  def __len__(self):
    return 2

  # overload the call method: when the object is called
  def __call__(self):
    print('Called!')
  

v1 = Vector(5, 7)
v2 = Vector(20, 35)
v3 = v1 + v2
v3()
print(v3)
print(len(v3))