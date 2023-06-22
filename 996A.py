n = int(input())
a = [100, 20, 10, 5, 1]
c = 0
for i in a:
    if n >= i:
        y = n // i
        n = n - (y * i)
        c += y
print(c)