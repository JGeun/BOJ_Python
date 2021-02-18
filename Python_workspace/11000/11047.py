import sys
N, K = map(int, sys.stdin.readline().split())
moneyUnit = []
for _ in range(N):
    moneyUnit.append(int(sys.stdin.readline()))

count = 0
for i in range(1, N+1):
    unit = moneyUnit[-i]

    if K >= unit:
        count += K // unit
        K %= unit

sys.stdout.write(str(count)+'\n')