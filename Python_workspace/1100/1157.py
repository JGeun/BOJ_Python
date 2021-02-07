alpha = [0]*26
word = input().upper()
for i in range(len(word)):
    alpha[ord(word[i])-ord("A")] += 1

max = 0
alphaList = []
for i in range(26):
    if alpha[i] > max:
        alphaList.clear()
        max = alpha[i]
        alphaList.append(i)
    elif alpha[i] == max:
        alphaList.append(i)

if not len(alphaList) == 1:
    print("?")
else:
    print(chr(alphaList[0]+ord("A")))