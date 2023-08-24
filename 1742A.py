x = int(input())
while x > 0:
    y = list(map(int, input().split()))
    if sum(y) - max(y) == max(y):
        print('YES')
    else:
        print('NO')
    x -= 1
