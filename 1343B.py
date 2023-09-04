t = int(input())
while t > 0:
    y = int(input())
    l = []
    t -= 1
    if y % 2 != 0 and y < 4:
        print('NO')
        continue
    y1 = y // 2
    y2 = y1
    i = 1
    while y1 > 0:
        if i % 2 == 0:
            l.append(i)
            i += 1
        else:
            i += 1
            continue
        y1 -= 1

    half1 = sum(l)
    i = 1
    while y2 > 1:
        if i % 2 != 0:
            l.append(i)
            i += 1
        else:
            i += 1
            continue
        y2 -= 1
    half2 = sum(l)
    all = half1*2 - half2
    l.append(all)
    if all % 2 == 0:
        print('NO')
    elif sum(l) == half1*2:
        print('YES')
        print(' '.join(map(str, l)))
    else:
        print('NO')

