n = int(input())
home = []
out = []
while n>0:
    a, b = map(int, input().split())
    home.append(a)
    out.append(b)
    n -= 1
t = 0
for i in home:
    for j in out:
        if i == j:
            t += 1
print(t)