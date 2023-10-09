string = 'codeforces'
t = int(input())
while t > 0:
    x = input()
    t -= 1
    if x in string:
        print('YES')
    else:
        print('NO')