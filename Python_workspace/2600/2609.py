import sys
import math
M, N = map(int, sys.stdin.readline().split())
sys.stdout.write(str(math.gcd(M, N))+'\n')
sys.stdout.write(str(M*N//math.gcd(M, N))+'\n')
