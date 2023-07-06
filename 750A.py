n, k = map(int, input().split())
while n > 0:
    if 5 * n * (n + 1) // 2 + k <= 240:
        break
    n -= 1
print(n)
'''
n, k = map(int,input().split())
c = []
n1 = 0
m = 240
rest = m - k
for i in range(n+1):
    c.append(i*5)
tim = (sum(c))
if tim <= rest:
    print(n)
else:
    for x in c:
        rest = rest - x
        if rest >= 0:
            n1 += 1
        else:
            break
    print(n1 - 1)
'''