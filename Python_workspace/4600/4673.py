selfNumber = [True]*10001
for index in range(1, 10001):
    num = index
    for j in range(len(str(index))):
        num += int(str(index)[j])

    if num < 10001:
        selfNumber[num] = False

for i in range(1, 10001):
    if selfNumber[i]:
        print(i)