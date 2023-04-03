LOCAL=False
if LOCAL:
    input_file = open('input.txt')

def read():
    if LOCAL:
        return input_file.readline()
    return input()


n, k = map(int, read().split())
x =list(map(int, read().split()))
c = 0

for i in x:
    if i>=x[k-1] and i>0:
        c+=1

print(c)
            

    


"""
def solve():
    n, k = map(int, read().split())
    i = 0
    while i != k:
        x = int(read())
        if x == 0:
            return i
        i +=1
    while i != n:
        y = int(read())
        if y == x:
            i +=1
        else:
            break
    return i

i = solve()
print(i)
"""