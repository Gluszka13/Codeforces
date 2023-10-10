t = int(input())
while t > 0:
    n = int(input())
    t -= 1
    coin1 = n // 3
    coin2 = coin1
    if n % 3 == 1:
        coin1 += 1
    elif n % 3 == 2:
        coin2 += 1
    print(coin1, coin2)