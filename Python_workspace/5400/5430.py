import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().rstrip().replace('RR', '')
    n = int(sys.stdin.readline())
    numList = deque()
    nums = sys.stdin.readline()[1:-2].split(",")
    for num in nums:
        numList.append(num)
    isError = False
    reverse = 0

    for i in range(len(p)):
        if p[i] == 'R':
            reverse += 1
        else:
            if n == 0 or len(numList) == 0:
                isError = True
                break
            else:
                if reverse % 2 == 1:
                    numList.pop()
                else:
                    numList.popleft()
    if isError:
        sys.stdout.write('error\n')
    else:
        if reverse%2 == 1:
            numList.reverse()
        sys.stdout.write('[' + ','.join(numList)+']\n')