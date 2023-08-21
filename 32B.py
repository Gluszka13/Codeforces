x = input()
b = []
i = 0
while i < len(x):
    if x[i] == '.':
        b.append('0')
        i += 1
    elif x[i] == '-' and x[i+1] == '.':
        b.append('1')
        i += 2
    else:
        b.append('2')
        i += 2
print(''.join(b))
