
# program to display the fibonacci value given an n number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n_terms = 4
print(fibonacci(n_terms))


# program to display the fibonacci secuence given an n number of iterations
def fibonacci_list(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

fib = fibonacci_list(5)
for i in fib:
    print(i)
