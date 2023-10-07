t = int(input())
while t > 0:
    a, b = map(int, input().split())  
    max_side = max(a, b)
    min_side = min(a, b)
 
    if min_side * 2 >= max_side:
        square_area = (min_side * 2) ** 2
    else:
        square_area = (max_side) ** 2
 
    print(square_area)
    t -= 1