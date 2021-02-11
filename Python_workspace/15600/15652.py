import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, N+1)]
caseList = list(combinations_with_replacement(nums, M))
for case in caseList:
    sys.stdout.write(' '.join(map(str, case))+"\n")