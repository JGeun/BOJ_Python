N = int(input())
for i in range(1, N+1):
    divideSum = i
    for j in range(len(str(i))):
        divideSum += int(str(i)[j])
    if divideSum == N:
        print(i)
        break
    if i == N:
        print(0)
        break