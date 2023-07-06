m ,n = map(int, input().split())
c = 0
for i in range(1, m+1):
    if i % 2 != 0:
        print(n*'#')
        c += 1
    if i % 2 == 0:
        if c % 2 != 0:
            print((n-1)*'.'+'#')
        else:
            print('#'+(n-1)*'.')