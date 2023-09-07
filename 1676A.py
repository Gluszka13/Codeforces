x = int(input())
while x > 0:
    y = input()
    x -= 1
    a = []
    b = []
    i = 0
    while i < 6:
        if i == 0 or i == 1 or i ==2:
            a.append(int(y[i]))
        else:
            b.append(int(y[i]))
        i += 1
    a = sum(a)
    b = sum(b)
    if a == b:
        print('YES')
    else:
        print('NO')
    