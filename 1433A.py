t = int(input())
len_to_x = {
    1: 1,
    2: 3,
    3: 6,
    4: 10,
}
while t > 0:
    n = input()
    x = len_to_x[len(n)]
    y = n[0]
    y = int(y)
    apart = (y - 1) * 10 + x
    print(apart)
    t -= 1