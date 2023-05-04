n=int(input())
s=input()
i=0
x=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        continue
    else:
        x+=1
print(x)