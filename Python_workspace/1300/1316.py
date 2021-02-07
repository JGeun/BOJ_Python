N = int(input())
count = 0
for _ in range(N):
    indexList = []
    word = input()
    isGroupWord = True
    for i in range(len(word)):
        if word[i] not in indexList:
            indexList.append(word[i])
        else:
            if word[i] in indexList and indexList[len(indexList)-1] != word[i]:
                isGroupWord = False
                break
    if isGroupWord:
        count += 1
print(count)


