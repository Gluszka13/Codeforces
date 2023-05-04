'''
x=input()
y=[]
for i in x:
    if i not in y:
        y.append(i)
    else:
        continue
if len(y)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!" )      

'''
x=input()
y=list(x)
y.sort()
i=0
c=1


for i in range(len(y)-1):
    if y[i]!=y[i+1]:
        c=c+1
    else:
        c=c+0

if c%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!" )
