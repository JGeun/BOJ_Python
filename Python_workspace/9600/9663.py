import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(range(N))
print(nums)
queenList = list(permutations(nums, N))
print(len(queenList))