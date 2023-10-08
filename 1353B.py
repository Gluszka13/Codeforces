t = int(input())
while t > 0:
    n, k = map(int,input().split())
    t -= 1
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    i = 0
    while k > 0:
        if b[i] > a[i]:
            y = b[i]
            a.pop(i)
            b.pop(i)
            a.append(y)
            k -= 1
        else:
            k -= 1
    max_sum = sum(a)
    print(max_sum)