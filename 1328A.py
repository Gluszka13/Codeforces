t = int(input())
for i in range(t):
   a, b = map( int,input().split())
   if a % b == 0:
       print('0')
   else:
       print(b - (a % b))

'''
t = int(input())
y =[]
while t > 0:
    a, b = map( int,input().split())
    c = 0
    while a % b != 0:
        a += 1
        c += 1
    y.append(c)
    t -= 1

for i in y:
    print(i)
'''