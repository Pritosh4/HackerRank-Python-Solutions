n = int(input())
lst=map(int, input().split())
res=[]
for i in lst:
    if i not in res:
        res.append(i)
res.sort()
a= res[::-1]

print(a[1])
