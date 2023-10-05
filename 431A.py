a = list(map(int,input().split()))
s = input()
kcal = []
for i in range(len(s)):
    kcal.append(a[int(s[i]) - 1])
kcal = sum(kcal)
print(kcal)
'''
a = list(map(int,input().split()))
s = input()
kcal = []
for i in range(len(s)):
    if s[i] == '1':
        kcal.append(a[0])
    if s[i] == '2':
        kcal.append(a[1])
    if s[i] == '3':
        kcal.append(a[2])
    if s[i] == '4':
        kcal.append(a[3])
kcal = sum(kcal)
print(kcal)
'''