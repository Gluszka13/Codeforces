n=int(input())
a,b=map(int,input().split())
l=[]
c=0
s=b-a
n=n-1
l.append(s)
while n>0:
    a,b=map(int,input().split())
    c=s-a
    l.append(c)
    s=b+c
    l.append(s)
    n-=1

l.sort()
l.reverse()
print(l[0])
