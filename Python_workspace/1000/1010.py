import sys
import math
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(math.factorial(M)//math.factorial(M-N) // math.factorial(N))+'\n')