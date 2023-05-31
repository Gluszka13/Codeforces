n = int(input())
w = 0
while n > 0:
    n -=1
    p, q = map(int, input().split())
    if p + 2 <= q:
        w += 1

print(w)

