t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    t-=1
    data1 = 0
    data2 = 0
    if len(a) == 1:
        if a[0] % 2 == 0:
            print(0)
        else:
            print(-1)
    else:
        for i in range(0,n,2):
            if a[i] % 2 == 0:
                continue
            else:
                data1 += 1
        for j in range(1,n,2):
            if a[j] % 2 != 0:
                continue
            else:
                data2 += 1
        data = data1+data2
        if data1 != data2:
            print(-1)
        else:
            print(data // 2)
            
    
        