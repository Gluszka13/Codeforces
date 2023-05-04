s = input()
r = ""
l = [0,0,0]
n = len(s)

if n == 1:
    print(s)
    
else:
    for i in range(n):
        if s[i] == "1":
            l[0] += 1
        elif s[i] == "2":
            l[1] += 1
        elif s[i] == "3":
            l[2] += 1
            
    for i in range(l[0]):
        r += "1+"
    for i in range(l[1]):
        r += "2+"
    for i in range(l[2]):
        r += "3+"
    
    print(r[0:-1])