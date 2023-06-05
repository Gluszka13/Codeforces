c = int(input())
n = c
y = []
while c > 1 :
    for i in range(1, c):
        if i % 2 == 0:
            y.append('I love that')
            c -= 1
        else:
            y.append(' I hate that ')
            c -= 1
while c == 1:
    if n % 2 == 0:
        y.append('I love it')
        c -= 1
    else:
        y.append(' I hate it')
        c -= 1
print((''.join(y)))