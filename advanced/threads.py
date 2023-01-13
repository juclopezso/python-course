from threading import Thread, Lock, current_thread
import time

# shared data
database_value = 0

def increase(lock):
  global database_value

  # race condition: two threads can read the same value and write the same value
  # prevent the race condition locking the state
  lock.acquire()
  local_copy = database_value

  # processing
  local_copy += 1
  time.sleep(0.1)

  database_value = local_copy
  lock.release() # remember to release the lock

  # could be done also with a context manager
  # with lock:
  #   local_copy = database_value
  #   local_copy += 1
  #   time.sleep(0.1)
  #   database_value = local_copy


if __name__ == '__main__':

  lock = Lock()
  print('starting value', database_value)

  thread1 = Thread(target=increase, args=(lock,))
  thread2 = Thread(target=increase, args=(lock,))

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  print('end value', database_value)


# Queues are thread-safe and process safe
from queue import Queue

def worker(q, lock):
  while True:
    value = q.get() # block and wait until items are available
    # processing...
    with lock:
      print(f'in {current_thread().name} got {value}')

    q.task_done() # notify the queue that the processing is done


if __name__ == '__main__':

  lock = Lock()
  q = Queue() # FIFO

  num_threads = 10

  for i in range(num_threads):
    thread = Thread(target=worker, args=(q, lock))
    # a daemon thread dies when the main thread dies
    thread.daemon = True # this kills the process
    thread.start()
  
  # put items in the queue 
  for i in range(1, 21):
    q.put(i)

  q.join() # block until all items are processed

  print('end queue')