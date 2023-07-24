n, k, l, c, d, p, nl, np = map(int, input().split())
print(min(k*l//nl, c*d, p//np)//n)
'''
n, k, l, c, d, p, nl, np = map(int,input().split())
kl = k * l 
cd = c * d 
nnl = n * nl 
nnp = np * n 
toast = [ nnl, nnp, n]
have = [kl, p, cd]
H = 3
i = 0
soft = []
while H > 0:
    H -= 1
    t1 = have[i] // toast[i]
    soft.append(t1)
    i += 1
print(min(soft))
'''