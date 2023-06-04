x = input()
y = input()
b = []
i = 0
c = len(x)
while c>0:
    c -= 1
    if x[i] == y[i]:
        b.append('0')
        i += 1
    else: 
        b.append('1')
        i +=1
print(''.join(b))