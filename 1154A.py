numbers = list(map(int,input().split()))
numbers.sort()
b = numbers[3] - numbers[0]
c = numbers[3] - numbers[1]
a = numbers[3] - numbers[2]
print(a, b, c)
