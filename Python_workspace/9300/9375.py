import sys
T = int(sys.stdin.readline())
for _ in range(T):
    wearType = []
    count = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        case, wear = sys.stdin.readline().rstrip().split()
        if wear not in wearType:
            wearType.append(wear)
            count.append(1)
        else:
            index = wearType.index(wear)
            count[index] += 1
    value = 1
    for i in range(len(count)):
        value *= (count[i]+1)
    sys.stdout.write(str(value-1)+'\n')
