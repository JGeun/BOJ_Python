import sys
import math
N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(numList)):
    sys.stdout.write(str(numList[0] // math.gcd(numList[0], numList[i])) + '/' + str(numList[i] // math.gcd(numList[0], numList[i]))+'\n')
