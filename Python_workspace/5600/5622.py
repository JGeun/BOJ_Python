dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
dialSum = 0
for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            dialSum += dial.index(j)+3
            break
print(dialSum)