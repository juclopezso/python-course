
# mypy: helps to hint arg types and return types
# installed via pip install mypy
# run as "mypy type_hinting.py"

def add(a: int, b: int) -> int:
  return a + b

# print(add("hello", "world")) # mypy will throw an error
print(add(1, 2)) # success


def print_name(name: str) -> None:
  print(name)

print_name("John") # success

# since python 3.9 list can be hinted as well
def add10(numbers: list[int]) -> list[int]:
  return [n + 10 for n in numbers]

print(add10([1, 2, 3])) # success
