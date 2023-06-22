n = int(input())
a = list(map(int, input().split()))
x = max(a)
y = min(a)
if a[0] == x and a[n-1] == y:
    print(0)
else:
    M = a.index(max(a))
    N = a.index(min(a))
    d = []
    for i in range(len(a)):
        if a[i] == y:
            d.append(i)
    if len(d) == 1:
        g = 0
        g = d[0]  
    else:
        g = d.index(max(d))
        g = d[g]
    if M > g:
        a.pop(M)
    c = M + (len(a) - g) - 1
    print(c)