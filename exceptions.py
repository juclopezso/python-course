# Errors and Exceptions

# syntax errors
a = 5
# print(a))

# type error
a = 5 + '10'
# file error
# f = open('test.txt')
# also value error, index error, key error


# exceptions
x = -5
if x < 0:
  raise Exception('x should be positive')

# assert
assert (x >= 0), 'x is not positive' # only for debugging

# try except
try:
  a = 8 / 0
except Exception as e:
  print('an error occurred', e)

# knowing the type of error
try:
  a = 8 / 1
  b = a + '10'
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print('everything is fine')
finally: # runs always even if there is an error
  print('cleaning up...')

# define exceptions
class ValueTooHighError(Exception):
  pass

class ValueTooSmallError(Exception):
  def __init__(self, message, value):
    self.message = message
    self.value = value


def test_value(x):
  if x > 100:
    raise ValueTooHighError('value is too high')
  if x < 5:
    raise ValueTooSmallError('value is too small', x)

try:
  test_value(200)
except ValueTooHighError as e:
  print(e)
except ValueTooSmallError as e:
  print(e.message, e.value)

