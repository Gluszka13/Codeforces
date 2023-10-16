t = int(input())
while t > 0:
    a = list(map(int,input().split()))
    a.sort()
    t -= 1
    print(a[1])