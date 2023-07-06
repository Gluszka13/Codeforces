n=int(input())
data = list(map(int, input().split()))
mi = data[0]
ma = data[0]
res = 0
for x in data:
    if x > ma:
        ma = x
        res += 1
    elif x < mi:
        mi = x
        res += 1
print(res)
'''
n = int(input())
l = list(map(int, input().split()))
c = 0
minm = 0
maxi = 0
if n <= 1:
    print(0)
else:
    for i in range(1):
        if l[i] < l[i + 1]:
            minm = l[i]
            maxi = l[i+1]
            c +=1
        elif l[i] > l[i + 1]:
            minm = l[i+1]
            maxi = l[i]
            c +=1 
        elif l[i] == l [i+1]:
            minm = l[i+1]
            maxi = l[i]
    for x in range(2,len(l)):
        if l[x] > maxi:
            maxi = l[x]
            c += 1
        elif l[x] < minm:
            minm = l[x]
            c += 1
        else:
            continue
    print(c)
'''