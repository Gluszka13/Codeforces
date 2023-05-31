n = int(input())
x = list(map(int, input().split()))
y = sum(x)
if y == 0:
    print('EASY')
else:
    print('HARD')