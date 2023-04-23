LOCAL=False
if LOCAL:
    input_file = open('input.txt')

def read():
    if LOCAL:
        return input_file.readline()
    return input()

j = list(map(int, read().split()))
i=0
r=0
a=0
b=0
n=5

while sum(j)==0:
    j = list(map(int, read().split()))
    a+=1
for i in range(len(j)):
    if j[i]==0:
        b+=1
    else:
        break
r=abs(n//2-a)+abs(n//2-b)
print(r) 



        

    