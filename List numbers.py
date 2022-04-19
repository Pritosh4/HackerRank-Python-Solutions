def list_numbers(n):
    print(n)
    if n==1:
        return 0
    else:
        return list_numbers(n-1)

list_numbers(9)
