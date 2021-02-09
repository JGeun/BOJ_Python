N = int(input())
personList = []
for _ in range(N):
    weight, height = map(int, input().split())
    personList.append([weight, height])

for i in range(N):
    count = 1
    for j in range(N):
        if i != j and personList[i][0] < personList[j][0] and personList[i][1] < personList[j][1]:
            count += 1
    print(count, end=' ')