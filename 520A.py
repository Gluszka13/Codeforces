n = int(input())
word1 = input()
w = word1.lower()
import string
alphabet1 = string.ascii_lowercase
alphabet = set(alphabet1)
word = set(w)
x = alphabet - word
if len(x) == 0:
    print('YES')
else:
    print('NO')