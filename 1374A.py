t = int(input())
while t > 0:
    x, y, n = map(int,input().split())
    t -= 1
    a = (n - y) // x
    k = a * x + y
    print(k)