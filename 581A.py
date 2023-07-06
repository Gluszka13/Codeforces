sock  = list(map(int,input().split()))
a = min(sock)
b = max(sock)
c = abs(a - b) // 2
print(a, c)