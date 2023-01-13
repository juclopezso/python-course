# Multiprocessing
from multiprocessing import Process, Value, Array, Lock, Pool
import os 
import time


def add_100(number, lock):
  for i in range(100):
    time.sleep(0.01)
    with lock:
      number.value += 1
    # also works with lock.acquire() and lock.release()
    # lock.acquire()
    # number.value += 1
    # lock.release()

def add_100_arr(numbers, lock):
  for i in range(100):
    time.sleep(0.01)
    for i in range(len(numbers)):
      with lock:
        numbers[i] += 1

if __name__ == '__main__':

  lock = Lock()
  # Value and Array used to shared data between processes
  shared_number = Value('i', 0) # i = integer, d = double, f = float
  shared_array = Array('d', [1.0, 20.0, 300.0])
  print('Number at begining', shared_number.value)
  print('Array at begining', shared_array[:])

  p1 = Process(target=add_100, args=(shared_number, lock))
  p2 = Process(target=add_100, args=(shared_number, lock))

  p3 = Process(target=add_100_arr, args=(shared_array, lock))
  p4 = Process(target=add_100_arr, args=(shared_array, lock))

  p1.start()
  p2.start()
  p3.start()
  p4.start()

  p1.join()
  p2.join()
  p3.join()
  p4.join()

  print('Number at end', shared_number.value)
  print('Array at end', shared_array[:])


# Using queues
from multiprocessing import Queue


def square(numbers, q):
  for i in numbers:
    q.put(i * i)

def make_negative(numbers, q):
  for i in numbers:
    q.put(i * -1)


if __name__ == '__main__':
  q = Queue()
  numbers = range(1, 6)

  # both processes are writing to the same queue
  p1 = Process(target=square, args=(numbers, q))
  p2 = Process(target=make_negative, args=(numbers, q))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  while not q.empty():
    print(q.get()) # prints and removes the first element of the queue

# Process pool: managed multiple processed
# control a pool of worker processes to which jobs can be submitted.
# manage available resources and split for example data into smaller chunks which can then be processed in parallel

def cube(number):
  return number * number * number

if __name__ == '__main__':

  numbers = range(1, 11)
  pool = Pool()

  # Methods: map, apply, join and close and more...
  # this will allocate the pools, allocated the data and run the method in parallel
  result = pool.map(cube, numbers)
  # run just one function in the pool in one process
  # pool.apply(cube, numbers[0])

  pool.close()
  pool.join()

  print('Pool cube result', result)
