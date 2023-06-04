n = int(input())
m = list(map(int, input().split()))
y = [0]*n
for i in range (n):
    y[m[i]-1] = i+1
b = ""
for a in y:
	b += " " + str(a)
print(b)