# Context managers
# great tool for resource management
# allow to allocate and release resources precisely 

# with open file example
# much cleaner and concise
with open('notes.txt', 'w') as f:
  # correctly closes the file even if an exception is raised
  f.write('Hello World')

# sames as below. Not very clean
# file = open('notes.txt', 'w')
# try:
#   file.write('Hello World')
# finally:
#   file.close()

# Context manager for custom classes
class ManagedFile:
  def __init__(self, filename):
    print('init')
    self.filename = filename

  # executed as soon as we enter the context
  def __enter__(self):
    print('entering context')
    self.file = open(self.filename, 'w')
    return self.file

  def __exit__(self, exc_type, exc_value, exc_traceback):
    if self.file:
      self.file.close()
    # handle the exception
    if exc_type:
      print('exception has been handled', exc_value)

    print('exit context')
    return True # suppress the exception

with ManagedFile('notes.txt') as f:
  print('doing stuff...')
  f.write('hello world')
  f.some_missing_method() # to test the exception handling

print('continuing...')

# Context manager with function
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
  f = open(filename, 'w')
  try:
    yield f
  except Exception as e:
    print('exception has been handled', e)
  finally:
    f.close()

with open_managed_file('notes.txt') as f:
  print('doing stuff in context manager function...')
  f.write('hello world')
  f.something() # to test the exception handling

print('continuing...')

