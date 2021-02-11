import sys
K = int(sys.stdin.readline())
numList = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        numList.pop()
    else:
        numList.append(num)
sys.stdout.write(str(sum(numList))+"\n")