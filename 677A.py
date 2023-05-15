n, h = map(int,input().split())
a = list(map(int,input().split()))
x = 0
i = 0
while n > 0:
    if a[i] > h :
        x = x + 2
        i += 1
    else:
        x =x + 1
        i += 1
    n = n - 1
    
print(x)