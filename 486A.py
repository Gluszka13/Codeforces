def slove():
    n = int(input())
    if n%2==0:
        return n//2
    else:
        y=(n-1)//2    
        return y-n

print (slove())