n = int(input())
while n > 0:
    n -= 1
    t = int(input())
    w = list(map(int, input().split()))
    a1 = max(w)
    b1 = min(w)
    a = w.count(a1)
    b = w.count(b1)
    if a < b:
        print(w.index(a1)+1)
    else:
        print(w.index(b1)+1)
'''
t = int(input())
for _ in range(t):
    n = int(inpu())
    a = list(map(tint, input().split()))
    x = sorted(a[:3])[1]
    for i in range(n):
        if a[i] != x:
            print(i + 1)
            break
'''