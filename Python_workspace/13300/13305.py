import sys
N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
needOil = 0

min = oil[0]
index = 0
for i in range(len(oil)-1):
    if min > oil[i]:
        min = oil[i]
    needOil += min * distance[i]

sys.stdout.write(str(needOil)+'\n')