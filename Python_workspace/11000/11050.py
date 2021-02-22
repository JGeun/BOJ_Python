import sys
import math
N, K = map(int, sys.stdin.readline().split())

sys.stdout.write(str(math.factorial(N)//math.factorial(N-K) // math.factorial(K))+'\n')