n = int(input())
data = map(int, input().split())

res = 0
p = 0
for x in data:
    if x > 0:
        p += x
    elif p == 0:
        res += 1
    else:
        p -= 1
print(res)

"""
n = int(input())
l = list(map(int, input().split()))
p = 0
z = 0
for i in l:
    if p > 0 and i < 0:
        p -= 1
        continue
    if i < 0:
        z += 1
    if i > 0:
        p += i
        continue
print(z)
"""