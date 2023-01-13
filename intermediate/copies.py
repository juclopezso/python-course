
# primitive copy
org = 5
cpy = org 
cpy = 6 # cpy is now a new var

# list wrong copy
org = [1, 2, 3]
cpy = org # cpy is a reference to org
cpy[0] = -10
print(org) # [1, 2, 3] - org is modified too

# Shallow copies: one level deep, only references of nested child objects
import copy

# all types of shallow copies
org = [1,2,3]
cpy = copy.copy(org)
cpy = list(org)
cpy = org.copy()
cpy = org[:]

# Deep copies: full independent copy of the object and all child objects
org = [[1,2,3,4], [5,6,7,8]]
cpy = copy.deepcopy(org)

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

class Company:
  def __init__(self, boss, employee):
      self.boss = boss
      self.employee = employee

p1 = Person('John', 36)
p2 = Person('Alex', 26)

c1 = Company(p1, p2)

# c2 = copy.copy(c1) # shallow copy doesn't work
c2 = copy.deepcopy(c1) # deep copy works
c2.boss.name = 'Cristian'

print(c1.boss.name)
print(c2.boss.name)