t = int(input())
for i in range(t):
    n = int(input())
    res = []
    pow = 1
    while n > 0:
        d = n % 10
        if d > 0:
            res.append(d * pow)
        n = n // 10
        pow = pow * 10
    print(len(res))
    print(' '.join(map(str, res)))
'''
l = int(input())
while l > 0:
    n = input()
    l -= 1
    if len(n) == 1:
        k = 1
        a = n
    else:
        a =[]
        k = len(n) - n.count('0')
        for i in range(len(n)):
            if n[i] != '0':
                a.append(n[i] + '0' * (len(n) - i - 1))             
    print(k)
    print(' '.join(a))
'''