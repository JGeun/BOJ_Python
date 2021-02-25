import sys
import math
N = int(sys.stdin.readline())
numStr = str(math.factorial(N))
count = 0
for i in range(1, len(numStr)+1):
    if numStr[-i] == '0':
        count += 1
    else:
        sys.stdout.write(str(count)+'\n')
        break
