'''
n,k=input().split()
k=int(k)
x=len(n)
c=n[x-1]
c=int(c)
s=0

while k>0:
    n=str(n)
    x=len(n)
    k=k-1
    c=n[x-1]
    c=int(c)
    n=int(n)
    if c>0:
        n=n-1
    else:
        n=n//10
print(n)
'''
n,k=map(int,input().split())
while k>0:
    k-=1
    d=n%10
    if d>0:
        n=n-1
    else:
        n=n//10
print(n)