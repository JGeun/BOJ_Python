import sys
N = int(sys.stdin.readline())
words = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    if word not in words:
        words.append(word)
words.sort(key=lambda x: (len(x), x))

for word in words:
    sys.stdout.write(word + "\n")
