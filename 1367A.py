t = int(int(input()))
while t > 0:
    b = input("") 
    a =[b[0], b[1]]
    t -= 1
    for i in range(2, len(b)):
        if i % 2 != 0:
            a.append(b[i])
    print("".join(a))