import sys
N, K = map(int, sys.stdin.readline().split())
moneyUnit = []
for _ in range(N):
    moneyUnit.append(int(sys.stdin.readline()))

moneyUnit.reverse()
count = 0
for unit in moneyUnit:
    if K == 0:
        sys.stdout.write(str(count)+'\n')
        break
    elif K >= unit:
        count += K // unit
        K %= unit