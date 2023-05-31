n = int(input())
m = list(map(int, input().split()))
y = [0]*n

for i in range(n + 1):
    y[m[i]] = i
    y.append(i)
print(y)