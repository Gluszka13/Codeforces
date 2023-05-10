s=input()
n=len(s)
c=0
i=0
for i in s:
    if i>='a'and i<='z':
        c+=1
if c>=(n/2):
    print(s.lower())
else:
    print(s.upper())


