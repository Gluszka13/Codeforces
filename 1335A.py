t = int(input())
a = []
while t > 0:
    n = int(input())
    t -= 1
    if n % 2 == 0:
        b = (n // 2) - 1
    else:
        b = n // 2
    a.append(b)
for i in a:
    print(i)

        