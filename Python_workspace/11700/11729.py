def hanoi(n, start, temp, end):
    if n == 1:
        move.append([start, end])
    else:
        hanoi(n - 1, start, end, temp)
        move.append([start, end])
        hanoi(n - 1, temp, start, end)


move = []
K = int(input())
hanoi(K, 1, 2, 3)

print(len(move))
for i in range(len(move)):
    print(move[i][0], move[i][1])