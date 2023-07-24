n = int(input())
if n % 2 == 1:
    print(9, n-9)
else:
    print(4, n-4)
'''
n = int(input())
for i in range(4, n):
    if i % 2 == 0 or i % 3 == 0:
        x = i
        y = n - i
        if y  % 2 == 0 or y % 3 == 0:
            print(x, y)
            break
        else:
            continue
'''