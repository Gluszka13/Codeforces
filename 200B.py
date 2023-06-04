n = int(input())
p = list(map(int, input().split()))
x = 0.0000
for i in p:
    x += float(i)/n
print(x)