import json

# encode a python object into a json string

class User:

  def __init__(self, name, age):
    self.name = name
    self.age = age

user = User('Max', 28)

def encode_user(obj):
  if isinstance(obj, User):
    return {
      'name': obj.name,
      'age': obj.age,
      obj.__class__.__name__: True # name of the class as a key
    }
  else:
    raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# same as above but using a class
from json import JSONEncoder

class UserEncoder(JSONEncoder):

  def default(self, obj):
    if isinstance(obj, User):
      return {
        'name': obj.name,
        'age': obj.age,
        obj.__class__.__name__: True
      }
    return JSONEncoder.default(self, obj)

userJSON = json.dumps(user, cls=UserEncoder)
# userJSON = UserEncoder().encode(user) # same as above
print(userJSON)


# decode a json string into a python object

def decode_user(dct):
  if User.__name__ in dct:
    return User(name=dct['name'], age=dct['age'])

  return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user), user.name, user.age)