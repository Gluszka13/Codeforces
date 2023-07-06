way = list(map(int,input().split()))
way.sort()
s = (way[2] - way[1])+(way[1] - way[0])
print(s)