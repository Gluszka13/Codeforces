t = int(input())
while t > 0:
    a, b, c = map(int,input().split())
    t -= 1
    if a + b == c:
        print('+')
    else:
        print('-')