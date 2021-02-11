import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, N+1)]
permutationList = list(permutations(nums, M))
for caseList in permutationList:
    sys.stdout.write(' '.join(map(str, caseList))+"\n")