no_A = int(input())
A = set(input().split())
N = int(input())
total = 0
for i in range(N):
    operation = []
    operation = input().split()
    new_set = set(input().split())
    if operation[0] == 'intersection_update':
        A.intersection_update(new_set)
    elif operation[0] == 'update':
        A.update(new_set)
    elif operation[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(new_set)
    elif operation[0] == 'difference_update':
        A.difference_update(new_set)

print(sum(set(map(int, A))))