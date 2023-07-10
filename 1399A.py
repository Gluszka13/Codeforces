'''
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    i = 0
    while n > 1:
        if abs(a[i] - a[i+1]) == 1 or a[i] == a[i+1]:
            a.pop(i)
        n -=1
    if len(a) == 1:
        print("YES")
    else:
        print("NO")
'''

t = int(input())
for i in range(t):
    n = int(input())
    xs = list(map(int, input().split()))
    xs.sort()
    ok = True
    for j in range(1, n):
        if xs[j] - xs[j-1]>1:
            ok=False
    if ok:
        print('YES')
    else:
        print('NO')