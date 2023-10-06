t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int,input().split()))
    t -= 1
    x = min(a)
    y = max(a)
    xy = y -x
    print(xy)