import sys
import math
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(A*B//math.gcd(A, B))+'\n')