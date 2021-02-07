alpha = [-1] * 26
S = input()
for i in range(len(S)):
    index = ord(S[i]) - ord("a")
    if alpha[index] == -1:
        alpha[index] = i

for i in range(26):
    print(alpha[i], end=' ')
