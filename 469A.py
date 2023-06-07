n = int(input())
p = list(map(int, input().split()))
p.pop(0)
p = set(p)
q = list(map(int, input().split()))
q.pop(0)
q = set(q)
x = p.union(q)
x = list(x)
b = sum(x)
if b > 0:
    if x[0] == 0:
            x.remove(x[0])
if len(x) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')