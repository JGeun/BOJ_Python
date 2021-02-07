T = int(input())
for i in range(T):
    line = input().split()
    for j in range(len(line[1])):
        for _ in range(int(line[0])):
            print(line[1][j], end='')
    print()
