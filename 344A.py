n = int(input())
p = int(input())
c = 1
while n - 1 > 0:
    n -= 1
    x = int(input())
    if p != x:
        c += 1
        p = x
print(c)
