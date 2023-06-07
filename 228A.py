s = list(map(int, input().split()))
s.sort()
b = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        b += 0
    else:
        b += 1
print(b)