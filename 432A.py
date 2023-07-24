n, k = map(int, input().split())
y = list(map(int, input().split()))
b = 0
for i in range(len(y)):
    if y[i] + k <= 5:
        b += 1
    else:
        continue
print(b // 3)
