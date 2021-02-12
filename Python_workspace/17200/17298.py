import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(N)]
stack = []

for i in range(len(numList)):
    while stack and numList[stack[-1]] < numList[i]:
        result[stack.pop()] = numList[i]
    stack.append(i)
print(' '.join(map(str, result)))