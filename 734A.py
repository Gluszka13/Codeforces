n=int(input())
s=input()
a=0
b=0

for i in s:
    if i=="A":
        a=a+1
    else:
        b=b+1
if a>b:
    print("Anton")
if b>a:
    print("Danik")
if a==b:
    print("Friendship")