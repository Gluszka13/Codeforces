n=int(input( ))
x=0
while n>0:
    y=str(input( ))
    n=n-1
    if y=="X++" or y=="++X":
        x+=1
    else:
        x-=1
print(x)