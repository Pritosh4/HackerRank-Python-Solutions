def factorial_recursive(n):
    if n>1:
        return n*factorial_recursive(n-1)
    else:
        return n

print(factorial_recursive(5))
