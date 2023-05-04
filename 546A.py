k,n,w=map(int,input().split())
x=0
c=[]
y=0
for i in range(w+1):
    y=i*k
    c.append(y)
    i=i+1
x=sum(c)
if n>=x:
    b=0
else:
    b=abs(x-n)
    
print(b)


