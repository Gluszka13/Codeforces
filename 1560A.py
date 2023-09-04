t = int(input())
while t > 0:
    k = int(input())
    k = k - 1
    c = 1
    i = 0
    while i < k:
        c += 1
        if c % 3 == 0 or c % 10 == 3:
            continue
        else:
            i += 1
    print(c)
    t -= 1
    
    
    
        
    



