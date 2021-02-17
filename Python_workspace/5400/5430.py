import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().rstrip().replace('RR', '')
    n = int(sys.stdin.readline())
    numList = sys.stdin.readline()[1:-2].split(",")
    isError = False
    for i in range(len(p)):
        if p[i] == 'R':
            numList.reverse()
        else:
            if n == 0 or len(numList) == 0:
                isError = True
                break
            else:
                numList.pop(0)
    if isError:
        sys.stdout.write('error\n')
    else:
        sys.stdout.write('['+ ','.join(numList)+']\n')