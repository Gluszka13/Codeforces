t = int(input())
while t > 0:
    x = int(input())
    t -= 1
    if x <= 1399:
        print('Division 4')
    elif x >= 1400 and x <= 1599:
        print('Division 3')
    elif x >= 1600 and x <= 1899:
        print('Division 2')
    else:
        print('Division 1')