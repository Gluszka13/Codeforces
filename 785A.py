n = int(input())
s = 0
while n > 0:
    n -= 1
    a = input()
    if a[0] == 'T':
        s += 4
    if a[0] == 'C':
        s += 6
    if a[0] == 'O':
        s += 8
    if a[0] == 'D':
        s += 12
    if a[0] == 'I':
        s += 20
print(s)
