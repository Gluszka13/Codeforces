k, r = map(int,input().split())
p = k
if k < r and r % k == 0:
    print(r // k)
else:
    for i in range(1,k*10):
        if k % 10 == r or k % 10 == 0:
            if i == 1:
                print(i)
                break
            else:
                print(i - 1)
                break
        else:
            k = p * i
            continue