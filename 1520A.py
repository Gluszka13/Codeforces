def is_teacher_suspicious(n, order):
    last_occurrence = {}
    for i in range(n):
        if order[i] in last_occurrence and last_occurrence[order[i]] != i - 1:
            return "NO"
        last_occurrence[order[i]] = i
    return "YES"
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    order = input().strip()
    result = is_teacher_suspicious(n, order)
    print(result)