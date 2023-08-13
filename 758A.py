n = int(input())
a = list(map(int,input().split()))
m = max(a)
S = []
for i in range(len(a)):
    s = m - a[i]
    S.append(s)
print(sum(S))
