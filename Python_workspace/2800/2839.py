N = int(input())
minInt = 9999

for i in range(N//5, -1, -1):
    count = 0
    value = N
    value -= i*5
    if value % 3 == 0:
        count = value // 3 + i
        if count < minInt:
            minInt = count

if minInt == 9999:
    print(-1)
else:
    print(minInt)
