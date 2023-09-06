n = int(input())
m = []
c = []
while n > 0:
    a = list(map(int,input().split()))
    n -= 1
    if a[0] > a[1]:
        m.append(1)
    elif a[0] < a[1]:
        c.append(1)
    else:
        continue
m1 = sum(m)
c1 = sum(c)
if m1 > c1:
    print("Mishka")
elif m1 < c1:
    print("Chris")
else:
    print("Friendship is magic!^^")