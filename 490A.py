n = int(input())
r = list(map(int,input().split()))
a = r.count(1)
b = r.count(2)
c = r.count(3)
if a == 0 or b == 0 or c == 0:
    print(0)
else:
    l = [a, b, c]
    team = min(l)
    print(team)
    a1 = []
    b1 = []
    c1= []
    for i in range(len(r)):
        if r[i] == 1:
            a1.append((i)+1)
        elif r[i] == 2:
            b1.append((i)+1)
        else:
            c1.append((i)+1)
    i = 0
    while team > 0:
        y = []
        y.append(a1[i])
        y.append(b1[i])
        y.append(c1[i])
        i += 1
        team -= 1
        y = list(map(str, y))
        print(' '.join(y))
'''
n = int(input())
t = list(map(int, input().split()))
a = [[], [], []]
for i in range(n):
    a[t[i] - 1].append(i + 1)
r = min(map(len, a))
print(r)
for i in range(r):
    print(a[0][i], a[1][i], a[2][i])
'''