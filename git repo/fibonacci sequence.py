# Question 2:fibonacci sequence

def fibonacci(n):
    if n in [0, 1]:
     return n
    else:
     return fibonacci(n-1) + fibonacci(n-2)


FibonacciSeries = [fibonacci(n) for n in range(15)]
print(FibonacciSeries)

