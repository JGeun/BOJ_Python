N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())

check = ['W', 'B']
count = []
for row in range(N-7):
    for column in range(M-7):
        blockCount = 0
        for i in range(row, row+8):
            for k in range(column, column+8):
                if board[i][k:k+1] != check[(k+i)% 2]:
                    blockCount += 1
        count.append(blockCount)
        blockCount = 0
        for i in range(row, row + 8):
            for k in range(column, column + 8):
                if board[i][k:k+1] != check[(k+i+1) % 2]:
                    blockCount += 1
        count.append(blockCount)

print(min(count))