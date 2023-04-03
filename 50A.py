LOCAL=False
if LOCAL:
    input_file = open('input.txt')

def read():
    if LOCAL:
        return input_file.readline()
    return input()

M, N = map(int, read().split())
b = M*N
d = 2*1
print(b//d)
