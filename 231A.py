s=0
n=int(input())
while n>0:
    a,b,c=map(int, input().split())
    d=a+b+c
    if d>=2:
        s+=1
    n-=1
print(s)