n = int(input())
s = m = 0
for i in range(n):
    a, b = map(int, input().split())
    s += b - a
    m = max(m, s)
print(m)
