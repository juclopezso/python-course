# with threading and multiprocessing we can run code in parallel

# Process
# It's an instance of a program (e.g. a Python interpreter or a shell)
# process can have multiple threads inside
# - Takes advante of multiple CPUs and core
# - Separate memory space, memory is not shared between processes
# - Great fro CPU-bound processing: its good to use it when we have a big task to do
# - New process is started independently from other processes
# - Processes are interruptable and killable
# - One GIL for each process, avoids GIL limitations
# Disadvantages:
# - Heavy weight
# - Starting a process is slower than a thread
# - More memory is used
# - IPC (Inter Process Communication) is more complex


# Thread
# It's an entity within a process that can be scheduled for execution (also known as lightweight process)
# A process can spawn multiple threads
# - All threads share the same memory space
# - Light weight
# - Starting a thread is faster than a process
# - Great for I/O-bound processing: its good to use it when we have a lot of waiting time
# -- Or when the program need to talk to the outside world (e.g. network, database, etc.)
# Disafvantages:
# - GIL allows just one thread at a time, there is no parallelism
# - No effect for CPU-bound tasks
# - Not interruptable or killable. Could cause memory leaks
# - Careful with raced conditions. Threads share the same memory space, so if two threads try to access the same variable at the same time, the result can be unpredictable

# GIL: Global Interpreter Lock: 
# is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. 
# - Alock that allows only one thread at a time to execute Python 
# - Needed in CPython because memory management is not thread-safe
# Avoid:
# - Use multiprocessing
# - Use a different, free-threaded Python implementation (e.g. Jython, IronPython, PyPy, etc.)
# - Use Python as a wrapper for third-party libraries written in other languages (C, C++) -> numpy, scipy

# Multiprocessing
from multiprocessing import Process
import os 
import time

# dummy example
def square_numbers():
  for i in range(100):
    i * i
    time.sleep(0.1)

processes = []
num_processes = os.cpu_count() # number of cores of the machine

# create processes
for i in range(num_processes):
  # p = Process(target=square_numbers, args=())
  p = Process(target=square_numbers)
  processes.append(p)

if __name__ == '__main__':

  # start processes
  for p in processes:
    p.start()

  # join processes: wait for a process to finish. Blocking the main thread until all processes finished
  for p in processes:
    p.join()

  # execute code after all processes finished
  print('end main P')


# Threading
from threading import Thread

threads = []
num_threads = 10

for i in range(num_threads):
  t = Thread(target=square_numbers)
  threads.append(t)

if __name__ == '__main__':

  # start processes
  for t in threads:
    t.start()

  # join threads
  for t in threads:
    t.join()

  # execute code after all processes finished
  print('end main T')
