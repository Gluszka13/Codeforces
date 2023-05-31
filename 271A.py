'''
y = input()
c = set(y)
n = len(c)
y = int(y)
x = y + 1
x = str(x)
b = set(x)
t = False

if n == 4:
    if len(b) == 4:
        print(x)
        t = True

while len(b) != 4:
    x = int(x)
    x = x + 1
    x = str(x)
    b = set(x)
if t == False:
    print(x)
'''
x = int(input()) + 1
while len(set(str(x))) != 4:
    x+=1
print(x)