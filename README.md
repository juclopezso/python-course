# Python Intermediate to Advanced Course


## Extra notes
[Advanced Python](https://github.com/patrickloeber/python-engineer-notebooks/tree/master/advanced-python)

# Summary

- Variables are dynamicly typed

### Sorting
```
arr = ["bob", "alice", "jane"]
arr.sort()
print(arr)
# custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)
```
### Strings
- Strings are inmutable

### Queues (double ended queue)
```
from collection import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
queue.popleft()
queue.appendleft(1)
queue.pop()
```
