import sys
N, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(len(arr)):
    if arr[i] < X:
        print("{}".format(arr[i]), end=" ")