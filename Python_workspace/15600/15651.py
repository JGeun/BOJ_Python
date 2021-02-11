import sys
from itertools import product
N, M = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, N+1)]
caseList = list(product(nums, repeat=M))
for case in caseList:
    sys.stdout.write(' '.join(map(str, case))+"\n")