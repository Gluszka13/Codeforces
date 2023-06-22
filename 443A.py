w = input()
import string
a = string.ascii_lowercase
y = []
for i in w:
    if i in a:
        y.append(i)
b = []
for i in y:
    if i not in b:
        b.append(i)
x = len(b)
print(x)