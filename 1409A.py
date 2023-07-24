t = int(input())
while t > 0:
    t -= 1
    b, a = map(int, input(). split())
    if a == b:
        print(0)
    elif a <= 10 and b <= 10:
        print(1)
    else:
        k = 0
        while b != a:
            w = abs(a - b)
            if w <= 10:
                print(1)
            else:
                k = w//10
                s = (k * 10) - w
                if s == 0:
                    print(k)
                else:
                    print(k+1)
            break
            