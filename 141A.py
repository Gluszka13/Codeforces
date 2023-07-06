a = input()
b = input()
ab = input()
mix = a + b
if len(mix) != len(ab):
    print('NO')
    exit()
else:
    for i in mix:
        if mix.count(i) != ab.count(i):
            print('NO')
            exit()
print('YES')

