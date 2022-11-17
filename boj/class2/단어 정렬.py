import sys

n = int(sys.stdin.readline())
word = set()
for _ in range(n):
    data = sys.stdin.readline().strip()
    word.add(data)
word = list(word)

word.sort(key=lambda x: (len(x), x))
for w in word:
    print(w)
