t = int(input())
while t > 0:
    l = list(map(int,input().split()))
    l1 = []
    t -= 1
    for i in range(1, 4):
        if l[i] > l[0]:
            l1.append(1)
        else:
            continue
    print(sum(l1))