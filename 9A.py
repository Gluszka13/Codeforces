points = list(map(int, input().split()))
a = max(points)
dic_probability = {
    1: '1/1',
    2: '5/6',
    3: '2/3',
    4: '1/2',
    5: '1/3',
    6: '1/6',
}
x = dic_probability[a]
print(x)