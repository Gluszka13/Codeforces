n = int(input())
x = list(map(int, input().split()))
r = [0, 0]
for i in range(n):
    idx = 0 if x[0] > x[-1] else -1
    r[i % 2] += x[idx]
    x.pop(idx)
print(r[0], r[1])
'''
n = int(input())
c = list(map(int,input().split()))
a = []
b =[]
i = 0
x = 0
while len(c) > 0:
    if n == 1 and (x + 1) % 2 == 0 or c[i] > c[i-1] and (x + 1) % 2 == 0:
        b.append(c[i])
        c.pop(0)
        n -= 1
        x += 1
    elif  c[i] < c[i-1] and (x + 1) % 2 == 0:
        b.append(c[i-1])
        c.pop(n-1)
        n -= 1
        x += 1
    elif n == 1 or c[i] > c[i-1]:
        a.append(c[i])
        c.pop(0)
        n -= 1
        x += 1
    elif c[i] < c[i-1]:
        a.append(c[i-1])
        c.pop(n-1)
        n -= 1
        x += 1
print(sum(a), sum(b))
'''