def fibonacci_recursive(n, a=1, b=1):
    if n>1:
        return fibonacci_recursive(n-1, b, a+b)
    else:
        return a + b
fib = fibonacci_recursive(3)
print(fib)
